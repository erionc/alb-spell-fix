
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
	t = input_text ; total_sub = 0
	
	## full word substitution template
	# t = re.sub(r"eshte|ështe|eshtë", "është", t)
	
	## call c substitutions 
	t, c = replace_cs(t) ; total_sub += c
	
	## call e substitutions
	t, c = replace_es(t) ; total_sub += c

	output_text = t
	## insert the corrected text in the second box
	field_out.insert(10, output_text)
	## print number of total substitutions
	print(f"U kryen {total_sub} zëvendësime.")
	
def replace_cs(text):
	## initializations 
	t = text ; c_subs = 0
	
	## ç'kemi
	t, c = re.subn(r"(c|c'|ç)(kemi)", r"ç'\2", t) ; c_subs += c
	## Ç'kemi 
	t, c = re.subn(r"(C|C'|Ç)(kemi)", r"Ç'\2", t) ; c_subs += c
	
	## çfarë 
	t, c = re.subn(r"(c|ç)(far)(e?)( |\.)", r"çfarë\4", t) ; c_subs += c
	## Çfarë
	t, c = re.subn(r"(C|Ç)(far)(e?)( |\.)", r"Çfarë\4", t) ; c_subs += c
	
	return (t, c_subs)
	
	

def replace_es(text):
	## initializations 
	t = text ; e_subs = 0
	
	## Është
	t, c = re.subn(r"(E|Ë)(sht)(e|ë)", r"Ë\2ë", t) ; e_subs += c
	## është
	t, c = re.subn(r"(e|ë)(sht)(e|ë)", r"ë\2ë", t) ; e_subs += c
	
	## unë Unë ujë Ujë
	t, c = re.subn(r"(u|U)(n|j)(e?)( |\.)", r"\1\2ë\4", t) ; e_subs += c
	
	## Mirë, mirë
	t, c = re.subn(r"(Mir|mir)(e?)( |\.)", r"\1ë\3", t) ; e_subs += c
	
	return (t, e_subs)
	
	