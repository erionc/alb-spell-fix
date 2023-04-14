
import re, string

## 0-5 simbole shtesë në fund të fjalëve për prapa_gjatshtesat dhe lakesat
prapa_gjat = "[a-zA-Z0-9çÇëË_-]{0,5}"

## 0-2 simbole shtesë në fund të fjalëve për mbaresa të shkurtra
prapa_shkurt = "[a-zA-Z0-9çÇëË_-]{0,2}"

## temat që shkruhen me C/c në vend të Ç/ç-së nistore
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (c|ç)
## cafk, caj, cajnik, canak, cibuk, cift, cmim, co, corap, cudi, cun, cup 
nis_pa_c_me_prap = "afk|aj|ajnik|anak|akerdis|akmak|ale|alë|alo|alu|allm|apkën|apken|arcaf|arçaf|art|ati|" + \
    "elur|ekan|ekic|ekiç|elik|erek|" + \
    "iban|ibuk|iflig|ift|ikërrim|ikerrim|iment|imk|izme|" + \
    "mall|mend|merit|mim|min|mo|mont|morrit|muar|" + \
    "nder|njer|" + \
    "okollat|orap|organi|orodit|" + \
    "udi|un"

## temat që shkruhen me C/c në vend të Ç/ç-së nistore
## nuk i jepet prapa_gjatshtesë -- cel -> çel
nis_pa_c_pa_prap = "el|up(e|ë)|ik(e|ë)"

## temat që shkruhen me Ç/ç në vend të C/c-së nistore
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (c|ç)
## çertifikatë, çertifikoj, çertifikim
nis_me_c = "ertifik"

## fjalë që mbarojnë me çi por shpesh shkruhen me ci
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (c|ç)
fund_me_ci = "All|all|Batak|batak|Inat|inat|Top|top|Zanat|zanat" 


## fjalë që shkruhen me Ç/ç në vend të C/c-së së brendshme
## përfshihen vetëm ato fjalë që përmbajnë vetëm 1 c e cila është e brendshme
def me_c_brenda(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

    ## (P|p)ro(ç|q)es -> (P|p)roces 
	t, c = re.subn(fr"(\b)(P|p)(roçes|roqes)({prapa_gjat})(\b)", r"\2roces\4", t) ; c_subs += c
    ##  (P|p)ro(ç|q)edur -> (P|p)rocedur
	t, c = re.subn(fr"(\b)(P|p)(roçedur|roqedur)({prapa_gjat})(\b)", r"\2rocedur\4", t) ; c_subs += c
    ##  (L|l)i(ç|q|sh)ens* -> (L|l)icens*
	t, c = re.subn(fr"(\b)(L|l)(içens|iqens|ishens)({prapa_gjat})(\b)", r"\2icens\4", t) ; c_subs += c

	return (t, e_subs, c_subs, tj_subs)


## fjalë që shkruhen me C/c në vend të Ç/ç-së së brendshme
## përfshihen vetëm ato fjalë që përmbajnë vetëm 1 c e cila është e brendshme
def pa_c_brenda(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

	## fjalë që mbarojnë me çi ; inatci -> inatçi ; zanatci -> zanatçi
	t, c = re.subn(fr"(\b)({fund_me_ci})(ci|qi)({prapa_gjat})(\b)", r"\2çi\4", t) ; c_subs += c

	## (R|r)e(c|q)el -> (R|r)eçel
	t, c = re.subn(fr"(\b)(R|r)(ecel|eqel)({prapa_gjat})(\b)", r"\2eçel\4", t) ; c_subs += c

	## ndricim -> ndriçim ; ndriques -> ndriçues ; ndricimtar -> ndriçimtar
	t, c = re.subn(fr"(\b)(N|n)(dric|driq)({prapa_gjat})(\b)", r"\2driç\4", t) ; c_subs += c

	## lincim -> linçim ; linqoj -> linçoj
	t, c = re.subn(fr"(\b)(L|l)(inc|inq)({prapa_gjat})(\b)", r"\2inç\4", t) ; c_subs += c

	return (t, e_subs, c_subs, tj_subs)


## redaktime të rasteve c'|q' + folje, ç' + folje, dhe çfarë
def c_apostrof_folje(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0
	
	## ç'bën, ç'bëni
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(bën|ben)({prapa_gjat})(\b)", r"ç'bën\4", t) ; c_subs += c
	## Ç'bën, Ç'bëni
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(bën|ben)({prapa_gjat})(\b)", r"Ç'bën\4", t) ; c_subs += c

	## ç'bëj, ç'bëjmë, ç'bëjnë
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(bëj|bej)({prapa_gjat})(\b)", r"ç'bëj\4", t) ; c_subs += c
	## Ç'bëj, Ç'bëjmë, Ç'bëjnë
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(bëj|bej)({prapa_gjat})(\b)", r"Ç'bëj\4", t) ; c_subs += c

	## ç'bëhet
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(bëh|beh)({prapa_gjat})(\b)", r"ç'bëh\4", t) ; c_subs += c
	## Ç'bëhet
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(bëh|beh)({prapa_gjat})(\b)", r"Ç'bëh\4", t) ; c_subs += c

	## ç'kemi, ç'ke, ç'keni
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(ke)({prapa_gjat})(\b)", r"ç'\3\4", t) ; c_subs += c
	## Ç'kemi, Ç'ke, Ç'keni 
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(ke)({prapa_gjat})(\b)", r"Ç'\3\4", t) ; c_subs += c
	
	## cka -> çka ; c'kam, ckam -> ç'kam ; c'ka(në) -> ç'ka(në) 
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(ka)({prapa_gjat})(\b)", r"ç'\3\4", t) ; c_subs += c
	## Cka -> Çka ; C'kam, Ckam -> Ç'kam ; C'ka(në) -> Ç'ka(në) 
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(ka)({prapa_gjat})(\b)", r"Ç'\3\4", t) ; c_subs += c
	
	## çfarë
	t, c = re.subn(fr"(\b)(c|ç|q)(far)(e|ë)?(\b)", r"çfarë", t) ; c_subs += c
	## Çfarë
	t, c = re.subn(fr"(\b)(C|Ç|Q)(far)(e|ë)?(\b)", r"Çfarë", t) ; c_subs += c

	return (t, e_subs, c_subs, tj_subs)


## funksion për zëvendësime c -> ç 
def redakto_c(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0
	
	## redaktime të rasteve c'|q' + folje, ç' + folje, dhe çfarë
	t, e_c, c_c, tj_c = c_apostrof_folje(t)
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c

	## fjalë që shkruhen me C/c ose Q/q në vend të Ç/ç-së nistore dhe që marrin prapashtesë - caj -> çaj ; qizme -> çizme
	t, c = re.subn(fr"(\b)(c|q)({nis_pa_c_me_prap})({prapa_gjat})(\b)", r"ç\3\4", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(C|Q)({nis_pa_c_me_prap})({prapa_gjat})(\b)", r"Ç\3\4", t) ; c_subs += c

	## fjalë që shkruhen me C/c ose Q/q në vend të Ç/ç-së nistore por që nuk marrin prapashtesë - cel -> çel
	t, c = re.subn(fr"(\b)(c|q)({nis_pa_c_pa_prap})(\b)", r"ç\3", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(C|Q)({nis_pa_c_pa_prap})(\b)", r"Ç\3", t) ; c_subs += c

	## fjalë që shkruen me Ç/ç ose Q/q në vend të C/c-së nistore - çertifikatë -> certifikatë
	t, c = re.subn(fr"(\b)(ç|q)({nis_me_c})({prapa_gjat})(\b)", r"c\3\4", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(Ç|Q)({nis_me_c})({prapa_gjat})(\b)", r"C\3\4", t) ; c_subs += c

	## fjalë që shkruhen me C/c ose Q/q në vend të Ç/ç-së së brendshme - recel -> reçel ; Reqel -> Reçel ; Allci -> Allçi
	t, e_c, c_c, tj_c = pa_c_brenda(t)
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c

	## fjalë që shkruhen me Ç/ç ose Q/q në vend të C/c-së së brendshme - proçes -> proces ; Proqedurë -> Procedurë 
	t, e_c, c_c, tj_c = me_c_brenda(t)
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c
	
	return (t, e_subs, c_subs, tj_subs)
	
	