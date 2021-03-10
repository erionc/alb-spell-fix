
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

## function for c - ç substitutions
def replace_c(text):
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
	
## function for e -> ë substitutions
def replace_e(text):
	## initializations 
	t = text ; e_subs = 0
	
	## Është
	t, c = re.subn(r"(E|Ë)(sht)(e|ë)?( |\.)", r"Ë\2ë\4", t) ; e_subs += c
	## është
	t, c = re.subn(r"(e|ë)(sht)(e|ë)?( |\.)", r"ë\2ë\4", t) ; e_subs += c
			
	## fjalë që shkruhen pa ë në fund ose me ë të shkruar e - mir(e) -> mirë
	pa_e = "Buk|buk|Mir|mir|Pun|pun|Shum|shum|uj|Uj|Un|un"
	t, c = re.subn(fr"({pa_e})(e?)( |\.)", r"\1ë\3", t) ; e_subs += c
	# t, c = re.subn(r"(Mir|mir)(e?)( |\.)", r"\1ë\3", t) ; e_subs += c
	
	return (t, e_subs)

## function for replacing dialectic forms
def replace_dial(text):
	## initializations 
	t = text ; dial_subs = 0
	
	## fjalë që shnkruhen pa a në fund - du(e) -> dua, thu(e) -> thua
	dial = "Du|du|Thu|thu"
	t, c = re.subn(fr"({dial})(e?)( |\.)", r"\1a\3", t) ; dial_subs += c
	
	return (t, dial_subs)
	
## function for english words substitutions
def replace_eng(text):
	## initializations 
	t = text ; eng_subs = 0
	
	return (t, eng_subs)
	
## function for word substitutions
def replace_words(text):
	## initializations 
	t = text ; word_subs = 0
	
	return (t, word_subs)
	

	
	