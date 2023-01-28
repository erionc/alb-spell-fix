
import re, string
from korrigjo_pj import *
from percaktime_baze import *

## tema fjalësh që duhen shqipëruar
tema_sq = ""

## tema fjalësh angleze që duhen përkthyer
tema_en = ""

## funksion për zëvendësime që përgatitin zëvendësimet e mëpasshme
def para_korrigjime(text):
	## vlerënisje 
	t = text ; c_subs = 0
	
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
def pas_korrigjime(text):
	## vlerënisje 
	t = text ; c_subs = 0
	
	## çoc -> çoç
	t, c = re.subn(fr"(\b)çoc(\b)", r"çoç", t) ; c_subs += c

	## zëvendësime të tjera 
	
	return (t, c_subs)
	
## funksion për zëvendësimin e fjalëve angleze 
def korrigjo_eng(text):
	## vlerënisje 
	t = text ; eng_subs = 0
	
	return (t, eng_subs)
	
## funksion për zëvendësime fjalësh të plota 
def korrigjo_terma(text):
	## vlerënisje 
	t = text ; word_subs = 0
	
	return (t, word_subs)
	