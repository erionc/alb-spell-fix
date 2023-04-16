
from percaktime import *
from redakto_pj import *
from redakto_e import *
from redakto_c import *

## fjalë që i paraprinë të-së -- do të, dua të, desha të 
para_te = "dua\s|do\s|duam\s|doni\s|duan\s|doja\s|doje\s|donte\s|" + \
	"donim\s|donit\s|donin\s|desha\s|deshe\s|deshte\s|deshëm\s|" + \
	"deshët\s|deshën\s|me\s|sapo\s|porsa\s|duhet\s|sikur\s|mund\s|" + \
	"kush\s|cil(i|a)\s|cil(ë|a)t\s|ku\sdo\s|kur\sdo\s|(c|ç)far(e|ë)\s|" 

## tema fjalësh që duhen shqipëruar
tema_sq = ""

## tema fjalësh angleze që duhen përkthyer
tema_en = ""

## funksion për zëvendësime që përgatitin zëvendësimet e mëpasshme
def para_redaktime(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

	## per -> për (nuk ka "per" në fgjssh)
	t, c = re.subn(fr"(\b)per(\b)", r"për", t) ; e_subs += c

	## p(e|ë)r me -> për të
	t, c = re.subn(fr"(\b)(per\sme|për\sme)(\b)", r"për të", t) ; e_subs += c
	
	## deshe(m|t|n) -> deshë(m|t|n)
	t, c = re.subn(fr"(\b)(D|d)(eshe)(m|t|n)(\b)", r"\2eshë\4", t) ; e_subs += c

	## cilet -> cilët
	t, c = re.subn(fr"(\b)cilet(\b)", r"cilët", t) ; e_subs += c
	
	## jan(e) -> janë, kan(e) -> kanë
	t, c = re.subn(fr"(\b)(J|j|K|k)(an)(e)?(\b)", r"\2anë", t) ; e_subs += c
	
	## pate(m|t|n) -> patë(m|t|n)
	t, c = re.subn(fr"(\b)(pate)(m|t|n)(\b)", r"patë\3", t) ; e_subs += c
	## qe(m|t|n)(e?) -> qe(m|t|n)ë
	t, c = re.subn(fr"(\b)(Q|q)(e)(m|t|n)(e)?(\b)", r"\2e\4ë", t) ; e_subs += c
	
	## kena -> kemi ; jena -> jemi
	t, c = re.subn(fr"(\b)(K|k|J|j)(ena)(\b)", r"\2emi", t) ; tj_subs += c
	
	## do te -> do të ; dua te -> dua të ; desha te -> desha të
	t, c = re.subn(fr"(\b)({para_te})(te)(\b)", r"\2të", t) ; e_subs += c
	
	## zëvendësime të tjera e -> ë
	
	return (t, e_subs, c_subs, tj_subs)
	
## funksion për zëvendësime që korrigjojnë zëvendësimet e mëparshme
def pas_redaktime(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0
	
	## çoc -> çoç
	t, c = re.subn(fr"(\b)çoc(\b)", r"çoç", t) ; c_subs += c

	## zëvendësime të tjera 
	
	return (t, e_subs, c_subs, tj_subs)
	
## funksion për zëvendësimin e fjalëve angleze 
def redakto_eng(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0
	
	return (t, e_subs, c_subs, tj_subs)
	
## funksion për zëvendësime fjalësh të plota 
def redakto_terma(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0
	
	return (t, e_subs, c_subs, tj_subs)

## funksioni kryesor i redaktimeve që thërret funksionet e tjera
def redakto(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

	# thirren zëvendësimet paraprake
	t, e_c, c_c, tj_c = para_redaktime(t) 
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c

	# thirren zëvendësimet e pjesoreve
	t, e_c, c_c, tj_c = redakto_pjes(t) 
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c
	
	# thirren zëvendësimet e e-së
	t, e_c, c_c, tj_c = redakto_e(t) 
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c
	
	# thirren zëvendësimet e c-së
	t, e_c, c_c, tj_c = redakto_c(t) 
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c
	
	# thirren zëvendësime e fjalëve
	t, e_c, c_c, tj_c = redakto_terma(t) 
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c
	
	# thirren zëvendësime e fjalëve angleze
	t, e_c, c_c, tj_c = redakto_eng(t) 
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c
	
	# thirren zëvendësimet përfundimtare
	t, e_c, c_c, tj_c = pas_redaktime(t) 
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c

	return (t, e_subs, c_subs, tj_subs)
	