
# https://www.geeksforgeeks.org/python-spell-corrector-gui-using-tkinter/

import re
import tkinter as tk
from tkinter import *
from replace import *
# from textblob import TextBlob # required by initial implementation

## initial implementation valid for English language only
'''
def correction(field1, field2): 
    # get a content from the first entry box 
    input_text = field1.get() 
 
	## all text corrections here
    # create a TextBlob object 
    blob_obj = TextBlob(input_text)
 
    # get a corrected word 
    output_text = str(blob_obj.correct()) 
 
    # insert the corrected text in the second entry box
    field2.insert(10, output_text) 
'''

## implementation for Albanian language
def correction(field_in, field_out):
	# get content from the first box
	input_text = field_in.get() 
	t = input_text ; total_sub = 0
		
	## call c substitutions 
	t, c = replace_c(t) ; total_sub += c
	
	## call e substitutions
	t, c = replace_e(t) ; total_sub += c
	
	## call word substitutions 
	t, c = replace_words(t) ; total_sub += c
	
	## call dialect substitutions
	t, c = replace_dial(t) ; total_sub += c
	
	## call english word substitutions
	t, c = replace_eng(t) ; total_sub += c

	output_text = t
	## insert the corrected text in the second box
	field_out.insert(10, output_text)
	## print number of total substitutions
	print(f"U kryen {total_sub} zëvendësime.")

## function to clear both text entry boxes
def clearAll(field1, field2):
	## whole content of the text area is deleted
	field1.delete(0, END)
	field2.delete(0, END)
	
## main execution code
if __name__ == "__main__":

	## create a GUI window with some specifications
	root = Tk()
	root.configure(background = "light green")	# background color of GUI
	root.geometry("350x200")					# size of GUI WidthxHeight
	root.title("Redaktor Teksti")				# main title of window
	
	## welcome message in the GUI
	headlabel = Label(root, text = "Mirë se vini te ky redaktor teksti",
					fg = "black", bg = "red")
	
	## create the label for the input text
	inlabel = Label(root, text = "Teksti Hyrës", fg = "black", bg = "green") 
	## create the label for the output text
	outlabel = Label(root, text = "Teksti Dalës", fg = "black", bg = "green")

	'''
	using grid method for placing widgets at respective positions in 
	table-like structure. padx keyword argument used to set pading along
	x asix.
	'''
	headlabel.grid(row = 0, column = 1) 
	inlabel.grid(row = 1, column = 0) 
	outlabel.grid(row = 3, column = 0, padx = 10) 
	
	## text entries for filling or typing the texts
	text1_field = Entry() ; text2_field = Entry()
	
	## padx and pady to set padding in x-axis and y-axis
	text1_field.grid(row = 1, column = 1, padx = 10, pady = 10)
	text2_field.grid(row = 3, column = 1, padx = 10, pady = 10)
	
	## correction button attached with correction function
	correct_button = Button(root, text = "Korrigjo", bg = "red", fg = "black", 
			command = lambda: correction(text1_field, text2_field))
	correct_button.grid(row = 2, column = 1)
	
	## clear button attached with clearAll function
	clear_button = Button(root, text = "Fshi", bg = "red", fg = "black",
			command = lambda: clearAll(text1_field, text2_field)) 
	clear_button.grid(row = 4, column = 1) 
	
	## start the GUI
	root.mainloop()
	
	
	
	