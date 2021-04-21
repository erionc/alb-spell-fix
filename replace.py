
import re, string

## 0-3 simbole shtesë në fund të fjalëve për të kapur prapashtesa 
## shquese dhe lakesat
suf = "[a-zA-Z0-9çÇëË_-]{0,4}"

## global variable that matches the ending of a word - (\b) is better
# we = " |\t|\n|\.|\?|:|;|,|!"

## fjalë që i paraprinë të-së - do të, dua të, desha të 
para_te = "dua\s|do\s|duam\s|doni\s|duan\s|doja\s|doje\s|donte\s|donim\s|" + \
"donit\s|donin\s|desha\s|deshe\s|deshte\s|deshëm\s|deshët\s|deshën\s|" + \
"me\s|sapo\s|porsa\s|duhet\s|sikur\s|mund\s|kush\s|cil(i|a)\s|cil(ë|a)t\s|" + \
"ku\sdo\s|kur\sdo\s" 

## foljet ndihmëse kam/jam që paraprijnë pjesoret
kj = "Kam\s|kam\s|Ke\s|ke\s|Ka\s|ka\s|Kemi\s|kemi\s|Keni\s|keni\s|" + \
	 "Kanë\s|kanë\s|" + \
	 "Jam\s|jam\s|Je\s|je\s|Është\s|është\s|Jemi\s|" + \
	 "jemi\s|Jeni\s|jeni\s|Janë\s|janë\s|" + \
	 "Kisha\s|kisha\s|Kishe\s|kishe\s|Kishte\s|kishte\s|Kishim\s" + \
	 "kishim\s|Kishit\s|kishit\s|Kishin\s|kishin\s|" + \
	 "Isha\s|isha\s|Ishe\s|ishe\s|Ishte\s|ishte\s|Ishim\s|ishim\s|" + \
	 "Ishit\s|ishit\s|Ishin\s|ishin\s|" + \
	 "Pata\s|pata\s|Pate\s|pate\s|Pati\s|pati\s|Patëm\s|patëm\s|" + \
	 "Patët\s|patët\s|Patën\s|patën\s|" + \
	 "Qeshë\s|qeshë\s|Qe\s|qe\s|Qemë\s|qemë\s|Qetë\s|qetë\s|" + \
	 "Qenë\s|qenë\s|"

## format e pashtjelluara që paraprijnë pjesoret
psht = "për\stë\s|duke\s|pa\s|"

## të tjera forma që qëndrojnë para pjesores 
pptj = "me\stë"

## forma që qëndrojnë para pjesores
pp = kj + psht + pptj

## pjesore të shkurtra që mbarojnë me 'u(r(e))', 'e(r(e))', 'a(r(e))' 
## por që duhet të mbarojnë me 'rë' -- pru -> prurë
pj_pa_re = "ble|fshi|gdhi|gri|la|lëpi|mar|mbi|mpi|nda|nga|ngri|nxi|nxjer|" + \
"pa|përfshi|përpi|pi|pre|pri|pru|qa|sha|shkri|shtri|shty|tështi|tha|vra"

## pjesore të shkurtra që mbarojnë me 'u' por që duhet të 
## mbarojnë me 'ar' -- shku -> shkuar
pj_pa_ar = "besu|d(e|ë)gju|dhunu|k(e|ë)rku|lexu|m(e|ë)su|" + \
"nd(e|ë)shku|ngacmu|shkru|shku|p(ë|e)su|punu|provu"

## pjesore të shkurtra që duhet të mbarojnë me 'ur' -- kap -> kapur
pj_pa_ur = "ardh|hap|kap|mat|mbyt|m(e|ë)rzit|ngrit|shit|thith|ul|" + \
"vulos|zbardh|zbraps|zmbraps|zhyt"

## pjesore të shkurtra që mbarojnë me 'y' por që duhet të 
## mbarojnë me 'yer' -- thy -> thyer		   
pj_pa_er = "fy|gry|kry|kthy|ly|shqy|thy"

## fjalë gegërisht që mbarojnë me 'u(e)' por që duhet të 
## mbarojnë me 'ua' -- du(e) -> dua, thu(e) -> thua
fj_dial = "(D|d)u|(G|g)ru|(M|m)u|(T|t)hu"

## tema fjalësh që duhen shqipëruar
tem_sq = ""

## tema fjalësh angleze që duhen përkthyer
tem_en = "file"

## funksion për zëvendësime nga të cilat varen zëvendësimet e tjera
def replace_dep(text):
	## initializations 
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
	
	## do te -> do të
	t, c = re.subn(fr"(\b)({para_te})(te)(\b)", r"\2të", t) ; c_subs += c
	
	## other e -> ë replacements here
	
	return (t, c_subs)

## function for replacing dialectic forms
def replace_dial(text):
	## initializations 
	t = text ; dial_subs = 0
	
	## fjalë që shnkruhen pa a në fund - du(e) -> dua, thu(e) -> thua
	t, c = re.subn(fr"(\b)({fj_dial})(e?)(\b)", r"\2a", t) ; dial_subs += c
	
	## pjesoret që shkruhen pa rë në fund - pru -> prurë
	t, c = re.subn(fr"(\b)({pp})({pj_pa_re})(r(e)?)?(\b)", r"\2\3rë", t) ; dial_subs += c

	## pjesoret që shkruhen pa ar në fund - shku -> shkuar
	t, c = re.subn(fr"(\b)({pp})({pj_pa_ar})(\b)", r"\2\3ar", t) ; dial_subs += c
	
	## pjesoret që shkruhen pa ur në fund - kap -> kapur
	t, c = re.subn(fr"(\b)({pp})({pj_pa_ur})(\b)", r"\2\3ur", t) ; dial_subs += c

	## pjesoret që shkruhen pa er në fund - thy -> thyer
	t, c = re.subn(fr"(\b)({pp})({pj_pa_er})(\b)", r"\2\3er", t) ; dial_subs += c

	return (t, dial_subs)
	
## function for english words substitutions
def replace_eng(text):
	## initializations 
	t = text ; eng_subs = 0
	
	return (t, eng_subs)
	
## function for word substitutions
def replace_words(text):
	## initializations 
	t = text ; word_subs = 0
	
	return (t, word_subs)
	

	
	