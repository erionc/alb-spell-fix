
from fund_me_e import *
from fund_pa_e import *

## funksion për zëvendësime e -> ë 
def korrigjo_e(text):
	## velerënisje
	t = text ; e_subs = 0
	
	## Është
	t, c = re.subn(fr"(\b)(E|Ë)(sht)(e|ë)?(\b)", r"Ë\3ë", t) ; e_subs += c
	## është
	t, c = re.subn(fr"(\b)(e|ë)(sht)(e|ë)?(\b)", r"ë\3ë", t) ; e_subs += c
	
	# thirren zëvendësimet e ë-së fundore të munguar
	t, c = korrigjo_pa_e(t) ; e_subs += c
	
	# thirren zëvendësimet e ë-së fundore të shkruar e
	t, c = korrigjo_me_e(t) ; e_subs += c
	
	return (t, e_subs)
