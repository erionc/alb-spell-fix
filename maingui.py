
import re
import tkinter as tk
from tkinter import *
from replace import *
from replace_e import *
from replace_c import *

## main correction function that calls other substitution functions
def correction(field_in, field_out, field_message):
	# get content from the first box
	input_text = field_in.get("1.0", END) 
	t = input_text ; total_sub = 0
	
	## call dependency substitutions
	t, c = replace_dep(t) ; total_sub += c
		
	## call e substitutions
	t, c = replace_e(t) ; total_sub += c
	
	## call c substitutions 
	t, c = replace_c(t) ; total_sub += c
	
	## call dialect substitutions
	t, c = replace_dial(t) ; total_sub += c
	
	## call word substitutions 
	t, c = replace_words(t) ; total_sub += c
	
	## call english word substitutions
	t, c = replace_eng(t) ; total_sub += c

	output_text = t
	output_message = str.format("{} zëvendësime. ", total_sub)
	## insert the corrected text in the second box
	field_out.insert("1.0", output_text)
	## insert the message in third box
	field_message.insert("1.0", output_message)

## function to clear both text entry boxes
def clearAll(field1, field2, field3):
	## whole content of the text area is deleted
	field1.delete("1.0", END)
	field2.delete("1.0", END)
	field3.delete("1.0", END)
	
## main execution code
if __name__ == "__main__":

	## create a GUI window with some specifications
	root = Tk()
	root.configure(background = "red")		# background color of GUI
	root.geometry("900x680")				# size of GUI WidthxHeight
	root.title("REDAKTOR TEKSTI PËR GJUHËN SHQIPE")		# main title of window
	
	## create the label for the input text
	inlabel = Label(root, text = "Hyrje", fg = "black", bg = "light green") 
	## create the label for the output text
	outlabel = Label(root, text = "Dalje", fg = "black", bg = "light green")

	'''
	using grid method for placing widgets at respective positions in 
	table-like structure. padx keyword argument used to set pading along
	x asix.
	'''
	inlabel.grid(row = 1, column = 0, padx = 7) 
	outlabel.grid(row = 17, column = 0, padx = 7) 
	
	## text entries for filling or typing the texts
	text1_field = Text(height=14, width=80, fg="white", bg="black")
	text2_field = Text(height=14, width=80, fg="white", bg="black")
	text3_field = Text(height=1, width=17, fg="white", bg="black")
	
	## padx and pady to set padding in x-axis and y-axis
	text1_field.grid(row = 1, column = 1, padx = 7, pady = 7)
	text2_field.grid(row = 17, column = 1, padx = 7, pady = 7)
	text3_field.place(x=693, y=637) 
	
	## correction button attached with correction function
	correct_button = Button(root, text = "Redakto", bg = "cyan", fg = "black", 
			command = lambda: correction(text1_field, text2_field, text3_field))
	correct_button.grid(row = 2, column = 1) # .place(x=790, y=300)
	
	## clear button attached with clearAll function
	clear_button = Button(root, text = "Shuaj", bg = "cyan", fg = "black",
			command = lambda: clearAll(text1_field, text2_field, text3_field)) 
	clear_button.grid(row = 18, column = 1) # .place(x=800, y=590)  
	
	## start the GUI
	root.mainloop()
	

