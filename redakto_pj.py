
from percaktime import *

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
"kap(e|ë)rdi|" + \
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
pj_pa_ar = "akordu|aktivizu|akuzu|analizu|anu|arnu|" + \
"barazu|besu|blu|" + \
"caktu|çliru|çmu|çu|(c|ç)minu|(c|ç)montu|" + \
"darku|dep(e|ë)rtu|d(e|ë)ftu|d(e|ë)gju|drenu|dhunu|dreku|" + \
"f(e|ë)rku|formulu|ftu|" + \
"gatu|g(e|ë)rmu|gllab(e|ë)ru|" + \
"hamend(e|ë)su|" + \
"imitu|" + \
"jetu|" + \
"la|lajm(e|ë)ru|lexu|" + \
"k(e|ë)ndu|k(e|ë)rc(e|ë)nu|k(e|ë)rku|klasifiku|konsumu|kopju|korrigju|kru|kryq(e|ë)zu|kund(e|ë)rshtu|kundru|kuror(e|ë)zu|" + \
"livru|l(e|ë)ndu|" + \
"martu|masivizu|mashtru|mbaru|mendu|m(e|ë)rgu|m(e|ë)su|minu|" + \
"nd(e|ë)rtu|nd(e|ë)shku|ndri(c|ç)u|ndryshu|ngacmu|" + \
"pajtu|parashiku|pastru|pendu|p(e|ë)rdhunu|p(e|ë)rgju|p(e|ë)rjetu|p(ë|e)su|pikturu|pleq(e|ë)ru|profilizu|provu|punu|" + \
"qarku|qarkullu|q(e|ë)ru|" + \
"rreshtu|rreziku|r(e|ë)ndu|rr(e|ë)zu|" + \
"sabotu|sakrifiku|shkarku|shkru|shku|shkurtu|shp(e|ë)rq(e|ë)ndru|shp(e|ë)tu|shpu|shqiptu|shqip(e|ë)ru|shtremb(e|ë)ru|shtru|shtu|shu|shum(e|ë)zu|simpatizu|sinkronizu|" + \
"t(e|ë)rbu|ting(e|ë)llu|trajnu|trazu|tregu|trillu|" + \
"vajtu|varf(e|ë)ru|vazhdu|vepru|verifiku|v(e|ë)llaz(e|ë)ru|vlu|" + \
"zbarku|zgju|zhbiru"

## pjesore të shkurtra që duhet të mbarojnë me 'ur' -- kap -> kapur
pj_pa_ur = "arratis|ardh|" + \
"(c|q|ç)el|(c|ç)mend|" + \
"dash|" + \
"flak|" + \
"g(e|ë)rvisht|gris|gropos|" + \
"hallakat|hap|" + \
"kap|kapardis|korr|kurdis|ky(c|ç)|" + \
"lag|" + \
"mat|majm|mbajt|mbath|mbyt|m(e|ë)rzit|mir(e|ë)mbajt|" + \
"ndesh|ngrit|ngrys|" + \
"pas|p(e|ë)rmbajt|p(e|ë)rplas|" + \
"qelb|qit|" + \
"rrah|" + \
"shit|shky(c|ç)|shmang|" + \
"thith|" + \
"ul|" + \
"vajt|var|varos|vulos|" + \
"zbardh|zbraps|zbyth|zgjat|zmbraps|zhyt"

## pjesore të shkurtra që mbarojnë me 'y' por që duhet të 
## mbarojnë me 'yer' -- thy -> thyer		   
pj_pa_er = "d(e|ë)fry|d(e|ë)mshp(e|ë)rbly|" + \
"f(e|ë)rsh(e|ë)lly|fishk(e|ë)lly|fy|" + \
"g(e|ë)njy|gry|" + \
"hak(e|ë)rry|" + \
"kap(e|ë)rcy|k(e|ë)mby|k(e|ë)rcy|kry|kthy|kursy|" + \
"ly|" + \
"mall(e|ë)ngjy|mb(e|ë)rthy|" + \
"ngadh(e|ë)njy|ngash(e|ë)ry|ngaz(e|ë)lly|ng(e|ë)rthy|ngjy|" + \
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
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0
		
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
	t, c = re.subn(fr"(\b)({fj_dial})(e?)(\b)", r"\2a", t) ; tj_subs += c

	# ## për me + pjesore -> për të + pjesore
	# t, c = re.subn(fr"(\b)(p(e|ë)r\sme\s)({pj_pa_e})(\b)", r"\2\3ë", t) ; pj_subs += c

	return (t, e_subs, c_subs, pj_subs, tj_subs)
	
	