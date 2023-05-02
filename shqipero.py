
from percaktime import *

## shkruhen me -CIEN por duhen shkruar me KAN
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_icien = "Fizi|fizi|" + \
	"Gramati|gramati|" + \
    "Informati|informati|" + \
    "Matemati|matemati|" + \
    "Statisti|statisti" 

## shkruhen me EN- por duhen shkruar pa të
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_en = "kapsul|kod|kript"

## shkruhen me -ER por duhen shkruar me -UES
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_er = "Kod|kod|" + \
	"Program|program"

## shkruhen me HYPER- por duhen shkruar me HIPER-
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_hyper = "graf|" + \
	"kub|" + \
	"lidhje|link|" + \
	"tekst|text"

## -ACION -> -IM
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_acion = "Emul|emul|" + \
	"Instal|instal|" + \
	"Kombin|kombin|Komunik|komunik|Konfigur|konfigur|" + \
	"Modula|modul|" + \
	"Simul|simul|" + \
	"Telekomunik|telekomunik|Transform|transform"

## XH -> GJ
permban_gj = "Axhend|axhend|" + \
	"Dixhital|dixhital"

def permban_gj(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0

	## dixhital -> digjital
	t, c = re.subn(fr"(\b)(Di|di)(xh)(ital)({albprapa_0_5})(\b)", r"\2gj\4\5", t) ; tj_subs += c 

	## axhendë -> agjendë
	t, c = re.subn(fr"(\b)(A|a)(xh)(end)({albprapa_0_5})(\b)", r"\2gj\4\5", t) ; tj_subs += c 

	return (t, e_subs, c_subs, pj_subs, tj_subs)
	

## funksion për shqipërime
def shqiperime(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0

	## kthimi i pikës në presje dhjetore 0.345 -> 0,345 ; 3.6e6 -> 3,6e6 ; -34.4e-4 -> -34,4e-4
	t, c = re.subn(fr"(\b)([-+]?)([0-9]*)(\.)([0-9]+)([eE][-+]?[0-9]+)?(\b)", r"\2\3,\5\6", t) ; 
	## shprehja e mëposhtëme zëvendëson edhe numrat e shkruar në formën .345 -> ,345
	# t, c = re.subn(fr"([-+]?)([0-9]*)(\.)([0-9]+)([eE][-+]?[0-9]+)?(\b)", r"\1\2,\4\5", t)
	tj_subs += c 

	## XH -> GJ
	t, e_c, c_c, p_c, tj_c = permban_gj(t)
	c_subs += c_c ; e_subs += e_c ; pj_subs =+ p_c ; tj_subs += tj_c

    ## HYPER -> HIPER ; hypertekst -> hipertekst
	t, c = re.subn(fr"(\b)(H|h)(yper)({nis_me_hyper})({albprapa_0_5})(\b)", r"\2iper\4\5", t) ; tj_subs += c 

    ## -ER -> -UES ; programer -> programues
	t, c = re.subn(fr"(\b)({albpara_0_5})({fund_me_er})(er)({albprapa_0_5})(\b)", r"\2\3ues\5", t) ; tj_subs += c 

    ## hiq EN- ; enkodoj -> kodoj
	t, c = re.subn(fr"(\b)(En|en)({nis_me_en})({albprapa_0_5})(\b)", r"\3\4", t) ; tj_subs += c 

    ## -CION -> -IM ; telekomunikacion -> telekomunikim
	t, c = re.subn(fr"(\b)({fund_me_acion})(acion)({albprapa_0_5})(\b)", r"\2im\4", t) ; tj_subs += c 

    ## -ICIEN -> -IKAN ; matematicien -> matematikan
	t, c = re.subn(fr"(\b)({fund_me_icien})(cien)({albprapa_0_5})(\b)", r"\2kan\4", t) ; tj_subs += c 
	
	return (t, e_subs, c_subs, pj_subs, tj_subs)


## funksion për zëvendësimin e fjalëve angleze 
def perkthime(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0

	## link -> lidhje ; Hyperlink -> Hiperlidhje
	t, c = re.subn(fr"(\b)({albpara_0_5})(L|l)(ink)(\b)", r"\2\3idhje", t) ; tj_subs += c 
	t, c = re.subn(fr"(\b)({albpara_0_5})(L|l)(inku)(\b)", r"\2\3idhja", t) ; tj_subs += c 
	t, c = re.subn(fr"(\b)({albpara_0_5})(L|l)(ink|inq)(e|et)(\b)", r"\2\3idhj\5", t) ; tj_subs += c 

	## text -> tekst ; Hypertext -> Hipertekst
	t, c = re.subn(fr"(\b)({albpara_0_5})(T|t)(ext)(\b)", r"\2\3ekst", t) ; tj_subs += c 
	t, c = re.subn(fr"(\b)({albpara_0_5})(T|t)(exti)(\b)", r"\2\3eksti", t) ; tj_subs += c 
	t, c = re.subn(fr"(\b)({albpara_0_5})(T|t)(exte|extet)(\b)", r"\2\3ekste\5", t) ; tj_subs += c 

	return (t, e_subs, c_subs, pj_subs, tj_subs)