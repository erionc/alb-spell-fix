
from percaktime import *


## shkruhen me -CIEN por duhen shkruar me KAN
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_icien = "Fizi|fizi|" + \
    "Informati|informati|" + \
    "Matemati|matemati|" + \
    "Statisti|statisti" 

## shkruhen me EN- por duhen shkruar pa të
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_er = "kapsul|kod|kript|"

## shkruhen me -ER por duhen shkruar me -UES
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_er = "Kod|kod|" + \
	"Program|program"

## shkruhen me HYPER- por duhen shkruar me HIPER-
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_hyper = "graf|" + \
	"kub|" + \
	"tekst"

## -ACION -> -IM
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_acion = "Emul|emul|" + \
	"Instal|instal|" + \
	"Komunik|komunik|Konfigur|konfigur|" + \
	"Modula|modul|" + \
	"Simula|simul|" + \
	"Telekomunik|telekomunik|Transform|transform"

## XH -> GJ
permban_gj = "Axhend|axhend|" + \
	"Dixhital|dixhital"
def permban_gj(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

	## dixhital -> digjital
	t, c = re.subn(fr"(\b)(Di|di)(xh)(ital)({prapa_gjat})(\b)", r"\2gj\4\5", t) ; tj_subs += c 

	## axhendë -> agjendë
	t, c = re.subn(fr"(\b)(A|a)(xh)(end)({prapa_gjat})(\b)", r"\2gj\4\5", t) ; tj_subs += c 

	return (t, e_subs, c_subs, tj_subs)
	

## funksion për shqipërime
def shqiperime(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

	## XH -> GJ
	t, e_c, c_c, tj_c = permban_gj(t)
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c

    ## HYPER -> HIPER ; hypertekst -> hipertekst
	t, c = re.subn(fr"(\b)(H|h)(yper)({nis_me_hyper})({prapa_gjat})(\b)", r"\2iper\4\5", t) ; tj_subs += c 

    ## -ER -> -UES ; programer -> programues
	t, c = re.subn(fr"(\b)({para_gjat})({fund_me_er})(er)({prapa_gjat})(\b)", r"\2\3ues\5", t) ; tj_subs += c 

    ## hiq EN- ; enkodoj -> kodoj
	t, c = re.subn(fr"(\b)(En|en)({nis_me_er})({prapa_gjat})(\b)", r"\3\4", t) ; tj_subs += c 

    ## -CION -> -IM ; telekomunikacion -> telekomunikim
	t, c = re.subn(fr"(\b)({fund_me_acion})(acion)({prapa_gjat})(\b)", r"\2im\4", t) ; tj_subs += c 

    ## -ICIEN -> -IKAN ; matematicien -> matematikan
	t, c = re.subn(fr"(\b)({fund_me_icien})(cien)({prapa_gjat})(\b)", r"\2kan\4", t) ; tj_subs += c 
	
	return (t, e_subs, c_subs, tj_subs)


## funksion për zëvendësimin e fjalëve angleze 
def perkthime(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0
	
	return (t, e_subs, c_subs, tj_subs)