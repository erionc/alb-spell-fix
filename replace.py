
import re

## 0-3 simbole shtesë në fund të fjalëve për të kapur prapashtesa 
## shquese dhe lakesat
suf = "[a-zA-Z0-9çÇëË_-]{0,3}"

## global variable that matches the ending of a word - (\b) is better
# we = " |\t|\n|\.|\?|:|;|,|!"

## fjalë gegërisht që mbarojnë me 'u(e)' por që duhet të 
## mbarojnë me 'ua' -- du(e) -> dua, thu(e) -> thua
fjale_geg1 = "du|Gru|gru|Mu|mu|thu"

## foljet ndihmëse kam/jam që paraprijnë pjesoret
kj = "kam |ke |ka |kemi |keni |kanë |jam |je |është |jemi |jeni |janë "

## pjesore të shkurtra gegërisht që mbarojnë me 'u', 'e', 'a' 
## por që duhet të mbarojnë me 'rë' -- pru -> prurë
pjes_geg1 = "pa|pi|pre|pru|vra|qa"

## pjesore të shkurtra gegërisht që mbarojnë me 'u' por që duhet të 
## mbarojnë me 'ar' -- shku -> shkuar
pjes_geg2 = "lexu|shkru|shku|dëgju|shiku|punu|k(e|ë)rku|m(e|ë)su"

## pjesore të shkurtra gegërisht që duhet të mbarojnë me 'ur' -- kap -> kapur
pjes_geg3 = "zbardh|ardh|zmbraps|zbraps|kap|hap"
	
## fjalë që shkruhen pa ë fundore ose me ë të shkruar e - mir(e) -> mirë
pa_e = "Buk|buk|Flak|flak|Jan|jan|Kan|kan|Mir|mir|Nj|nj|Pun|pun|Rrug|" + \
		"rrug|Shum|shum|Uj|uj|Un|un"
		
## temat që shkruhen me C/c në vend të Ç/ç-së nistore
## cafk*, caj, cajnik, cift*, coj, corap*, cudi, cun, 
pa_c_nis = "afk|aj|ajnik|ift|o|orap|udi|un"

## tema fjalësh që duhen shqipëruar
tem_sq = ""

## tema fjalësh angleze që duhen përkthyer
tem_en = "file"


## function for c - ç substitutions
def replace_c(text):
	## initializations 
	t = text ; c_subs = 0
	
	## ç'kemi, ç'ke, ç'keni, 
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(ke)({suf})(\b)", r"ç'\3\4", t) ; c_subs += c
	## Ç'kemi, Ç'ke, Ç'keni, 
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(ke)({suf})(\b)", r"Ç'\3\4", t) ; c_subs += c
	
	## cka -> çka ; c'kam, ckam -> ç'kam ; c'ka(në) -> ç'ka(në) 
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(ka)({suf})(\b)", r"ç'\3\4", t) ; c_subs += c
	## Cka -> Çka ; C'kam, Ckam -> Ç'kam ; C'ka(në) -> Ç'ka(në) 
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(ka)({suf})(\b)", r"Ç'\3\4", t) ; c_subs += c
	
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
	t, c = re.subn(fr"(\b)(c)({pa_c_nis})({suf})(\b)", r"ç\3\4", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(C)({pa_c_nis})({suf})(\b)", r"Ç\3\4", t) ; c_subs += c
	# t, c = re.subn(fr"(\b)(C)({pa_c_nis})(\b)", r"Ç\3", t) ; c_subs += c
	
	return (t, c_subs)
	
## function for e -> ë substitutions
def replace_e(text):
	## initializations 
	t = text ; e_subs = 0
	
	## Është
	t, c = re.subn(fr"(\b)(E|Ë)(sht)(e|ë)?(\b)", r"Ë\3ë", t) ; e_subs += c
	## është
	t, c = re.subn(fr"(\b)(e|ë)(sht)(e|ë)?(\b)", r"ë\3ë", t) ; e_subs += c
	
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
	
	## pjesoret që shkruhen pa ur në fund - kap -> kapur
	t, c = re.subn(fr"(\b)({kj})({pjes_geg3})(\b)", r"\2\3ur", t) ; dial_subs += c

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
	

	
	