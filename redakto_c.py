
from nistore_c import *

## funksion për zëvendësime c -> ç 
def korrigjo_c(text):
	## vlerënisje
	t = text ; c_subs = 0
	
	## ç'kemi, ç'ke, ç'keni, 
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(ke)({prapa})(\b)", r"ç'\3\4", t) ; c_subs += c
	## Ç'kemi, Ç'ke, Ç'keni, 
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(ke)({prapa})(\b)", r"Ç'\3\4", t) ; c_subs += c
	
	## cka -> çka ; c'kam, ckam -> ç'kam ; c'ka(në) -> ç'ka(në) 
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(ka)({prapa})(\b)", r"ç'\3\4", t) ; c_subs += c
	## Cka -> Çka ; C'kam, Ckam -> Ç'kam ; C'ka(në) -> Ç'ka(në) 
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(ka)({prapa})(\b)", r"Ç'\3\4", t) ; c_subs += c
	
	## çfarë 
	t, c = re.subn(fr"(\b)(c|ç|q)(far)(e|ë)?(\b)", r"çfarë", t) ; c_subs += c
	## Çfarë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(far)(e|ë)?(\b)", r"Çfarë", t) ; c_subs += c
	
	# ## çupë
	t, c = re.subn(fr"(\b)(c|ç|q)(up)(e|ë)?(\b)", r"çupë", t) ; c_subs += c
	# ## Çupë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(up)(e|ë)?(\b)", r"Çupë", t) ; c_subs += c
	
	## çikë
	t, c = re.subn(fr"(\b)(c|ç|q)(ik)(e|ë)?(\b)", r"çikë", t) ; c_subs += c
	## Çikë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(ik)(e|ë)?(\b)", r"Çikë", t) ; c_subs += c
	
	## fjalë që shkruhen me C/c ose Q/q në vend të Ç/ç-së nistore - caj -> çaj ; qizme -> çizme
	t, c = re.subn(fr"(\b)(c|q)({pa_c_nis})({prapa})(\b)", r"ç\3\4", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(C|Q)({pa_c_nis})({prapa})(\b)", r"Ç\3\4", t) ; c_subs += c

	## fjal;; q;; shkruen me Ç/ç ose Q/q n;; vend t;; C/c-s;; nistore - çertifikatë -> certifikatë
	t, c = re.subn(fr"(\b)(ç|q)({me_c_nis})({prapa})(\b)", r"c\3\4", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(Ç|Q)({me_c_nis})({prapa})(\b)", r"C\3\4", t) ; c_subs += c

	## për fjalën ekzakte çka lejon shpreje (e|ë) te paraqitja e saj
	# t, c = re.subn(fr"(\b)(C)({pa_c_nis})(\b)", r"Ç\3", t) ; c_subs += c
	
	return (t, c_subs)
	
	