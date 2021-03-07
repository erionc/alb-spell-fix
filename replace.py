
import re
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
	t = input_text
	
	## all text corrections go here
	
	## full word substitution template
	# t = re.sub(r"eshte|ështe|eshtë", "është", t)
	
	## ç'kemi
	t = re.sub(r"(c|c'|ç)(kemi)", r"ç'\2", t)
	
	## Ç'kemi 
	t = re.sub(r"(C|C'|Ç)(kemi)", r"Ç'\2", t)
	
	## Është
	t = re.sub(r"(E|Ë)(sht)(e|ë)", r"Ë\2ë", t)
	
	## është
	t = re.sub(r"(e|ë)(sht)(e|ë)", r"ë\2ë", t)
	
	output_text = t
	## insert the corrected text in the second box
	field_out.insert(10, output_text)