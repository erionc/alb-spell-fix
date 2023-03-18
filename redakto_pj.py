
import re, string

## 0-5 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
prapa = "[a-zA-Z0-9çÇëË_-]{0,5}"

## fjalë që i paraprinë të-së -- do të, dua të, desha të 
para_te = "dua\s|do\s|duam\s|doni\s|duan\s|doja\s|doje\s|donte\s|" + \
	"donim\s|donit\s|donin\s|desha\s|deshe\s|deshte\s|deshëm\s|" + \
	"deshët\s|deshën\s|me\s|sapo\s|porsa\s|duhet\s|sikur\s|mund\s|" + \
	"kush\s|cil(i|a)\s|cil(ë|a)t\s|ku\sdo\s|kur\sdo\s|(c|ç)far(e|ë)\s|" 

## foljet ndihmëse kam/jam që paraprijnë pjesoret
kam_jam = "Kam\s|kam\s|Ke\s|ke\s|Ka\s|ka\s|Kemi\s|Kena\s|kemi\s|kena\s|Keni\s|keni\s|Kanë\s|kanë\s|" + \
	"Jam\s|jam\s|Je\s|je\s|Është\s|është\s|Jemi\s|Jena\s|jemi\s|jena\s|Jeni\s|jeni\s|Janë\s|janë\s|" + \
	"Kisha\s|kisha\s|Kishe\s|kishe\s|Kishte\s|kishte\s|Kishim\s" + \
	"kishim\s|Kishit\s|kishit\s|Kishin\s|kishin\s|" + \
	"Isha\s|isha\s|Ishe\s|ishe\s|Ishte\s|ishte\s|Ishim\s|ishim\s|" + \
	"Ishit\s|ishit\s|Ishin\s|ishin\s|" + \
	"Pata\s|pata\s|Pate\s|pate\s|Pati\s|pati\s|Patëm\s|patëm\s|" + \
	"Patët\s|patët\s|Patën\s|patën\s|" + \
	"Qeshë\s|qeshë\s|Qe\s|qe\s|Qemë\s|qemë\s|Qetë\s|qetë\s|" + \
	"Qenë\s|qenë\s|"

## format e pashtjelluara që paraprijnë pjesoret
form_pashtj = "për\stë\s|duke\s|pa\s|"

## të tjera forma që qëndrojnë para pjesores 
tjera_para_pjesor = "me\stë\s"

## forma që qëndrojnë para pjesores
para_pjesoreve = kam_jam + form_pashtj + tjera_para_pjesor


## pjesore që mbarojnë me 'u(r(e))', 'e(r(e))', 'a(r(e))', 'y(r(e))' 
## por që duhet të mbarojnë me 'rë' -- pru -> prurë, pre -> prerë, 
## sha -> sharë, shty -> shtyrë
pj_pa_re = "ble|" + \
"ça|" + \
"fshi|" + \
"gdhi|gri|" + \
"la|l(e|ë)pi|" + \
"mar|mbi|mpi|" + \
"nda|ndy|nga|ngri|nxi|nxjer|" + \
"pa|p(e|ë)r(c|ç)a|përfshi|p(e|ë)rpi|p(e|ë)shty|pi|pre|pri|pru|" + \
"qa|" + \
"sha|shka|shkri|shp(e|ë)la|shp(e|ë)rnda|shtri|shty|" + \
"tështi|tha|" + \
"vet(e|ë)vra|vra"

## pjesore të shkurtra që mbarojnë me 'u' por që duhet të 
## mbarojnë me 'ar' -- shku -> shkuar
pj_pa_ar = "akordu|aktivizu|akuzu|analizu|arnu|" + \
"barazu|besu|blu|" + \
"caktu|çliru|çmu|çu|(c|ç)minu|" + \
"darku|dep(e|ë)rtu|d(e|ë)ftu|d(e|ë)gju|drenu|dhunu|dreku|" + \
"f(e|ë)rku|ftu|" + \
"g(e|ë)rmu|gllab(e|ë)ru|" + \
"hamend(e|ë)su|" + \
"imitu|" + \
"la|lajm(e|ë)ru|lexu|" + \
"k(e|ë)ndu|k(e|ë)rc(e|ë)nu|k(e|ë)rku|klasifiku|konsumu|kopju|korrigju|kru|kryq(e|ë)zu|kund(e|ë)rshtu|" + \
"livru|l(e|ë)ndu|" + \
"martu|masivizu|mashtru|mbaru|mendu|m(e|ë)su|minu|" + \
"nd(e|ë)shku|ngacmu|" + \
"pajtu|pendu|p(e|ë)rdhunu|p(ë|e)su|pikturu|provu|punu|" + \
"qarku|qarkullu|q(e|ë)ru|" + \
"rreziku|r(e|ë)ndu|" + \
"sakrifiku|shkarku|shkru|shku|shp(e|ë)tu|shpu|shqiptu|shqip(e|ë)ru|shtremb(e|ë)ru|shtru|shtu|shu|shum(e|ë)zu|" + \
"trajnu|trazu|" + \
"vajtu|varf(e|ë)ru|vazhdu|vepru|verifiku|v(e|ë)llaz(e|ë)ru|vlu|" + \
"zbarku|zgju"

## pjesore të shkurtra që duhet të mbarojnë me 'ur' -- kap -> kapur
pj_pa_ur = "ardh|" + \
"(c|q|ç)el|(c|ç)mend|" + \
"dash|" + \
"flak|" + \
"hallakat|hap|" + \
"kap|korr|kurdis|" + \
"lag|" + \
"mat|majm|mbajt|mbath|mbyt|m(e|ë)rzit|mir(e|ë)mbajt|" + \
"ndesh|ngrit|ngrys|" + \
"pas|p(e|ë)rmbajt|" + \
"qelb|qit|" + \
"rrah|" + \
"shit|shkurtu|" + \
"thith|" + \
"ul|" + \
"vajt|vulos|" + \
"zbardh|zbraps|zgjat|zmbraps|zhyt"

## pjesore të shkurtra që mbarojnë me 'y' por që duhet të 
## mbarojnë me 'yer' -- thy -> thyer		   
pj_pa_er = "d(e|ë)fry|d(e|ë)mshp(e|ë)rbly|" + \
"f(e|ë)rsh(e|ë)lly|fishk(e|ë)lly|fy|" + \
"g(e|ë)njy|gry|" + \
"hak(e|ë)rry|" + \
"kap(e|ë)rcy|k(e|ë)mby|k(e|ë)rcy|kry|kthy|kursy|" + \
"ly|" + \
"mall(e|ë)ngjy|mb(e|ë)rthy|" + \
"ngall(e|ë)njy|ngash(e|ë)ry|ngaz(e|ë)lly|ng(e|ë)rthy|ngjy|" + \
"parap(e|ë)lqy|p(e|ë)lqy|p(e|ë)rkthy|p(e|ë)rly|p(e|ë)rthy|" + \
"rr(e|ë)fy|rr(e|ë)mby|" + \
"sh(e|ë)rby|shk(e|ë)lqy|shly|shqy|shp(e|ë)rbly|shp(e|ë)rthy|" + \
"thy|" + \
"urry|ushqy|" + \
"vy|" + \
"zb(e|ë)rthy|zhg(e|ë)njy|zhg(e|ë)rry|zhy"

## pjesore të shkurtra që duhet të mbarojnë me 'ë' -- qen -> qenë, vën -> vënë
pj_pa_e = "dal|l(e|ë)n|mbjell|ngr(e|ë)n|q(e|ë)n|sht(e|ë)n|th(e|ë|a)n|v(e|ë)n|z(e|ë)n"

## fjalë dialektore që mbarojnë me 'u(e)' por që duhet të 
## mbarojnë me 'ua' -- du(e) -> dua, thu(e) -> thua
fj_dial = "(D|d)u|(G|g)ru|(M|m)u|(T|t)hu"


## funksion për zëvendësimin e pjesoreve të shkurtëra
def redakto_pjes(text):
	## vlerënisje 
	t = text ; pj_subs = 0
		
	## pjesoret që shkruhen pa rë në fund -- pru -> prurë
	t, c = re.subn(fr"(\b)({para_pjesoreve})({pj_pa_re})(r(e)?)?(\b)", r"\2\3rë", t) ; pj_subs += c

	## pjesoret që shkruhen pa ar në fund -- shku -> shkuar
	t, c = re.subn(fr"(\b)({para_pjesoreve})({pj_pa_ar})(\b)", r"\2\3ar", t) ; pj_subs += c
	
	## pjesoret që shkruhen pa ur në fund -- kap -> kapur
	t, c = re.subn(fr"(\b)({para_pjesoreve})({pj_pa_ur})(\b)", r"\2\3ur", t) ; pj_subs += c

	## pjesoret që shkruhen pa er në fund -- thy -> thyer
	t, c = re.subn(fr"(\b)({para_pjesoreve})({pj_pa_er})(\b)", r"\2\3er", t) ; pj_subs += c

	## pjesoret që shkruhen pa ë në fund -- qen -> qenë, vën -> vënë
	t, c = re.subn(fr"(\b)({para_pjesoreve})({pj_pa_e})(\b)", r"\2\3ë", t) ; pj_subs += c

	## fjalë që shnkruhen pa a në fund -- du(e) -> dua, thu(e) -> thua
	t, c = re.subn(fr"(\b)({fj_dial})(e?)(\b)", r"\2a", t) ; pj_subs += c



	# ## për me + pjesore -> për të + pjesore
	# t, c = re.subn(fr"(\b)(p(e|ë)r\sme\s)({pj_pa_e})(\b)", r"\2\3ë", t) ; pj_subs += c

	return (t, pj_subs)
	
	