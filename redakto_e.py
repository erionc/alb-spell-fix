
from percaktime import *

'''
Fjalë që shkruhen pa ë fundore ose me e në vend të saj -- mir(e) -> mirë
zëvendësohet edhe varianti pa ë fundore, meqë nuk përplaset me ndonjë
fjalë tjetër 
'''

no_e_end = [
# a
['drenalin', 
'ft', 
'jk', 
'lbumin', 
'm', 'mbasad', 'meb', 'mplitud', 
'naliz',
'ngjin', 'nilin', 
'rk', 'rn', 'rnaj', 'rr', 
'spirin', 
'tkin', 
'utostrad',],

# b														
['ab', 'ac', 'af', 'ag', 'alad', 'alt', 'alad', 'alerin', 'altin', 'arn',
'(e|ë)ltaj', 'enzin', '(e|ë)shtaj', 
'ib', 'ibliotek', 'im', 'ishtaj', 'iskaj', 'iskot', 
'lac', 'linaj', 'llokad', 
'obin', 'oj', 'ornaj', 'otin', 
'regaj', 'rek', 'rigad', 'rimaj', 'rinaj', 'ritm', 'rrikad',
'ubullim', 'udalla(c|ç)k', 'uj', 'ujtin', 'uk', 'ul', 'unac', 'ungaj',],

# c		
['açk', 'aher', 'ajk', 'apin', 
'elin', 'entigrad', 
'fag', 
'ungaj'],

# d															
['ad', 'afin', 'aj', 'ardh', 'at', 
'ecigrad', 'eg', 'ekad', 'eltin', 'epozit', 'er', '(e|ë)llinj', 
'h(e|ë)mball', 'hom', 
'iafragm', 'ig', 'isfat', 'isiplin', 'ispozit', 'it', 
'jegurin', 
'oktrin', 'or', 'ordolin',
'rag', 'rejt', 'rit', 'rithnaj',
'ushkaj', 'uzin',
'ymb(e|ë)dhjet',],

# e
['kspedit', 'kspozit',
'n',
'rzin',
'strad',],

# f								
['am', 'asad', 
'errnaj', 
'ieraj', 'iskaj', 
'jal', 
'lam', 'loknaj',
'rik', 
'undaj', 'und(e|ë)rin', 'urk', 'ush', 'ushnaj', 'ushtag',
'ytaqaf',],

# g													
['ab', 'abardin', 'af', 'alin', 'ar', 'ardalin', 'ardhnaj', 'azolin',
'(e|ë)lqerin', '(e|ë)rmadh', '(e|ë)rdhaj', '(e|ë)rmaj', 
'ijotin', 
'jasht', 'jasht(e|ë)mb(e|ë)dhjet', 'jat', 'jeraqin', 'j(e|ë)m', 'jer',
'j(e|ë)kafsh', 'jell', 'jethnaj', 'jiraf', 'jithmon', 'jithnaj', 'jiz',
'jysm(e|ë)kafsh',
'licerin', 'lin',
'odin', 'oj', 'om',
'rad', 'rahm', 'remin', 'rib', 'ril', 'rop', 'roshnaj', 'runaj', 'rykaj', 
'un', 'uraj', 'urgac', 'urnaj',],

# h
['apësir', 'art', 'artin',
'emoglobin', 'er',
'ipotek',
'oshafk',
'umb(e|ë)sir', 'umb(e|ë)tir', 'umner', 'und(e|ë)k(e|ë)rrab',
'und(e|ë)shkab', 'urm'],

# i									
['j', 'mshtaj', 'mtaj',],	

# j
['aj', 'av', 
'et'],
	
# k 	
['abin', 'açk', 'afk', 'afsh', 'aft', 'al', 'aldaj', 'aliqaf',
'alt(e|ë)rin', 'amin', 'anarin', 'anavac', 'antin', 'apic', 'aptin',
'arabin', 'arakatin', 'arfic', 'artolin', 'artotek', 'asht',
'at(e|ë)rmb(e|ë)dhjet',
'(e|ë)rrab', '(e|ë)rthiz',
'inin', 'lim', 'lithm',
'lla(c|ç)',
'odrin', 'okain', 'olesterin', 'omodin', 'opertin', 'orac', 'ov',
'rahaqaf', 'renaj', 'ryeradh', 'rahin',
'ukumjaçk', 'undrin', 'ungac', 'uraj', 'urv', 'ushtetut', 'uzhin',],
	
# l								
['açk', 'afsh', 'agazin', 'agsht', 'akin', 'argin', 'eckurin', 'edhnaj',
'(e|ë)maj', 'ënd', '(e|ë)ndin',
'igatin', 'im', 'imonad', 'imurin', 'ir',
'laçk', 'lamarin', 'isnaj', 'lokaj',
'oj', 'op',
'uft', 'ugaj', 'ugin', 'ugnaj', 'ulnaj', 'umnaj',],

# m								
['agm', 'akin', 'andarin', 'andolin', 'argarin', 'ark', 'art', 'artin',
'atric', 'askarad',
'(e|ë)llag', '(e|ë)ndafsht',
'ij', 'in', 'ir', 'iz',
'jaft',
'oll', 'olldrag', 'orfin', 'ortaj',
'urtaj', 'uzik'],

# n		
['aft', 'aftalin', 'ap', 
'djes', 
'(e|ë)n(e|ë)daj', '(e|ë)nt', '(e|ë)nt(e|ë)mb(e|ë)dhjet',
'gaj', 'gjyr', 
'ikotin', 'inull', 'ism', 'itroglicerin', 
'j', 'j(e|ë)mb(e|ë)dhjet',
],
	
# o				
['fi(c|ç)in',
'limpiad',
'rigjin', 'rt', 
'pozit'],	
	
# p								
['aaft', 'adrejt', 'afk', 'aft', 'ag', 'aj', 'ajag', 'akic',
'arabim', 'arad', 'aradhom', 'arafin', 'arakthin', 'arm', 'araman',
'armend', 'atin',
'elerin', 'em', 'en', 'end', 'enicilin', 'es', 'es(e|ë)mb(e|ë)dhjet',
'(e|ë)shtym',
'in', 'ishin', 'ishnaj',
'jac', 'jeshk',
'la(c|ç)k', 'lag', 'lastelin', 'lejad', 'lepnaj', 'levic', 'llaj', 
'omad', 'ozit',
'rapashpin', 'redh', 'remis', 'rik', 'ron', 'rostitut', 'rotein',
'ul', 'un', 'uplaj', 'ushk',
'yllnaj',],

# q		
['af(e|ë)k(e|ë)rrab',
'indark', 
'uk(e|ë)lin', 'ukm'],	
	
# r											
['ac', 'adh',
'(e|ë)r', 'etin', 'ezolut',
'imt',
'rafshnaj', 'rag', 'raj', 'rangallin', 'rep', 'rib', 'rob',
'ozmarin', 
'rethnaj', 'r(e|ë)kaj', 'r(e|ë)shaj', 'rug', 'rungaj', 'rugic', 'rugin', 
'utin',],

# s												
['a(c|ç)m', 'af', 'ag', 'akarin', 'arag', 
'erenad', 
'fid', 'fin',
'hakullin', 'heg', 'heshnaj', 'hib', 'hkab', 'hkarravin', 'hkat(e|ë)rrin',
'hkoznaj', 'hkrab', 'hkreptim', 'hkresurin', 'hkurraj', 'hpag',
'hpartallin', 'hpejt', 'hpell', 'hport', 'hum', 'humic', 'hqis', 'htat',
'htat(e|ë)mb(e|ë)dhjet', 'htrenjt',
'intez', 'it',
'kilifac', 'kutin',
'ob',
'partakiad', 'pin',
'terlin', 'tin', 'trajc', 'treptomicin', 'tuf',
'uferin', 'ulin', 'hulnaj',
'yprin',],

# t
['aj', 'hagm', 'han', 'ap', 'arab', 'arg', 'arrac', 'avolin', 'et',
'et(e|ë)mb(e|ë)dhjet', 'etraciklin',
'hatin', 'hellin', 'hik',
'oksin', 'orb',
'rag', 'rampolin', 'razir', 'remb(e|ë)dhjet', 'r(e|ë)ndelin',
'rin', 'rungaj',
'urbin',
'yftaj', 'ymnaj', 'ymtaj',],	

# u											
['j',
'l(ë|e)rim',
'n', 'niversiad',
'zin'],

# v												
['adh', 'aksin', 'al', 'azelin',
'et(e|ë)tim', 'ezullim',
'ideotek', 'iktim', 'il', 'iolin', 'itamin', 'itrin',
'jeg', 'jeturin',
'lag', 'ler', 'llaj',
'og(e|ë)lin', 'on', 'orb(e|ë)tin',
'rag', 'raj', 'rim'],

# x								
['haj', 'helatin', 'hung',
'in', 'ix', ],	

# y														
['n', 'ndyr'],	

# z										
['an',
'gjyr',
'hab', 'hdrejt',
'jarrt',
'orr'],												
]


'''
Fjalë që shkruhen me e fundore në vend të ë-së -- maje -> majë varianti pa e apo ë fundore ka përplasje me një fjalë tjetër në atë formë, ndaj këto fjalë duhet të zëvendësohen vetëm kur shfaqen me e në fund, pra në shembullin më sipër nuk duhet të ngatërohet maje me maj (muaji)
'''

with_e_end = [
# a
['mvis', 'n',],

# b															
['allin',],

# c		
[],

# d															
['hjet'],

# e
[],

# f								
[],

# g													
['ac', 'urin', 'jelin', 'jeturin',],

# h
['edhurin', 'eroin',],

# i									
[],	

# j
[],	

# k			
['afein', 'am', 'ok'],
	
# l								
['ac', 'lac', 'laj', 'ug', 'yr'],

# m											
['aj', 'arin', 'beturin', 'jegullin', 'ushk'], 

# n					
['grehin', 'j(e|ë)zet'],	

# o							
[],		

# p								
['ort', 'raj', 'rov',],

# q		
['ep',],	
	
# r											
['rafshin', 'rethin',],

# s												
['hin', 'hpatin', 'htat'],

# t
['aks', 'erin', 'errin', 'jer', 'ulin',],	
	
# u											
['rin',],

# v												
['aj'],

# x								
[],	

# y														
[],	

# z										
['gjedh',],												
]

upp = string.ascii_uppercase.replace('W', '') # nistoret e mëdha
low = string.ascii_lowercase.replace('w', '') # nistoret e vogla

# bashkimi i nistoreve të mëdha e të vogla
initials = ['(' + upp[i] + '|' +  low[i] + ')' for i in range(0, 25)]


## përgatitja e shprehjes së rregullt për ë-në fundore të munguar
no_e_exp = [] # bashkësia e fjalëve më sipër

# bashkimi i nistoreve dhe fjalëve që fillojnë me secilën prej tyre
for i in range(0, 25):
	no_e_exp.extend(map((lambda x: initials[i] + x), no_e_end[i]))

# lidhja e fjalëve me operatorin | për formimin e shprehjes së rregullt
no_e_regex = '|'.join(no_e_exp)


## përgatitja e shprehjes së rregullt për e-në fundore të shkruar e
with_e_exp = [] # bashkësia e fjalëve më sipër

# bashkimi i nistoreve dhe fjalëve që fillojnë me secilën prej tyre
for i in range(0, 25):
	with_e_exp.extend(map((lambda x: initials[i] + x), with_e_end[i]))

# lidhja e fjalëve me operatorin | për formimin e shprehjes së rregullt
with_e_regex = '|'.join(with_e_exp)


## fjalë që shfaqin probleme me ë-të fundore
def pa_e_fundore(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

	## fjalë që shkruhen pa ë fundore ose me ë të shkruar e -- mir(e) -> mirë
	t, c = re.subn(fr"(\b)({no_e_regex})(e)?(\b)", r"\2ë", t) ; e_subs += c

	## fjalë që shkruhen me ë fundore të shkruar e -- maje -> majë
	t, c = re.subn(fr"(\b)({with_e_regex})(e)(\b)", r"\2ë", t) ; e_subs += c

	return (t, e_subs, c_subs, tj_subs)


## fjalë që nisin me BË por shpesh shkruhen me BE - beshtineë -> bështinë
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_be = "j|n|jme|jmë|jne|jnë|" + \
	"rtas|rtet|rtasim|rtasin|rtitje|rtitur|rthama|rthamat|rthame|rthamë|rthamor|rthamore" + \
	"shem|shëm|shtaje|shtajë|shtinë"

## fjalë që nisin me DË por shpesh shkruhen me DE - dergoj -> dërgoj
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_de = "fre|fri|" + \
	"nim|noj|nu|" + \
	"rge|rgi|rgo|rgu|" + \
	"shir|shp|sht"

## fjalë që nisin me FË por shpesh shkruhen me FE - femijë -> fëmijë
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_fe = "mij|rge|rgo|rge|rgë|rk|shf"

## fjalë që nisin me GË por shpesh shkruhen me GE - germoj -> gërmoj
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_ge = "l|" + \
	"rb|rm|rv|" + \
	"z"

## fjalë që nisin me GJË por shpesh shkruhen me GJE - gjemim -> gjëmim
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_gje = "ra|rat|send" 

## fjalë që nisin me KË por shpesh shkruhen me KE - keput -> këput
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_ke = "ll|" + \
	"mb|" + \
	"na|" + \
	"nd|" + \
	"ng|" + \
	"put|" + \
	"rc|" + \
	"s|" + \
	"shill|sht|" + \
	"ta|te|ti|tu"

## fjalë që nisin me LË por shpesh shkruhen me LE - leviz -> lëviz
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_le = "ndim|ndo|" + \
	"shim|sho|" + \
	"viz"

## fjalë që nisin me LLË por shpesh shkruhen me LLE - llengë -> llëngë
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_lle = "\w"
	
## fjalë që nisin me MARRË por shpesh shkruhen me MARRE - marreveshje -> marrëveshje
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_marre = "dh|" + \
	"s|" + \
	"ve|" + \
	"zi"
	
## fjalë që nisin me MË por shpesh shkruhen me ME - mesues -> mësues
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_me = "kat|" + \
	"nyr|" + \
	"rga|rgi|rgo|rgu|" + \
	"shir|sim|sue"

## fjalë që nisin me NË por shpesh shkruhen me NE - nensistem -> nënsistem
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_ne = "b\w|c\w|ç\w|d\w|f\w|g\w|k\w|l\w|m\w|na|ne\w|p\w|q\w|r\w|s\w|t\w|u\w|v\w"

## fjalë që nisin me NJË por shpesh shkruhen me NJE - njekohshem -> njëkoshëm
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_nje = "ko|me|si"

## fjalë që nisin me për por shpesh shkruhen me per - permend -> përmend
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_per_shper = "afër|afr|" + \
	"b|" + \
	"cudn|çudn|" + \
	"dit|dor|" + \
	"faqes|faqës|fit|ft|fshi|fund|" + \
	"genjesh|gënjesh|gj|gjith|goj|" + \
	"hap|" + \
 	"k|" + \
	"ligj|" + \
	"mend|" + \
	"nda|" + \
	"pelit|pëlit|pi|pil|piq|pjek|pun|" + \
	"qas|qend|" + \
	"rall|" + \
	"serit|sërit|shkr|shtat|siat|sos|" + \
	"th|" + \
	"ul|ulesi|ulësi|ur|" + \
	"vet|vi|" + \
	"z"

## fjalë që nisin me RË por shpesh shkruhen me RE - renie -> rënie
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_re = "ndes|ndë\w|nie" 

## fjalë që nisin me RRË por shpesh shkruhen me RRE - rrekëllej -> rrëkëllej
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_rre = "mbe|nde|ndo|pir|shkate|shkatë|" 

## fjalë që nisin me SË por shpesh shkruhen me SE - serish -> sërish
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_se = "mu|" + \
	"ke|" + \
	"ndu|" + \
	"ris"

## fjalë që nisin me SHË por shpesh shkruhen me SHE - sheroj -> shëroj
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_she = "nde|ndos|no|rbej|rben|rby|rim|ro|ru" 

## fjalë që nisin me TË por shpesh shkruhen me TE - veshtroj -> vështroj
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_te = "rh\w|rku\w|rth\w"

## fjalë që nisin me VË por shpesh shkruhen me VE - terheq -> tërheq
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_ve = "lli|men|nie|rda|rej|rsu|rtet|shtr|zhg"


## fjalë që përmbajnë DHËS por shpesh shkruhen me DHES - paraardhes -> paraardhës
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_dhes = "Ar|ar|" + \
	"Dre|dre|" + \
	"He|he|" + \
	"Mble|mble|" + \
	"Tre|tre|" + \
	"Vje|vje"

## fjalë që përmbajnë ËK por shpesh shkruhen me EK - pisllek -> pisllëk
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_ek = "Boll|boll|Budallall|budallall|" + \
	"Dembell|dembell|" + \
	"Fodull|fodull|Fukarall|fukarall|" + \
	"Gomarll|gomarll|" + \
	"Hamall|hamall|" + \
	"Pisll|pisll|" + \
	"Synetll|synetll|" + \
	"Tersll|tersll"

## fjalë që përmbajnë ËM por shpesh shkruhen me EM - jashtem -> jashtëm
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_em = "fis|fund|" + \
	"jasht|" + \
	"moç|moc|" + \
	"pafund"

## fjalë që përmbajnë ËR por shpesh shkruhen me ER - seder -> sedër
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_er = "Ashp|ashp|" + \
	"Hat|hat|" + \
	"Kat|kat|Ket|ket|Kod|kod|" + \
	"Lak|lak|Let|let|Lib|lib|Lod|lod|" + \
	"Mbret|mbret|Mjed|mjed|Mjesht|mjesht|Mot|mot|" + \
	"Orkest|orkest|" + \
	"Posht|posht|" + \
	"Sed|sed|shtret|Shqip|" + \
	"Teat|teat|Tjet|tjet|Thjesht|Thjesht|" + \
	"Varf|varf"

## fjalë që përmbajnë ËROR por shpesh shkruhen me EROR - femeror -> femëror
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_eror = "Burr|burr|" + \
	"Fem|fem|Fëmij|fëmij|Femij|femij|" + \
	"Kafsh|kafsh|" + \
	"Vëllaz|vëllaz|Vellaz|vellaz"

## fjalë që përmbajnë ËSI por shpesh shkruhen me ESI - largesi -> largësi
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_esi = "Armiq|armiq|At|at|" + \
	"But|but|" + \
	"Fort|fort|" + \
	"Gjat|gjat|Gjer|gjer|Fshatar|fshatar|" + \
	"Kenaq|kenaq|Kënaq|kënaq|Krip|krip|" + \
	"Larg|larg|Lart|lart|Lasht|lasht|Leht|leht|" + \
	"Madh|madh|Mend|mend|Mëm|mëm|Miq|miq|Mjek|mjek|" + \
	"Pron|pron|" + \
	"Qart|qart|" + \
	"Shëndet|shëndet|Shendet|shendet|Shpejt|shpejt|" + \
	"Rast|rast|Rënd|rënd|Rend|rend|" + \
	"Var|var|Vërtet|vërtet|Vertet|vertet|Vrazhd|vrazhd"

## fjalë që përmbajnë ËSOR por shpesh shkruhen me ESOR - rastesor -> rastësor
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_esor = "Armiq|armiq|Paq|paq|Rast|rast"

## fjalë që përmbajnë SHTË por shpesh shkruhen me SHTE - kreshte -> kreshtë
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_shte = "Ava|ava|" + \
	"Bri|bri|" + \
	"Gja|gja|" + \
	"Ja|ja|" + \
	"Ka|ka|" + \
	"La|la|Le|le|" + \
	"Mbrap|mbrap|" + \
	"She|she|" + \
	"Thje|thje|Tri|tri|" + \
	"Vje|vje"

## fjalë që përmbajnë ËSHT por shpesh shkruhen me ESHT - qumesht -> qumësht
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_esht = "Lag|lag|" + \
	"Plog|plog|" + \
	"Qum|qum"

## fjalë që përmbajnë ËTOR por shpesh shkruhen me ETOR - shërbetor -> shërbëtor
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_etor = "Shërb|shërb|Sherb|sherb"

## fjalë që përmbajnë ËTI por shpesh shkruhen me ETOR - shërbetor -> shërbëtor
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_etor = "Shërb|shërb|Sherb|sherb"

## fjalë që shkruhen me E/e në vend të Ë/ë-së te ndonjë parashtesë
def pa_e_para(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

	## fjalë që nisin me bë - bej -> bëj
	t, c = re.subn(fr"(\b)(be)({nis_me_be})(\b)", r"bë\3", t) ; e_subs += c
	## fjalë që nisin me Bë ; Beshtinë -> Bështinë
	t, c = re.subn(fr"(\b)(Be)({nis_me_be})(\b)", r"Bë\3", t) ; e_subs += c

	## fjalë që nisin me dë - dergoj -> dërgoj
	t, c = re.subn(fr"(\b)(de)({nis_me_de})({prapa_1_12})(\b)", r"dë\3\4", t) ; e_subs += c
	## fjalë që nisin me Dë ; Deshpërim -> Dëshpërim
	t, c = re.subn(fr"(\b)(De)({nis_me_de})({prapa_1_12})(\b)", r"Dë\3\4", t) ; e_subs += c

	## fjalë që nisin me fë - ferkoj -> fërkoj
	t, c = re.subn(fr"(\b)(fe)({nis_me_fe})({prapa_0_12})(\b)", r"fë\3\4", t) ; e_subs += c
	## fjalë që nisin me Fë ; Femijëri -> Fëmijëri
	t, c = re.subn(fr"(\b)(Fe)({nis_me_fe})({prapa_0_12})(\b)", r"Fë\3\4", t) ; e_subs += c

	## fjalë që nisin me gë - germoj -> gërmoj
	t, c = re.subn(fr"(\b)(ge)({nis_me_ge})({prapa_0_12})(\b)", r"gë\3\4", t) ; e_subs += c
	## fjalë që nisin me Bë ; Germim -> Gërmim
	t, c = re.subn(fr"(\b)(Ge)({nis_me_ge})({prapa_0_12})(\b)", r"Gë\3\4", t) ; e_subs += c

	## fjalë që nisin me gjë - gjera -> gjëra
	t, c = re.subn(fr"(\b)(gje)({nis_me_gje})(\b)", r"gjë\3", t) ; e_subs += c
	## fjalë që nisin me Bë ; Germim -> Gërmim
	t, c = re.subn(fr"(\b)(Gje)({nis_me_gje})(\b)", r"Gjë\3", t) ; e_subs += c

	## fjalë që nisin me kë - keput -> këput
	t, c = re.subn(fr"(\b)(ke)({nis_me_ke})({prapa_0_7})(\b)", r"kë\3\4", t) ; e_subs += c
	## fjalë që nisin me Kë ; Kendoj -> Këndoj
	t, c = re.subn(fr"(\b)(Ke)({nis_me_ke})({prapa_0_7})(\b)", r"Kë\3\4", t) ; e_subs += c

	## fjalë që nisin me lë - leviz -> lëviz
	t, c = re.subn(fr"(\b)(le)({nis_me_le})({prapa_0_7})(\b)", r"lë\3\4", t) ; e_subs += c
	## fjalë që nisin me Lë ; Levizje -> Lëvizje
	t, c = re.subn(fr"(\b)(Le)({nis_me_le})({prapa_0_7})(\b)", r"Lë\3\4", t) ; e_subs += c

	## fjalë që nisin me llë - leviz -> lëviz
	t, c = re.subn(fr"(\b)(lle)({nis_me_lle})({prapa_0_12})(\b)", r"llë\3\4", t) ; e_subs += c
	## fjalë që nisin me Llë ; Levizje -> Lëvizje
	t, c = re.subn(fr"(\b)(Lle)({nis_me_lle})({prapa_0_12})(\b)", r"Llë\3\4", t) ; e_subs += c

	## fjalë që nisin me marrë - marreveshje -> marrëveshje
	t, c = re.subn(fr"(\b)(marre)({nis_me_marre})({prapa_0_5})(\b)", r"marrë\3\4", t) ; e_subs += c
	## fjalë që nisin me Marrë ; Marres -> Marrës
	t, c = re.subn(fr"(\b)(Marre)({nis_me_marre})({prapa_0_5})(\b)", r"Marrë\3\4", t) ; e_subs += c

	## fjalë që nisin me më - mesues -> mësues
	t, c = re.subn(fr"(\b)(me)({nis_me_me})({prapa_0_5})(\b)", r"më\3\4", t) ; e_subs += c
	## fjalë që nisin me Më ; Mesues -> Mësues
	t, c = re.subn(fr"(\b)(Me)({nis_me_me})({prapa_0_5})(\b)", r"Më\3\4", t) ; e_subs += c

	## fjalë që nisin me në - nensistem -> nënsistem
	t, c = re.subn(fr"(\b)(ne)({nis_me_ne})({prapa_0_12})(\b)", r"në\3\4", t) ; e_subs += c
	## fjalë që nisin me Në ; Nentor -> Nëntor
	t, c = re.subn(fr"(\b)(Ne)({nis_me_ne})({prapa_0_12})(\b)", r"Në\3\4", t) ; e_subs += c

	## fjalë që nisin me një - njekohshëm -> njëkohshëm
	t, c = re.subn(fr"(\b)(nje)({nis_me_nje})({prapa_0_7})(\b)", r"një\3\4", t) ; e_subs += c
	## fjalë që nisin me Një ; Njekohësi -> Njëkohësi
	t, c = re.subn(fr"(\b)(Nje)({nis_me_nje})({prapa_0_7})(\b)", r"Një\3\4", t) ; e_subs += c

	## fjalë që nisin me për - permend -> përmend
	t, c = re.subn(fr"(\b)(per)({nis_me_per_shper})({prapa_0_12})(\b)", r"për\3\4", t) ; e_subs += c
	## fjalë që nisin me Për ; Perdorimi -> Përdorimi
	t, c = re.subn(fr"(\b)(Per)({nis_me_per_shper})({prapa_0_12})(\b)", r"Për\3\4", t) ; e_subs += c

	## fjalë që nisin me shpër - shperhap -> shpërhap
	t, c = re.subn(fr"(\b)(shper)({nis_me_per_shper})({prapa_0_7})(\b)", r"shpër\3\4", t) ; e_subs += c
	## fjalë që nisin me Shpër ; Shperqendrim -> Shpërqendrim
	t, c = re.subn(fr"(\b)(Shper)({nis_me_per_shper})({prapa_0_7})(\b)", r"Shpër\3\4", t) ; e_subs += c

	## fjalë që nisin me rë - renie -> rënie
	t, c = re.subn(fr"(\b)(re)({nis_me_re})({prapa_0_7})(\b)", r"rë\3\4", t) ; e_subs += c
	## fjalë që nisin me Rë ; Rendësi -> Rëndësi
	t, c = re.subn(fr"(\b)(Re)({nis_me_re})({prapa_0_7})(\b)", r"Rë\3\4", t) ; e_subs += c

	## fjalë që nisin me rrë - rrekëllej -> rrëkëllej
	t, c = re.subn(fr"(\b)(rre)({nis_me_rre})({prapa_0_7})(\b)", r"rrë\3\4", t) ; e_subs += c
	## fjalë që nisin me Rrë ; Rrshqitje -> Rrëshqitje
	t, c = re.subn(fr"(\b)(Rre)({nis_me_rre})({prapa_0_7})(\b)", r"Rrë\3\4", t) ; e_subs += c

	## fjalë që nisin me së - semurë -> sëmurë
	t, c = re.subn(fr"(\b)(se)({nis_me_se})({prapa_0_7})(\b)", r"së\3\4", t) ; e_subs += c
	## fjalë që nisin me Së ; Semundje -> Sëmundje
	t, c = re.subn(fr"(\b)(Se)({nis_me_se})({prapa_0_7})(\b)", r"Së\3\4", t) ; e_subs += c

	## fjalë që nisin me së - sherbej -> shërbej
	t, c = re.subn(fr"(\b)(she)({nis_me_she})({prapa_0_7})(\b)", r"shë\3\4", t) ; e_subs += c
	## fjalë që nisin me Së ; Shendet -> Shëndet
	t, c = re.subn(fr"(\b)(She)({nis_me_she})({prapa_0_7})(\b)", r"Shë\3\4", t) ; e_subs += c

	## fjalë që nisin me të - terheq -> tërheq
	t, c = re.subn(fr"(\b)(te)({nis_me_te})({prapa_0_12})(\b)", r"të\3\4", t) ; e_subs += c
	## fjalë që nisin me Të ; Terheqja -> Tërheqja
	t, c = re.subn(fr"(\b)(Te)({nis_me_te})({prapa_0_12})(\b)", r"Të\3\4", t) ; e_subs += c

	## fjalë që nisin me vë - venie -> vënie
	t, c = re.subn(fr"(\b)(ve)({nis_me_ve})({prapa_0_7})(\b)", r"vë\3\4", t) ; e_subs += c
	## fjalë që nisin me Vë ; Vemendja -> Vëmendja
	t, c = re.subn(fr"(\b)(Ve)({nis_me_ve})({prapa_0_7})(\b)", r"Vë\3\4", t) ; e_subs += c

	return (t, e_subs, c_subs, tj_subs)


## fjalë që shkruhen me E/e në vend të Ë/ë-së te ndonjë prapashtesë 
def pa_e_prapa(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0

	## fjalë që mbarojnë me dhës ; hedhes -> hedhës
	t, c = re.subn(fr"(\b)({para_0_7})({fund_me_dhes})(dhes)({prapa_0_5})(\b)", r"\2\3dhës\5", t) ; e_subs += c

	## fjalë që mbarojnë me ëk ; pisllek -> pisllëk
	t, c = re.subn(fr"(\b)({fund_me_ek})(ek)({prapa_0_5})(\b)", r"\2ëk\4", t) ; e_subs += c

	## fjalë që mbarojnë me ëm ; hershem -> hershëm
	t, c = re.subn(fr"(\b)({fund_me_em})(em)({prapa_0_5})(\b)", r"\2ëm\4", t) ; e_subs += c

	## fjalë që mbarojnë me ër ; seder -> sedër
	t, c = re.subn(fr"(\b)({fund_me_er})(er)({prapa_0_5})(\b)", r"\2ër\4", t) ; e_subs += c

	## fjalë që përmbajnë ësi ; largesi -> largësi
	t, c = re.subn(fr"(\b)({fund_me_esi})(esi)({prapa_0_5})(\b)", r"\2ësi\4", t) ; e_subs += c

	## fjalë që përmbajnë ësor ; paqesor -> paqësor
	t, c = re.subn(fr"(\b)({fund_me_esor})(esor)({prapa_0_5})(\b)", r"\2ësor\4", t) ; e_subs += c

	## fjalë që përmbajnë ëror ; femeror -> femëror
	t, c = re.subn(fr"(\b)({fund_me_eror})(eror)({prapa_0_5})(\b)", r"\2ëror\4", t) ; e_subs += c

	## fjalë që mbarojnë me ësht ; qumesht -> qumësht 
	t, c = re.subn(fr"(\b)({fund_me_esht})(esht)({prapa_0_5})(\b)", r"\2ësht\4", t) ; e_subs += c

	## fjalë që përmbajnë ëtor ; shërbetor -> shërbëtor
	t, c = re.subn(fr"(\b)({fund_me_etor})(etor)({prapa_0_5})(\b)", r"\2ëtor\4", t) ; e_subs += c

	## gjithë fjalët që mbarojnë me SHËM - nuk ka fjalë me SHEM
	t, c = re.subn(fr"(\b)({para_1_12})(shem)(\b)", r"\2shëm\4", t) ; e_subs += c

	## gjithë fjalët që mbarojnë me SHMËRI - nuk ka fjalë me SHMERI
	t, c = re.subn(fr"(\b)({para_1_12})(shmeri)(\b)", r"\2shmëri\4", t) ; e_subs += c

	## fjalë që përmbajnë shtë ; kashte -> kashtë
	t, c = re.subn(fr"(\b)({fund_me_shte})(shte)({prapa_0_5})(\b)", r"\2shtë\4", t) ; e_subs += c

	return (t, e_subs, c_subs, tj_subs)


## funksion për zëvendësime e -> ë 
def redakto_e(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0
	
	## Është
	t, c = re.subn(fr"(\b)(E|Ë)(sht)(e|ë)?(\b)", r"Ë\3ë", t) ; e_subs += c
	## është
	t, c = re.subn(fr"(\b)(e|ë)(sht)(e|ë)?(\b)", r"ë\3ë", t) ; e_subs += c

	## problemet me ë-të fundore
	t, e_c, c_c, tj_c = pa_e_fundore(t)
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c

	## fjalët me e brenda para - mesoj -> mësoj
	t, e_c, c_c, tj_c = pa_e_para(t)
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c

	## fjalët me e brenda prapa - qumesht -> qumësht
	t, e_c, c_c, tj_c = pa_e_prapa(t)
	c_subs += c_c ; e_subs += e_c ; tj_subs += tj_c
	
	return (t, e_subs, c_subs, tj_subs)

