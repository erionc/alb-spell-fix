
from percaktime import *

## temat që shkruhen me C/c në vend të Ç/ç-së nistore
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (c|ç)
## cafk, caj, cajnik, canak, cibuk, cift, cmim, co, corap, cudi, cun, cup 
nis_pa_c_me_prap = "afk|aj|ajnik|anak|akerdis|akmak|ale|alë|alo|alu|allm|apkën|apken|" + \
	"arcaf|arçaf|art|" + \
	"asje|asja|ati|" + \
    "elur|ekan|ekic|ekiç|elik|erek|" + \
    "iban|ibuk|iflig|ift|ikërrim|ikerrim|iment|imk|izme|" + \
    "mall|mend|merit|mim|min|mo|mont|morrit|muar|" + \
    "nder|njer|" + \
    "okollat|orap|organi|orodit|" + \
    "udi|un"

## temat që shkruhen me Ç/ç në vend të Q/q-së nistore
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (c|ç)
## çasje -> qasje
nis_me_q_jo_me_c = "orto|asj|uka\w"

## temat që shkruhen me C/c në vend të Ç/ç-së nistore
## nuk i jepet prapashtesë -- cel -> çel
nis_pa_c_pa_prap = "el|up(e|ë)|ik(e|ë)"

## temat që shkruhen me Ç/ç në vend të C/c-së nistore
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (c|ç)
## çertifikatë, çertifikoj, çertifikim
nis_me_c = "ertifik"

## fjalë ku shfaqen gabime me c-të, q-të dhe ç-të nistore
def pa_c_nistore(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

	## fjalë që shkruhen me C/c ose Q/q në vend të Ç/ç-së nistore dhe që marrin prapashtesë - caj -> çaj ; qizme -> çizme
	t, c = re.subn(fr"(\b)(c|q)({nis_pa_c_me_prap})({prapa_0_5})(\b)", r"ç\3\4", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(C|Q)({nis_pa_c_me_prap})({prapa_0_5})(\b)", r"Ç\3\4", t) ; c_subs += c

	## fjalë që shkruhen me C/c ose Q/q në vend të Ç/ç-së nistore por që nuk marrin prapashtesë - cel -> çel
	t, c = re.subn(fr"(\b)(c|q)({nis_pa_c_pa_prap})(\b)", r"ç\3", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(C|Q)({nis_pa_c_pa_prap})(\b)", r"Ç\3", t) ; c_subs += c

	t, c = re.subn(fr"(\b)(c|ç)({nis_me_q_jo_me_c})({prapa_0_5})(\b)", r"q\3\4", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(C|Ç)({nis_me_q_jo_me_c})({prapa_0_5})(\b)", r"Q\3\4", t) ; c_subs += c

	## fjalë që shkruen me Ç/ç ose Q/q në vend të C/c-së nistore - çertifikatë -> certifikatë
	t, c = re.subn(fr"(\b)(ç|q)({nis_me_c})({prapa_0_5})(\b)", r"c\3\4", t) ; c_subs += c
	t, c = re.subn(fr"(\b)(Ç|Q)({nis_me_c})({prapa_0_5})(\b)", r"C\3\4", t) ; c_subs += c

	return (t, e_subs, c_subs, tj_subs)


## fjalë ku shfaqen gabime me c-të, q-të dhe ç-të fundore 
fund_me_c = "Ky|ky"

## fjalë ku shfaqen gabime me c-të, q-të dhe ç-të nistore
def pa_c_fundore(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

	## fjalë që shkruhen me c ose q në vend të ç-së fundore - kyc -> kyç
	t, c = re.subn(fr"(\b)({fund_me_c})(c|q)({prapa_0_7})(\b)", r"\2ç\4", t) ; c_subs += c

	return (t, e_subs, c_subs, tj_subs)

## fjalë që mbarojnë me çi por shpesh shkruhen me ci
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (c|ç)
fund_me_ci = "All|all|Batak|batak|Inat|inat|Top|top|Zanat|zanat" 

## fjalë që përmbajnë ÇUES/ÇOJ por shpesh shkruhen me CUES/COJ - ndricues -> ndriçues ; ndricoj-> ndriçoj
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (c|ç)
permban_cues_coj_cim = "Lin|lin|" + \
	"Ndri|ndri|" + \
	"Për|për|Per|per|" + \
	"Tej|tej"

## fjalë që përmbajnë ÇEL por shpesh shkruhen me CEL - recel -> reçel
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (c|ç)
permban_cel = "Nder|Ndër|nder|ndër|" + \
	"Re|re"

## fjalë që shkruhen me Ç/ç në vend të C/c-së së brendshme
## përfshihen vetëm ato fjalë që përmbajnë vetëm 1 c e cila është e brendshme
def me_c_brenda(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

    ## (P|p)ro(ç|q)es -> (P|p)roces 
	t, c = re.subn(fr"(\b)(P|p)(roçes|roqes)({prapa_0_5})(\b)", r"\2roces\4", t) ; c_subs += c
    ##  (P|p)ro(ç|q)edur -> (P|p)rocedur
	t, c = re.subn(fr"(\b)(P|p)(roçedur|roqedur)({prapa_0_5})(\b)", r"\2rocedur\4", t) ; c_subs += c
    ##  (L|l)i(ç|q|sh)ens* -> (L|l)icens*
	t, c = re.subn(fr"(\b)(L|l)(içens|iqens|ishens)({prapa_0_5})(\b)", r"\2icens\4", t) ; c_subs += c

	return (t, e_subs, c_subs, tj_subs)

## fjalë që shkruhen me C/c në vend të Ç/ç-së së brendshme
## përfshihen vetëm ato fjalë që përmbajnë vetëm 1 c e cila është e brendshme
def pa_c_brenda(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

	## fjalë që mbarojnë me çi ; inatci -> inatçi ; zanatci -> zanatçi
	t, c = re.subn(fr"(\b)({fund_me_ci})(ci|qi)({prapa_0_5})(\b)", r"\2çi\4", t) ; c_subs += c

	## fjalë që përmbajnë ÇUES/ÇOJ por shpesh shkruhen me CUES/COJ - ndricues -> ndriçues ; ndricoj-> ndriçoj
	t, c = re.subn(fr"(\b)({permban_cues_coj_cim})(c|q)(u|o|i)({prapa_0_5})(\b)", r"\2ç\4\5", t) ; c_subs += c

	## fjalë që përmbajnë ÇEL por shpesh shkruhen me CEL - recel -> reçel
	t, c = re.subn(fr"(\b)({permban_cel})(cel|qel)({prapa_0_5})(\b)", r"\2çel\4", t) ; c_subs += c

	return (t, e_subs, c_subs, tj_subs)


## redaktime të rasteve c'|q' + folje, ç' + folje, dhe çfarë
def c_apostrof_folje(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0
	
	## ç'bën, ç'bëni
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(bën|ben)({prapa_0_5})(\b)", r"ç'bën\4", t) ; c_subs += c
	## Ç'bën, Ç'bëni
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(bën|ben)({prapa_0_5})(\b)", r"Ç'bën\4", t) ; c_subs += c

	## ç'do, ç'doni
	t, c = re.subn(fr"(\b)(c'|q')(do|doni)({prapa_0_5})(\b)", r"ç'\3\4", t) ; c_subs += c
	## Ç'do, Ç'do
	t, c = re.subn(fr"(\b)(C'|Q')(do|doni)({prapa_0_5})(\b)", r"Ç'\3\4", t) ; c_subs += c

	## çdo, çdokush, ...
	t, c = re.subn(fr"(\b)(c|q)(do)({prapa_0_5})(\b)", r"ç\3\4", t) ; c_subs += c
	## Çdo, Çdokush, ...
	t, c = re.subn(fr"(\b)(C|Q)(do)({prapa_0_5})(\b)", r"Ç\3\4", t) ; c_subs += c

	## ç'bëj, ç'bëjmë, ç'bëjnë
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(bëj|bej)({prapa_0_5})(\b)", r"ç'bëj\4", t) ; c_subs += c
	## Ç'bëj, Ç'bëjmë, Ç'bëjnë
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(bëj|bej)({prapa_0_5})(\b)", r"Ç'bëj\4", t) ; c_subs += c

	## ç'bëhet
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(bëh|beh)({prapa_0_5})(\b)", r"ç'bëh\4", t) ; c_subs += c
	## Ç'bëhet
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(bëh|beh)({prapa_0_5})(\b)", r"Ç'bëh\4", t) ; c_subs += c

	## ç'kemi, ç'ke, ç'keni
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(ke)({prapa_0_5})(\b)", r"ç'\3\4", t) ; c_subs += c
	## Ç'kemi, Ç'ke, Ç'keni 
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(ke)({prapa_0_5})(\b)", r"Ç'\3\4", t) ; c_subs += c
	
	## cka -> çka ; c'kam, ckam -> ç'kam ; c'ka(në) -> ç'ka(në) 
	t, c = re.subn(fr"(\b)(c|c'|ç|q|q')(ka)({prapa_0_5})(\b)", r"ç'\3\4", t) ; c_subs += c
	## Cka -> Çka ; C'kam, Ckam -> Ç'kam ; C'ka(në) -> Ç'ka(në) 
	t, c = re.subn(fr"(\b)(C|C'|Ç|Q|Q')(ka)({prapa_0_5})(\b)", r"Ç'\3\4", t) ; c_subs += c
	
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

	## fjalë që shkruhen me C/c ose Q/q në vend të Ç/ç-së nistore - cafkë -> çafkë
	t, e_c, c_c, tj_c = pa_c_nistore(t)
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c

	## fjalë që shkruhen me c ose q në vend të ç-së fundore - kyc -> kyç
	t, e_c, c_c, tj_c = pa_c_fundore(t)
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c

	## fjalë që shkruhen me C/c ose Q/q në vend të Ç/ç-së së brendshme - inatci -> inatçi
	t, e_c, c_c, tj_c = pa_c_brenda(t)
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c

	## fjalë që shkruhen me Ç/ç ose Q/q në vend të C/c-së së brendshme - proçes -> proces ; Proqedurë -> Procedurë 
	t, e_c, c_c, tj_c = me_c_brenda(t)
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c
	
	return (t, e_subs, c_subs, tj_subs)
	
	