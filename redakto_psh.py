
''' Redaktime të parashtesave dhe prapashtesave '''

from percaktime import *

## shkruhen me EN- por duhen shkruar pa të
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_en = "kapsul|kod|kript"

## shkruhen me HYPER- por duhen shkruar me HIPER-
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_hyper = "graf|" + \
	"kub|" + \
	"lidhje|link|" + \
	"tekst|text"

## shkruhen me -ER por duhen shkruar me -UES
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_er = "Kod|kod|" + \
	"Program|program"

## -ACION -> -IM
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_acion_im = "Emul|emul|" + \
	"Instal|instal|" + \
	"Kombin|kombin|Komunik|komunik|Konfigur|konfigur|" + \
	"Modula|modul|" + \
	"Simul|simul|" + \
	"Telekomunik|telekomunik|Transform|transform"

## shkruhen me -AL por duhen shkruar me -OR
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_al_or = "Natyr|natyr|Spektr|spektr"

## shkruhen me -AL por duhen shkruar me -IK
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_al_ik = "Binomi|binomi|Polinomi|polinomi|Term|term"

## shkruhen me -TIVE por duhen shkruar me -UES
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_tiv_ues = "Komunik|komunik"

## shkruhen me -CIEN por duhen shkruar me KAN
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_icien = "Fizi|fizi|" + \
	"Gramati|gramati|" + \
    "Informati|informati|" + \
    "Matemati|matemati|" + \
    "Statisti|statisti" 

## funksion për redaktimin e parashtesave dhe prapashtesave
def paraprapashtesa(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0

    ## HYPER -> HIPER ; hypertekst -> hipertekst
	t, c = re.subn(fr"(\b)(H|h)(yper)({nis_me_hyper})({albprapa_0_5})(\b)", r"\2iper\4\5", t) ; tj_subs += c 

    ## -ER -> -UES ; programer -> programues
	t, c = re.subn(fr"(\b)({albpara_0_5})({fund_me_er})(er)({albprapa_0_5})(\b)", r"\2\3ues\5", t) ; tj_subs += c 

    ## hiq EN- ; enkodoj -> kodoj
	t, c = re.subn(fr"(\b)(En|en)({nis_me_en})({albprapa_0_5})(\b)", r"\3\4", t) ; tj_subs += c 

    ## -ACION -> -IM ; telekomunikacion -> telekomunikim
	t, c = re.subn(fr"(\b)({fund_me_acion_im})(acion)({albprapa_0_5})(\b)", r"\2im\4", t) ; tj_subs += c 

    ## -AL -> -OR ; natyral -> natyror
	t, c = re.subn(fr"(\b)({fund_me_al_or})(al)({albprapa_0_5})(\b)", r"\2or\4", t) ; tj_subs += c 

    ## -AL -> -IK ; termal -> termik
	t, c = re.subn(fr"(\b)({fund_me_al_ik})(al)({albprapa_0_5})(\b)", r"\2ik\4", t) ; tj_subs += c 

    ## -TIV -> -UES ; komunikativ -> komunikues
	t, c = re.subn(fr"(\b)({fund_me_tiv_ues})(ativ)({albprapa_0_5})(\b)", r"\2ues\4", t) ; tj_subs += c 

    ## -ICIEN -> -IKAN ; matematicien -> matematikan
	t, c = re.subn(fr"(\b)({fund_me_icien})(cien)({albprapa_0_5})(\b)", r"\2kan\4", t) ; tj_subs += c 
	
	return (t, e_subs, c_subs, pj_subs, tj_subs)
