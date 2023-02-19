
from percaktime import *

## temat që shkruhen me C/c në vend të Ç/ç-së nistore
## ruhen prapashtesat ndaj nuk pranohen tema me grupe alternative me | si (c|ç)
## cafk, caj, cajnik, canak, cibuk, cift, cimk, cmim, co, corap, cudi, cun, cup 
pa_c_nis = "afk|aj|ajnik|anak|akerdis|akmak|ale|alë|alo|alu|allm|apkën|apken|arcaf|arçaf|art|ati|" + \
    "el|ekan|ekic|ekiç|elik|erek|" + \
    "ibuk|ift|ikërrim|ikerrim|iment|imk|izme|" + \
    "mend|merit|mim|min|mo|mont|morrit|" + \
    "nder|njer|" + \
    "o|okollat|orap|organi|orodit|" + \
    "u|udi|un"

## temat që shkruhen me Ç/ç në vend të  C/c-së nistore
## ruhen prapashtesat ndaj nuk pranohen tema me grupe alternative me | si (c|ç)
## çertifikatë, çertifikoj, çertifikim
me_c_nis = "ertifik"

## fjalë që shkruhen me Ç/ç në vend të C/c-së së brendshme
## përfshihen vetëm ato fjalë që përmbajnë vetëm 1 c e cila është e brendshme
def me_c_brenda(text):
    ## vlerënisje
    t = text ; c_subs = 0

    ## (P|p)ro(ç|q)es -> (P|p)roces 
    t, c = re.subn(fr"(\b)(P|p)(roçes|roqes)({prapa})(\b)", r"\2roces\4", t) ; c_subs += c
    ##  (P|p)ro(ç|q)edur -> (P|p)rocedur
    t, c = re.subn(fr"(\b)(P|p)(roçedur|roqedur)({prapa})(\b)", r"\2rocedur\4", t) ; c_subs += c

    return (t, c_subs)

## fjalë që shkruhen me C/c në vend të Ç/ç-së së brendshme
## përfshihen vetëm ato fjalë që përmbajnë vetëm 1 c e cila është e brendshme
def pa_c_brenda(text):
    ## vlerënisje
    t = text ; c_subs = 0

    ## (R|r)e(c|q)el -> (R|r)eçel
    t, c = re.subn(fr"(\b)(R|r)(ecel|eqel)({prapa})(\b)", r"\2eçel\4", t) ; c_subs += c
    ## (A|a)ll(c|q)i -> (A|a)llçi
    t, c = re.subn(fr"(\b)(A|a)(llci|llqi)({prapa})(\b)", r"\2llçi\4", t) ; c_subs += c

    return (t, c_subs)





	
