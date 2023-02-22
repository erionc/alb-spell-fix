
from percaktime import *

## temat që shkruhen me C/c në vend të Ç/ç-së nistore
## ruhen prapashtesat ndaj nuk pranohen tema me grupe alternative me | si (c|ç)
## cafk, caj, cajnik, canak, cibuk, cift, cimk, cmim, co, corap, cudi, cun, cup 
nis_pa_c = "afk|aj|ajnik|anak|akerdis|akmak|ale|alë|alo|alu|allm|apkën|apken|arcaf|arçaf|art|ati|" + \
    "el|ekan|ekic|ekiç|elik|erek|" + \
    "ibuk|iflig|ift|ikërrim|ikerrim|iment|imk|izme|" + \
    "mend|merit|mim|min|mo|mont|morrit|" + \
    "nder|njer|" + \
    "o|okollat|orap|organi|orodit|" + \
    "u|udi|un"

## temat që shkruhen me Ç/ç në vend të C/c-së nistore
## ruhen prapashtesat ndaj nuk pranohen tema me grupe alternative me | si (c|ç)
## çertifikatë, çertifikoj, çertifikim
nis_me_c = "ertifik"

## fjalë që mbarojnë me çi por shpesh shkruhen me ci
## ruhen prapashtesat ndaj nuk pranohen tema me grupe alternative me | si (c|ç)
fund_me_ci = "All|all|Inat|inat|Top|top|Zanat|zanat" 


## fjalë që shkruhen me Ç/ç në vend të C/c-së së brendshme
## përfshihen vetëm ato fjalë që përmbajnë vetëm 1 c e cila është e brendshme
def me_c_brenda(text):
    ## vlerënisje
    t = text ; c_subs = 0

    ## (P|p)ro(ç|q)es -> (P|p)roces 
    t, c = re.subn(fr"(\b)(P|p)(roçes|roqes)({prapa})(\b)", r"\2roces\4", t) ; c_subs += c
    ##  (P|p)ro(ç|q)edur -> (P|p)rocedur
    t, c = re.subn(fr"(\b)(P|p)(roçedur|roqedur)({prapa})(\b)", r"\2rocedur\4", t) ; c_subs += c
    ##  (L|l)i(ç|q|sh)ens* -> (L|l)icens*
    t, c = re.subn(fr"(\b)(L|l)(içens|iqens|ishens)({prapa})(\b)", r"\2icens\4", t) ; c_subs += c

    return (t, c_subs)


## fjalë që shkruhen me C/c në vend të Ç/ç-së së brendshme
## përfshihen vetëm ato fjalë që përmbajnë vetëm 1 c e cila është e brendshme
def pa_c_brenda(text):
    ## vlerënisje
    t = text ; c_subs = 0

    ## fjalë që mbarojnë me çi ; inatci -> inatçi ; zanatci -> zanatçi
    t, c = re.subn(fr"(\b)({fund_me_ci})(ci|qi)({prapa})(\b)", r"\2çi\4", t) ; c_subs += c

    ## (R|r)e(c|q)el -> (R|r)eçel
    t, c = re.subn(fr"(\b)(R|r)(ecel|eqel)({prapa})(\b)", r"\2eçel\4", t) ; c_subs += c

    return (t, c_subs)


## funksion për zëvendësime c -> ç 
def redakto_c(text):
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
	t, c = re.subn(fr"(\b)(c|q)({nis_pa_c})({prapa})(\b)", r"ç\3\4", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(C|Q)({nis_pa_c})({prapa})(\b)", r"Ç\3\4", t) ; c_subs += c

	## fjalë që shkruen me Ç/ç ose Q/q në vend të C/c-së nistore - çertifikatë -> certifikatë
	t, c = re.subn(fr"(\b)(ç|q)({nis_me_c})({prapa})(\b)", r"c\3\4", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(Ç|Q)({nis_me_c})({prapa})(\b)", r"C\3\4", t) ; c_subs += c

	## fjalë që shkruhen me C/c ose Q/q në vend të Ç/ç-së së brendshme - recel -> reçel ; Reqel -> Reçel ; Allci -> Allçi
	t, c = pa_c_brenda(t) ; c_subs += c

	## fjalë që shkruhen me Ç/ç ose Q/q në vend të C/c-së së brendshme - proçes -> proces ; Proqedurë -> Procedurë 
	t, c = me_c_brenda(t) ; c_subs += c

	## për fjalën ekzakte çka lejon shpreje (e|ë) te paraqitja e saj
	# t, c = re.subn(fr"(\b)(C)({pa_c_nis})(\b)", r"Ç\3", t) ; c_subs += c
	
	return (t, c_subs)
	
	