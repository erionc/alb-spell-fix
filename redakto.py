
from redakto_pj import *
from redakto_e import *
from redakto_c import *

## tema fjalësh që duhen shqipëruar
tema_sq = ""

## tema fjalësh angleze që duhen përkthyer
tema_en = ""

## funksion për zëvendësime që përgatitin zëvendësimet e mëpasshme
def para_redaktime(text):
	## vlerënisje 
	t = text ; c_subs = 0

	## p(e|ë)r me -> për të
	t, c = re.subn(fr"(\b)(per\sme|për\sme)(\b)", r"për të", t) ; c_subs += c
	
	## deshe(m|t|n) -> deshë(m|t|n)
	t, c = re.subn(fr"(\b)(D|d)(eshe)(m|t|n)(\b)", r"\2eshë\4", t) ; c_subs += c

	## cilet -> cilët
	t, c = re.subn(fr"(\b)cilet(\b)", r"cilët", t) ; c_subs += c
	
	## jan(e) -> janë, kan(e) -> kanë
	t, c = re.subn(fr"(\b)(J|j|K|k)(an)(e)?(\b)", r"\2anë", t) ; c_subs += c
	
	## pate(m|t|n) -> patë(m|t|n)
	t, c = re.subn(fr"(\b)(pate)(m|t|n)(\b)", r"patë\3", t) ; c_subs += c
	## qe(m|t|n)(e?) -> qe(m|t|n)ë
	t, c = re.subn(fr"(\b)(Q|q)(e)(m|t|n)(e)?(\b)", r"\2e\4ë", t) ; c_subs += c
	
	## kena -> kemi ; jena -> jemi
	t, c = re.subn(fr"(\b)(K|k|J|j)(ena)(\b)", r"\2emi", t) ; c_subs += c
	
	## per -> për (nuk ka per në fgjssh)
	t, c = re.subn(fr"(\b)per(\b)", r"për", t) ; c_subs += c
	
	## do te -> do të ; dua te -> dua të 
	t, c = re.subn(fr"(\b)({para_te})(te)(\b)", r"\2të", t) ; c_subs += c
	
	## zëvendësime të tjera e -> ë
	
	return (t, c_subs)
	
## funksion për zëvendësime që korrigjojnë zëvendësimet e mëparshme
def pas_redaktime(text):
	## vlerënisje 
	t = text ; c_subs = 0
	
	## çoc -> çoç
	t, c = re.subn(fr"(\b)çoc(\b)", r"çoç", t) ; c_subs += c

	## zëvendësime të tjera 
	
	return (t, c_subs)
	
## funksion për zëvendësimin e fjalëve angleze 
def redakto_eng(text):
	## vlerënisje 
	t = text ; eng_subs = 0
	
	return (t, eng_subs)
	
## funksion për zëvendësime fjalësh të plota 
def redakto_terma(text):
	## vlerënisje 
	t = text ; word_subs = 0
	
	return (t, word_subs)

## funksioni kryesor i redaktimeve që thërret funksionet e tjera
def redakto(text):
	## vlerënisje
	t = text ; total_sub = 0

	# thirren zëvendësimet paraprake
	t, c = para_redaktime(t) ; total_sub += c

	# thirren zëvendësimet e pjesoreve
	t, c = redakto_pjes(t) ; total_sub += c
	
	# thirren zëvendësimet e e-së
	t, c = redakto_e(t) ; total_sub += c
	
	# thirren zëvendësimet e c-së
	t, c = redakto_c(t) ; total_sub += c
	
	# thirren zëvendësime e fjalëve
	t, c = redakto_terma(t) ; total_sub += c
	
	# thirren zëvendësime e fjalëve angleze
	t, c = redakto_eng(t) ; total_sub += c
	
	# thirren zëvendësimet përfundimtare
	t, c = pas_redaktime(t) ; total_sub += c

	return (t, total_sub)
	