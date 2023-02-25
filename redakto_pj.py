
from percaktime import *

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
pj_pa_ar = "besu|blu|" + \
"caktu|çmu|çu|(c|ç)minu|d(e|ë)gju|" + \
"darku|dhunu|dreku|" + \
"ftu|la|lexu|" + \
"k(e|ë)ndu|k(e|ë)rku|korrigju|kru|kund(e|ë)rshtu|" + \
"livru|l(e|ë)ndu|" + \
"martu|mbaru|mendu|m(e|ë)su|minu|" + \
"nd(e|ë)shku|ngacmu|" + \
"pendu|p(ë|e)su|provu|punu|" + \
"q(e|ë)ru|" + \
"rreziku|r(e|ë)ndu|" + \
"sakrifiku|shkarku|shkru|shku|shp(e|ë)tu|shpu|shtru|shtu|shu|" + \
"trazu|" + \
"vajtu|v(e|ë)llaz(e|ë)ru|vlu|" + \
"zbarku|zgju"

## pjesore të shkurtra që duhet të mbarojnë me 'ur' -- kap -> kapur
pj_pa_ur = "ardh|" + \
"(c|q|ç)el|(c|ç)mend|" + \
"flak|" + \
"hallakat|hap|" + \
"kap|" + \
"lag|" + \
"mat|majm|mbajt|mbyt|m(e|ë)rzit|mir(e|ë)mbajt|" + \
"ngrit|ngrys|" + \
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
pj_pa_e = "l(e|ë)n|ngr(e|ë)n|q(e|ë)n|sht(e|ë)n|th(e|ë|a)n|v(e|ë)n|z(e|ë)n"

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

	return (t, pj_subs)
	
	