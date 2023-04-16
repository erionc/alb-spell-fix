
from percaktime import *


## shkruhen me CIEN por duhen shkruar me KAN
fund_me_icien = "Fizi|fizi|" + \
    "Informati|informati|" + \
    "Matemati|matemati|" + \
    "Statisti|statisti" 


## funksion për zëvendësimin e fjalëve angleze 
def perkthime(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0
	
	return (t, e_subs, c_subs, tj_subs)
	
## funksion për zëvendësime fjalësh të plota 
def shqiperime(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

    ## ICIEN -> IKAN ; matematicien -> matematikan
	t, c = re.subn(fr"(\b)({fund_me_icien })(cien)({prapa_gjat})(\b)", r"\2kan\4", t) ; tj_subs += c
	
	return (t, e_subs, c_subs, tj_subs)