
import re

## global variable that matches the ending of a word in regex
we = " |\t|\n|\.|\?|;|,|!"

## fjalë gegërisht që mbarojnë me 'u(e)' por që duhet të 
## mbarojnë me 'ua' -- du(e) -> dua, thu(e) -> thua
fjale_geg1 = "Du|du|Thu|thu|Gru|gru"
	
## pjesore të shkurtra gegërisht që mbarojnë me 'u' por që duhet 
## të mbarojnë me 'rë' -- pru -> prurë
pjes_geg1 = "Pru|pru|Vra|vra"

## pjesore të shkurtra gegërisht që mbarojnë me 'u' por që duhet të 
## mbarojnë me 'ar' -- shku -> shkuar
pjes_geg2 = "Lexu|lexu|Shkru|shkru|Shku|shku|Dëgju|dëgju|Shiku|shiku"

## function for c - ç substitutions
def replace_c(text):
	## initializations 
	t = text ; c_subs = 0
	
	## ç'kemi, ç'ke, ç'keni, 
	t, c = re.subn(fr"(c|c'|ç)(ke*)", r"ç'\2", t) ; c_subs += c
	## Ç'kemi, Ç'ke, Ç'keni, 
	t, c = re.subn(fr"(C|C'|Ç)(ke*)", r"Ç'\2", t) ; c_subs += c
	
	## cka -> çka, c'ka(në) -> ç'ka(në)
	t, c = re.subn(fr"(c)('?)(ka*)", r"ç\2\3", t) ; c_subs += c
	## Cka -> Çka, C'ka(në) -> Ç'ka(në)
	t, c = re.subn(fr"(C)('?)(ka*)", r"Ç\2\3", t) ; c_subs += c
	
	## çfarë 
	t, c = re.subn(fr"(c|ç)(far)(e?)({we})", r"çfarë\4", t) ; c_subs += c
	## Çfarë
	t, c = re.subn(fr"(C|Ç)(far)(e?)({we})", r"Çfarë\4", t) ; c_subs += c
	
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
	pa_e = "Buk|buk|Mir|mir|Nj|nj|Pun|pun|Shum|shum|uj|Uj|Un|un"
	t, c = re.subn(fr"({pa_e})(e?)({we})", r"\1ë\3", t) ; e_subs += c
	# t, c = re.subn(r"(Mir|mir)(e?)( |\.)", r"\1ë\3", t) ; e_subs += c
	
	return (t, e_subs)

## function for replacing dialectic forms
def replace_dial(text):
	## initializations 
	t = text ; dial_subs = 0
	
	## fjalë që shnkruhen pa a në fund - du(e) -> dua, thu(e) -> thua
	t, c = re.subn(fr"({fjale_geg1})(e?)({we})", r"\1a\3", t) ; dial_subs += c
	
	## pjesoret që shkruhen pa rë në fund - pru -> prurë
	t, c = re.subn(fr"({pjes_geg1})({we})", r"\1rë\2", t) ; dial_subs += c

	## pjesoret që shkruhen pa ar në fund - shku -> shkuar
	t, c = re.subn(fr"({pjes_geg2})({we})", r"\1ar\2", t) ; dial_subs += c
	
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
	

	
	