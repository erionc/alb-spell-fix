
import re

## global variable that specifies the ending of a word in regex
we = " |\t|\n|\.|\?|;|!"

## function for c - ç substitutions
def replace_c(text):
	## initializations 
	t = text ; c_subs = 0
	
	## ç'kemi
	t, c = re.subn(r"(c|c'|ç)(kemi)", r"ç'\2", t) ; c_subs += c
	## Ç'kemi 
	t, c = re.subn(r"(C|C'|Ç)(kemi)", r"Ç'\2", t) ; c_subs += c
	
	## çfarë 
	t, c = re.subn(r"(c|ç)(far)(e?)({we})", r"çfarë\4", t) ; c_subs += c
	## Çfarë
	t, c = re.subn(r"(C|Ç)(far)(e?)({we})", r"Çfarë\4", t) ; c_subs += c
	
	return (t, c_subs)
	
## function for e -> ë substitutions
def replace_e(text):
	## initializations 
	t = text ; e_subs = 0
	
	## Është
	t, c = re.subn(fr"(E|Ë)(sht)(e|ë)?({we})", r"Ë\2ë\4", t) ; e_subs += c
	## është
	t, c = re.subn(fr"(e|ë)(sht)(e|ë)?({we})", r"ë\2ë\4", t) ; e_subs += c
			
	## fjalë që shkruhen pa ë në fund ose me ë të shkruar e - mir(e) -> mirë
	pa_e = "Buk|buk|Mir|mir|Pun|pun|Shum|shum|uj|Uj|Un|un"
	t, c = re.subn(fr"({pa_e})(e?)({we})", r"\1ë\3", t) ; e_subs += c
	# t, c = re.subn(r"(Mir|mir)(e?)( |\.)", r"\1ë\3", t) ; e_subs += c
	
	return (t, e_subs)

## function for replacing dialectic forms
def replace_dial(text):
	## initializations 
	t = text ; dial_subs = 0
	
	## fjalë që shnkruhen pa a në fund - du(e) -> dua, thu(e) -> thua
	dial1 = "Du|du|Thu|thu|Gru|gru"
	t, c = re.subn(fr"({dial1})(e?)({we})", r"\1a\3", t) ; dial_subs += c
	
	## fjalë që shkruhen pa rë në fund - pru -> prurë
	dial2 = "Pru|pru|Vra|vra"
	t, c = re.subn(fr"({dial2})({we})", r"\1rë\2", t) ; dial_subs += c

	## fjalë që shkruhen pa ar në fund - shku -> shkuar
	dial3 = "Lexu|lexu|Shkru|shkru|Shku|shku"
	t, c = re.subn(fr"({dial3})({we})", r"\1ar\2", t) ; dial_subs += c
	
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
	

	
	