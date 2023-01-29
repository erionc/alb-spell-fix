
from percaktime_baze import *

## pjesore që mbarojnë me 'u(r(e))', 'e(r(e))', 'a(r(e))', 'y(r(e))' 
## por që duhet të mbarojnë me 'rë' -- pru -> prurë, pre -> prerë, 
## sha -> sharë, shty -> shtyrë
pj_pa_re = "ble|" + \
"ça|" + \
"fshi|" + \
"gdhi|gri|" + \
"la|lëpi|" + \
"mar|mbi|mpi|" + \
"nda|nga|ngri|nxi|nxjer|" + \
"pa|p(e|ë)r(c|ç)a|përfshi|përpi|pi|pre|pri|pru|" + \
"qa|" + \
"sha|shka|shkri|shp(e|ë)la|shp(e|ë)rnda|shtri|shty|" + \
"tështi|tha|" + \
"vet(e|ë)vra|vra"

## pjesore të shkurtra që mbarojnë me 'u' por që duhet të 
## mbarojnë me 'ar' -- shku -> shkuar
pj_pa_ar = "besu|blu|" + \
"caktu|çmu|çu|d(e|ë)gju|" + \
"dhunu|" + \
"ftu|la|lexu|" + \
"k(e|ë)rku|kru|" + \
"mbaru|mendu|m(e|ë)su|" + \
"nd(e|ë)shku|ngacmu|" + \
"p(ë|e)su|punu|provu|" + \
"shkru|shku|shtru|shtu|shu|" + \
"vlu|" + \
"zgju"

## pjesore të shkurtra që duhet të mbarojnë me 'ur' -- kap -> kapur
pj_pa_ur = "ardh|" + \
"flak|" + \
"hallakat|hap|" + \
"kap|" + \
"lag|" + \
"mat|majm|mbajt|mbyt|m(e|ë)rzit|mir(e|ë)mbajt|" + \
"ngrit|" + \
"p(e|ë)rmbajt|" + \
"qit|" + \
"rrah|" + \
"shit|" + \
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
"ngall(e|ë)njy|ngash(e|ë)ry|ngaz(e|ë)lly|" + \
"parap(e|ë)lqy|p(e|ë)lqy|p(e|ë)rkthy|p(e|ë)rly|p(e|ë)rthy|" + \
"ng(e|ë)rthy|ngjy|" + \
"rr(e|ë)fy|rr(e|ë)mby|" + \
"sh(e|ë)rby|shk(e|ë)lqy|shly|shqy|shp(e|ë)rbly|shp(e|ë)rthy|" + \
"thy|" + \
"urry|ushqy|" + \
"vy|" + \
"zb(e|ë)rthy|zhg(e|ë)njy|zhy"

## fjalë dialektore që mbarojnë me 'u(e)' por që duhet të 
## mbarojnë me 'ua' -- du(e) -> dua, thu(e) -> thua
fj_dial = "(D|d)u|(G|g)ru|(M|m)u|(T|t)hu"


## funksion për zëvendësimin e pjesoreve të shkurtëra
def korrigjo_pjes(text):
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

	## fjalë që shnkruhen pa a në fund -- du(e) -> dua, thu(e) -> thua
	t, c = re.subn(fr"(\b)({fj_dial})(e?)(\b)", r"\2a", t) ; pj_subs += c

	return (t, pj_subs)
	
	