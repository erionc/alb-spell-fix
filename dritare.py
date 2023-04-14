
import tkinter as tk
from tkinter import *

# importimi i funksioneve korrigjuese nga modulet përkatëse
from redakto import *

## funksioni kryesor i redaktimeve që thërret funksionet e tjera
def redaktime(field_in, field_out, field_message):
	# merret përmbajtja e kutizës së parë
	input_text = field_in.get("1.0", END) 
	t = input_text ; c_subs, e_subs, tj_subs, total_sub = 0, 0, 0, 0
	
	## thirret funksioni kryesor i redaktimeve
	t, e_subs, c_subs, tj_subs = redakto(t)
	total_sub = c_subs + e_subs + tj_subs

	output_text = t

	output_message = f"Zëvendësime të ë-ve:\t\t\t{e_subs}\n" + \
		f"Zëvendësime të ç-ve:\t\t\t{c_subs}\n" + \
		f"Zëvendësime të tjera:\t\t\t{tj_subs}\n" + \
		f"Zëvendësime totale:\t\t\t{total_sub}"
	
	# # shfaqet totali i zëvendësimeve të kryera
	# if total_sub == 1:
	# 	output_message = str.format("{} zëvendësim. ", total_sub)
	# else:
	# 	output_message = str.format("{} zëvendësime. ", total_sub)
	
	# futet teksti i redaktuar te kutiza e dytë
	field_out.insert("1.0", output_text)
	# futet mesazhi i zëvendësimeve te kutiza e tretë
	field_message.insert("1.0", output_message)

## funksion që fshin tekstin nga kutizat
def fshiKrejt(field1, field2, field3):
	## fshihet e gjithë përmbajtja e fushës së tekstit
	field1.delete("1.0", END)
	field2.delete("1.0", END)
	field3.delete("1.0", END)
	
## pikënisja e ekzekutimit
if __name__ == "__main__":

	# krijohet ndërfaqja grafike me disa specifikime
	root = Tk()
	root.configure(background = "red")		# ngjyra e sfondit
	root.geometry("1200x1060")				# përmasat e dritares
	root.resizable(width=False, height=False)	
	
	# titulli i dritares kryesore
	root.title("REDAKTOR TEKSTI PËR GJUHËN SHQIPE")		
	
	# etiketa për tekstin hyrës
	inlabel = Label(root, text = "Hyrje", fg = "black", bg = "light green") 
	# etiketa për tekstin dalës (të redaktuar)
	outlabel = Label(root, text = "Dalje", fg = "black", bg = "light green")

	inlabel.grid(row = 1, column = 0, padx = 10) 
	outlabel.grid(row = 17, column = 0, padx = 10) 
	
	# tre fushat e tekstit 
	text1_field = Text(height=20, width=90, fg="white", bg="black")
	text2_field = Text(height=20, width=90, fg="white", bg="black")
	text3_field = Text(height=4, width=30, fg="white", bg="black")
	
	# pozicionimi i tre fushave të tekstit te dritarja kryesore
	text1_field.grid(row = 1, column = 1, padx = 7, pady = 7)
	text2_field.grid(row = 17, column = 1, padx = 7, pady = 7)
	text3_field.place(x=790, y=960) 
	
	# butoni i korrigjimit lidhet me funksionin e korrigjimeve
	correct_button = Button(root, text = "Redakto", bg = "cyan", fg = "black", command = lambda: redaktime(text1_field, text2_field, text3_field))
	correct_button.grid(row = 2, column = 1) # .place(x=790, y=300)
	
	# butoni i fshirjes lidhet me funksionin e fshirjes
	clear_button = Button(root, text = "Shuaj", bg = "cyan", fg = "black",
	command = lambda: fshiKrejt(text1_field, text2_field, text3_field)) 
	clear_button.grid(row = 18, column = 1) # .place(x=800, y=590)  
	
	# aktivizimi i dritares grafike
	root.mainloop()
