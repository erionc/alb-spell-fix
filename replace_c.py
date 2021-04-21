
import re, string

## temat që shkruhen me C/c në vend të Ç/ç-së nistore
## ruhen prapashtesat ndaj nuk pranohen tema me grupe alternative me |
## cafk, caj, cajnik, cibuk, cift, cimk, cmim, co, corap, cudi, cun, cmendur 
pa_c_nis = "afk|aj|ajnik|akmak|arcaf|arçaf|ibuk|ift|imk|izme|mim|" + \
"o|orap|udi|un|mendur"

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
	t, c = re.subn(fr"(\b)(c|ç|q)(far)(e|ë)?(\b)", r"çfarë", t) ; c_subs += c
	## Çfarë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(far)(e|ë)?(\b)", r"Çfarë", t) ; c_subs += c
	
	## çupë
	t, c = re.subn(fr"(\b)(c|ç|q)(up)(e|ë)?(\b)", r"çupë", t) ; c_subs += c
	## Çupë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(up)(e|ë)?(\b)", r"Çupë", t) ; c_subs += c
	
	## çikë
	t, c = re.subn(fr"(\b)(c|ç|q)(ik)(e|ë)?(\b)", r"çikë", t) ; c_subs += c
	## Çikë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(ik)(e|ë)?(\b)", r"Çikë", t) ; c_subs += c
	
	## fjalë që shkruhen me C/c në vend të Ç/ç-së nistore - caj -> çaj
	t, c = re.subn(fr"(\b)(c)({pa_c_nis})({suf})(\b)", r"ç\3\4", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(C)({pa_c_nis})({suf})(\b)", r"Ç\3\4", t) ; c_subs += c
	# t, c = re.subn(fr"(\b)(C)({pa_c_nis})(\b)", r"Ç\3", t) ; c_subs += c
	
	return (t, c_subs)
	
	