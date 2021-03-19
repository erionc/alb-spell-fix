
import re

## global variable that matches the ending of a word - (\b) is better
# we = " |\t|\n|\.|\?|:|;|,|!"

## fjalë gegërisht që mbarojnë me 'u(e)' por që duhet të 
## mbarojnë me 'ua' -- du(e) -> dua, thu(e) -> thua
fjale_geg1 = "du|thu|Gru|gru"

## foljet ndihmëse kam/jam që paraprijnë pjesoret
kj = "kam |ke |ka |kemi |keni |kanë |jam |je |është |jemi |jeni |janë "

## pjesore të shkurtra gegërisht që mbarojnë me 'u', 'e', 'a' 
## por që duhet të mbarojnë me 'rë' -- pru -> prurë
pjes_geg1 = "pa|pi|pre|pru|vra"

## pjesore të shkurtra gegërisht që mbarojnë me 'u' por që duhet të 
## mbarojnë me 'ar' -- shku -> shkuar
pjes_geg2 = "lexu|shkru|shku|dëgju|shiku"
	
## fjalë që shkruhen pa ë fundore ose me ë të shkruar e - mir(e) -> mirë
pa_e = "Buk|buk|Flak|flak|Mir|mir|Nj|nj|Pun|pun|Rrug|rrug|Shum|shum|" + \
		"Uj|uj|Un|un"
		
## fjalë që shkruhen me C/c në vend të Ç/ç-së nistore
## cafkë, caj, cajnik, cifte, coj, corape, cun, 
pa_c_nis = "afkë|aj|ajnik|ifte|oj|orape|un"

## function for c - ç substitutions
def replace_c(text):
	## initializations 
	t = text ; c_subs = 0
	
	## ç'kemi, ç'ke, ç'keni, - no ending (\b)
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(ke*)", r"ç'\3", t) ; c_subs += c
	# t, c = re.subn(fr"(\b)(c|ç|q)('?)(ke*)", r"ç\3\4", t) ; c_subs += c
	## Ç'kemi, Ç'ke, Ç'keni, - no ending (\b)
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(ke*)", r"Ç'\3", t) ; c_subs += c
	# t, c = re.subn(fr"(\b)(C|Ç|Q)('?)(ke*)", r"Ç\3\4", t) ; c_subs += c
	
	## cka -> çka ; c'kam, ckam -> ç'kam ; c'ka(në) -> ç'ka(në) - no ending (\b)
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(ka*)", r"ç'\3", t) ; c_subs += c
	# t, c = re.subn(fr"(\b)(c|q|ç)('?)(ka*)", r"ç\3\4", t) ; c_subs += c
	## Cka -> Çka ; C'kam, Ckam -> Ç'kam ; C'ka(në) -> Ç'ka(në) - no ending (\b)
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(ka*)", r"Ç'\3", t) ; c_subs += c
	# t, c = re.subn(fr"(\b)(C|Q|Ç)('?)(ka*)", r"Ç\3\4", t) ; c_subs += c
	
	## çfarë 
	t, c = re.subn(fr"(\b)(c|ç|q)(far)(e?)(\b)", r"çfarë", t) ; c_subs += c
	## Çfarë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(far)(e?)(\b)", r"Çfarë", t) ; c_subs += c
	
	## çupë
	t, c = re.subn(fr"(\b)(c|ç|q)(up)(e?)(\b)", r"çupë", t) ; c_subs += c
	## Çupë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(up)(e?)(\b)", r"Çupë", t) ; c_subs += c
	
	## çikë
	t, c = re.subn(fr"(\b)(c|ç|q)(ik)(e?)(\b)", r"çikë", t) ; c_subs += c
	## Çikë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(ik)(e?)(\b)", r"Çikë", t) ; c_subs += c
	
	## fjalë që shkruhen me C/c në vend të Ç/ç-së nistore - caj -> çaj
	t, c = re.subn(fr"(\b)(c)({pa_c_nis})(\b)", r"ç\3", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(C)({pa_c_nis})(\b)", r"Ç\3", t) ; c_subs += c
	
	return (t, c_subs)
	
## function for e -> ë substitutions
def replace_e(text):
	## initializations 
	t = text ; e_subs = 0
	
	## Është
	t, c = re.subn(fr"(\b)(E|Ë)(sht)(e|ë)?(\b)", r"Ë\3ë", t) ; e_subs += c
	## është
	t, c = re.subn(fr"(\b)(e|ë)(sht)(e|ë)?(\b)", r"ë\3ë", t) ; e_subs += c
			
	## kan(e) -> kanë
	t, c = re.subn(fr"(\b)(K|k)(an)(e?)(\b)", r"\2\3ë", t) ; e_subs += c
	## jan(e) -> janë
	t, c = re.subn(fr"(\b)(J|j)(an)(e?)(\b)", r"\2\3ë", t) ; e_subs += c
	
	## fjalë që shkruhen pa ë fundore ose me ë të shkruar e - mir(e) -> mirë
	t, c = re.subn(fr"(\b)({pa_e})(e?)(\b)", r"\2ë", t) ; e_subs += c
	# t, c = re.subn(r"(Mir|mir)(e?)( |\.)", r"\1ë\3", t) ; e_subs += c
	
	return (t, e_subs)

## function for replacing dialectic forms
def replace_dial(text):
	## initializations 
	t = text ; dial_subs = 0
	
	## fjalë që shnkruhen pa a në fund - du(e) -> dua, thu(e) -> thua
	t, c = re.subn(fr"(\b)({fjale_geg1})(e?)(\b)", r"\2a", t) ; dial_subs += c
	
	## pjesoret që shkruhen pa rë në fund - pru -> prurë
	t, c = re.subn(fr"(\b)({kj})({pjes_geg1})(\b)", r"\2\3rë", t) ; dial_subs += c

	## pjesoret që shkruhen pa ar në fund - shku -> shkuar
	t, c = re.subn(fr"(\b)({kj})({pjes_geg2})(\b)", r"\2\3ar", t) ; dial_subs += c
	
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
	

	
	