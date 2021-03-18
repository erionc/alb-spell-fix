
import re

## global variable that matches the ending of a word
we = " |\t|\n|\.|\?|:|;|,|!"

## fjalë gegërisht që mbarojnë me 'u(e)' por që duhet të 
## mbarojnë me 'ua' -- du(e) -> dua, thu(e) -> thua
fjale_geg1 = "Du|du|Thu|thu|Gru|gru"
	
## pjesore të shkurtra gegërisht që mbarojnë me 'u', 'e', 'a' 
## por që duhet të mbarojnë me 'rë' -- pru -> prurë
pjes_geg1 = "Pi|pi|Pre|pre|Pru|pru|Vra|vra"

## pjesore të shkurtra gegërisht që mbarojnë me 'u' por që duhet të 
## mbarojnë me 'ar' -- shku -> shkuar
pjes_geg2 = "Lexu|lexu|Shkru|shkru|Shku|shku|Dëgju|dëgju|Shiku|shiku"
	
## fjalë që shkruhen pa ë fundore ose me ë të shkruar e - mir(e) -> mirë
pa_e = "Buk|buk|Flak|flak|Mir|mir|Nj|nj|Pun|pun|Rrug|rrug|Shum|shum|" + \
		"Uj|uj|Un|un"
		
## fjalë që shkruhen me C/c në vend të Ç/ç-së nistore
## caj, cajnik, cifte, coj, corape, cun, 
pa_c_nis = "aj|ajnik|ifte|oj|orape|un"

## function for c - ç substitutions
def replace_c(text):
	## initializations 
	t = text ; c_subs = 0
	
	## ç'kemi, ç'ke, ç'keni, - no {we}
	t, c = re.subn(fr"(\b)(c|c'|ç|q)(ke*)", r"ç'\3", t) ; c_subs += c
	## Ç'kemi, Ç'ke, Ç'keni, - no {we}
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q)(ke*)", r"Ç'\3", t) ; c_subs += c
	
	## cka -> çka ; c'kam, ckam -> ç'kam ; c'ka(në) -> ç'ka(në) - no {we}
	t, c = re.subn(fr"(\b)(c|q)('?)(ka*)", r"ç\3\4", t) ; c_subs += c
	## Cka -> Çka ; C'kam, Ckam -> Ç'kam ; C'ka(në) -> Ç'ka(në) - no {we}
	t, c = re.subn(fr"(\b)(C|Q)('?)(ka*)", r"Ç\3\4", t) ; c_subs += c
	
	## çfarë 
	t, c = re.subn(fr"(\b)(c|ç|q)(far)(e?)({we})", r"çfarë\5", t) ; c_subs += c
	## Çfarë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(far)(e?)({we})", r"Çfarë\5", t) ; c_subs += c
	
	## çupë
	t, c = re.subn(fr"(\b)(c|ç|q)(up)(e?)({we})", r"çupë\5", t) ; c_subs += c
	## Çupë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(up)(e?)({we})", r"Çupë\5", t) ; c_subs += c
	
	## çikë
	t, c = re.subn(fr"(\b)(c|ç|q)(ik)(e?)({we})", r"çikë\5", t) ; c_subs += c
	## Çikë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(ik)(e?)({we})", r"Çikë\5", t) ; c_subs += c
	
	## fjalë që shkruhen me C/c në vend të Ç/ç-së nistore - caj -> çaj
	t, c = re.subn(fr"(\b)(c)({pa_c_nis})({we})", r"ç\3\4", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(C)({pa_c_nis})({we})", r"Ç\3\4", t) ; c_subs += c
	
	return (t, c_subs)
	
## function for e -> ë substitutions
def replace_e(text):
	## initializations 
	t = text ; e_subs = 0
	
	## Është
	t, c = re.subn(fr"(E|Ë)(sht)(e|ë)?({we})", r"Ë\2ë\4", t) ; e_subs += c
	## është
	t, c = re.subn(fr"(e|ë)(sht)(e|ë)?({we})", r"ë\2ë\4", t) ; e_subs += c
			
	## fjalë që shkruhen pa ë fundore ose me ë të shkruar e - mir(e) -> mirë
	t, c = re.subn(fr"(\b)({pa_e})(e?)({we})", r"\2ë\4", t) ; e_subs += c
	# t, c = re.subn(r"(Mir|mir)(e?)( |\.)", r"\1ë\3", t) ; e_subs += c
	
	return (t, e_subs)

## function for replacing dialectic forms
def replace_dial(text):
	## initializations 
	t = text ; dial_subs = 0
	
	## fjalë që shnkruhen pa a në fund - du(e) -> dua, thu(e) -> thua
	t, c = re.subn(fr"(\b)({fjale_geg1})(e?)({we})", r"\2a\4", t) ; dial_subs += c
	
	## pjesoret që shkruhen pa rë në fund - pru -> prurë
	t, c = re.subn(fr"(\b)({pjes_geg1})({we})", r"\2rë\3", t) ; dial_subs += c

	## pjesoret që shkruhen pa ar në fund - shku -> shkuar
	t, c = re.subn(fr"(\b)({pjes_geg2})({we})", r"\2ar\3", t) ; dial_subs += c
	
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
	

	
	