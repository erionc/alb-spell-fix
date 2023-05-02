
from redakto_pj import *
from redakto_e import *
from redakto_c import *
from shqipero import *

## fjalë që i paraprinë të-së -- do të, dua të, desha të 
para_te = "dua\s|do\s|duam\s|doni\s|duan\s|doja\s|doje\s|donte\s|" + \
	"donim\s|donit\s|donin\s|desha\s|deshe\s|deshte\s|deshëm\s|" + \
	"deshët\s|deshën\s|me\s|sapo\s|porsa\s|duhet\s|sikur\s|mund\s|" + \
	"kush\s|cil(i|a)\s|cil(ë|a)t\s|ku\sdo\s|kur\sdo\s|(c|ç)far(e|ë)\s" 

def hiq_tekst_joshqip(text):
	## hiq hiperlidhjet
	text = re.sub(r'<[^>]*/>', '', text)
	## hiq termat frëngjisht
	text = re.sub(r'\((F|f)r\w*(\.|:)(.*?)\)', '', text)
	## hiq termat italisht
	text = re.sub(r'\((I|i)t\w*(\.|:)(.*?)\)', '', text)
	## hiq termat anglisht
	text = re.sub(r'\((A|a)ng\w*(\.|:)(.*?)\)', '', text)
	text = re.sub(r'\((E|e)n\w*(\.|:)(.*?)\)', '', text)
	## hiq termat gjermanisht
	text = re.sub(r'\((G|g)jer\w*(\.|:)(.*?)\)', '', text)
	text = re.sub(r'\((D|d)e\w*(\.|:)(.*?)\)', '', text)
	## hiq termat spanjisht
	text = re.sub(r'\((S|s)p\w*(\.|:)(.*?)\)', '', text)
	text = re.sub(r'\((E|e)s\w*(\.|:)(.*?)\)', '', text)
	## hiq termat rusisht
	text = re.sub(r'\((R|r)us\w*(\.|:)(.*?)\)', '', text)
	## hiq termat japonisht
	text = re.sub(r'\((J|j)ap\w*(\.|:)(.*?)\)', '', text)
	## hiq termat portugalisht
	text = re.sub(r'\((P|p)ort\w*(\.|:)(.*?)\)', '', text)
	## hiq termat kineze
	text = re.sub(r'\((K|k)in\w*(\.|:)(.*?)\)', '', text)
	## hiq termat turke
	text = re.sub(r'\((T|t)ur\w*(\.|:)(.*?)\)', '', text)
	## hiq termat arabe
	text = re.sub(r'\((A|a)rab\w*(\.|:)(.*?)\)', '', text)

	## remove double+ spaces between two words
	text = re.sub(r'(\w+)([ ]{2,})(\w+)', r'\1 \3', text)

	return text

## funksion për zëvendësime që përgatitin zëvendësimet e mëpasshme
def para_redaktime(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0

	## hiq fjalët e huaja
	t = hiq_tekst_joshqip(t)

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
	
	return (t, e_subs, c_subs, pj_subs, tj_subs)
	
## funksion për zëvendësime që korrigjojnë zëvendësimet e mëparshme
def pas_redaktime(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0
	
	## çoc -> çoç
	t, c = re.subn(fr"(\b)çoc(\b)", r"çoç", t) ; c_subs += c

	## te + folje -> të + folje
	t, c = re.subn(fr"(\b)(te )({folje})({albprapa_0_3})(\b)", r"të \3\4", t) ; e_subs += c

	## te te + folje -> të të + folje
	t, c = re.subn(fr"(\b)(te |të )(te |të )({folje})({albprapa_0_3})(\b)", r"të të \4\5", t) ; e_subs += c

	## prapësime të zëvendësimeve te disa fjalë të huaja

	## zëvendësime të tjera 
	
	return (t, e_subs, c_subs, pj_subs, tj_subs)
	
## funksioni kryesor i redaktimeve që thërret funksionet e tjera
def redakto(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0

	# thirren zëvendësimet paraprake
	t, e_c, c_c, p_c, tj_c = para_redaktime(t) 
	c_subs += c_c ; e_subs += e_c ; pj_subs += p_c ; tj_subs += tj_c

	# thirren zëvendësimet e pjesoreve
	t, e_c, c_c, p_c, tj_c = redakto_pjes(t) 
	c_subs += c_c ; e_subs += e_c ; pj_subs += p_c ; tj_subs += tj_c
	
	# thirren zëvendësimet e e-së
	t, e_c, c_c, p_c, tj_c = redakto_e(t) 
	c_subs += c_c ; e_subs += e_c ; pj_subs += p_c ; tj_subs += tj_c
	
	# thirren zëvendësimet e c-së
	t, e_c, c_c, p_c, tj_c = redakto_c(t) 
	c_subs += c_c ; e_subs += e_c ; pj_subs += p_c ; tj_subs += tj_c
	
	# thirren zëvendësime për shqipërime
	t, e_c, c_c, p_c, tj_c = shqiperime(t) 
	c_subs += c_c ; e_subs += e_c ; pj_subs += p_c ; tj_subs += tj_c
	
	# thirren zëvendësime për përkthime
	t, e_c, c_c, p_c, tj_c = perkthime(t) 
	c_subs += c_c ; e_subs += e_c ; pj_subs += p_c ; tj_subs += tj_c
	
	# thirren zëvendësimet përfundimtare
	t, e_c, c_c, p_c, tj_c = pas_redaktime(t) 
	c_subs += c_c ; e_subs += e_c ; pj_subs += p_c ; tj_subs += tj_c

	return (t, e_subs, c_subs, pj_subs, tj_subs)
	