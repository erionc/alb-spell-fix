
''' Redaktime të ë-ve '''

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
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0

	## fjalë që shkruhen pa ë fundore ose me ë të shkruar e -- mir(e) -> mirë
	t, c = re.subn(fr"(\b)({no_e_regex})(e)?(\b)", r"\2ë", t) ; e_subs += c

	## fjalë që shkruhen me ë fundore të shkruar e -- maje -> majë
	t, c = re.subn(fr"(\b)({with_e_regex})(e)(\b)", r"\2ë", t) ; e_subs += c

	return (t, e_subs, c_subs, pj_subs, tj_subs)


## fjalë që nisin me BË por shpesh shkruhen me BE - beshtineë -> bështinë
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_be = "jme|jmë|jne|jnë|" + \
	"rtas|rtet|rtasim|rtasin|rtitje|rtitur|rthama|rthamat|rthame|rthamë|rthamor|rthamore|" + \
	"shem|shëm|shtaje|shtajë|shtinë"

## fjalë që nisin me DË por shpesh shkruhen me DE - dergoj -> dërgoj
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_de = "fre|fri|" + \
	"mt|" + \
	"ngl|nim|noj|nu|" + \
	"rge|rgi|rgo|rgu|" + \
	"shir|shp|sht"

## fjalë që nisin me DHË por shpesh shkruhen me DHE - e dhenë -> e dhënë
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_dhe = "mba|na|nd|ne|në"

## fjalë që nisin me FË por shpesh shkruhen me FE - femijë -> fëmijë
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_fe = "lli|mij|rge|rgo|rgë|rk|shf"

## fjalë që nisin me GË por shpesh shkruhen me GE - germoj -> gërmoj
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_ge = "l|" + \
	"rb|rm|rv|" + \
	"z"

## fjalë që nisin me GJË por shpesh shkruhen me GJE - gjemim -> gjëmim
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_gje = "mim|me\w{0,7}|më\w{0,7}|mo|ndër|ra|rat|send" 

## fjalë që nisin me KË por shpesh shkruhen me KE - keput -> këput
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_ke = "ll|" + \
	"mb|" + \
	"na|" + \
	"nd|" + \
	"ng|" + \
	"put|" + \
	"rc|rp|" + \
	"s|" + \
	"shill|sht|" + \
	"ta|te|ti|tu"

## fjalë që nisin me LË por shpesh shkruhen me LE - leviz -> lëviz
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_le = "kua|kun|kuq|kur|" + \
	"mi|" + \
	"ndim|ndo|" + \
	"pih|pij|pir" + \
	"shim|sho|shua|shue|" + \
	"viz|vroj"

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
	"ngë|nge\w|nyr|" + \
	"rga|rgi|rgo|rgu|" + \
	"shir|sim|sue"

## fjalë që nisin me NDËR por shpesh shkruhen me NDER - nderkombëtar -> ndërkombëtar
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_nder = "fu|ko|lidh|pr|ti|to|"

## fjalë që nisin me NË por shpesh shkruhen me NE - nensistem -> nënsistem
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_ne = "me|më|na|ne|në|ns|nto|pe|pë"

## fjalë që nisin me NJË por shpesh shkruhen me NJE - njekohshem -> njëkoshëm
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_nje = "ko|me|si|v"

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

## fjalë që nisin me QË por shpesh shkruhen me QE - qeroj -> qëroj
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_qe = "lli|llo|ndro|roh|roj|ron"

## fjalë që nisin me RË por shpesh shkruhen me RE - renie -> rënie
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_re = "ndes|ndë\w|nie" 

## fjalë që nisin me RRË por shpesh shkruhen me RRE - rrekëllej -> rrëkëllej
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_rre = "mbe|mo|mi|mu|nde|ndo|pir|shkate|shkatë|shq|zu" 

## fjalë që nisin me SË por shpesh shkruhen me SE - serish -> sërish
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_se = "mu|" + \
	"ke|" + \
	"ndu|" + \
	"pat|" + \
	"ris"

## fjalë që nisin me SHË por shpesh shkruhen me SHE - sheroj -> shëroj
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_she = "mt|nde|ndos|no|rbej|rben|rby|rim|ro|ru" 

## fjalë që nisin me TË por shpesh shkruhen me TE - veshtroj -> vështroj
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_te = "rh\w|rku\w|rth\w"

## fjalë që nisin me VË por shpesh shkruhen me VE - terheq -> tërheq
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_ve = "lli|men|nie|rda|rej|rsu|rtet|shtr|zhg"

## fjalë që nisin me ZË por shpesh shkruhen me ZE - zenkë -> zënkë
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
nis_me_ze = "ne|në|nke|nkë|ve|vë"


## fjalë që përmbajnë DHËS por shpesh shkruhen me DHES - paraardhes -> paraardhës
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_dhes = "Ar|ar|" + \
	"Dre|dre|" + \
	"He|he|" + \
	"Kre|kre|" + \
	"Mble|mble|" + \
	"Tre|tre|" + \
	"Vje|vje"

## fjalë që përmbajnë ËK por shpesh shkruhen me EK - pisllek -> pisllëk
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_ek = "Agall|agall|Avashll|avashll|" + \
	"Bejll|bejll|Beqarll|beqarll|Boll|boll|Budallall|budallall|" + \
	"Dembell|dembell|" + \
	"Fodull|fodull|Fukarall|fukarall|" + \
	"Gomarll|gomarll|" + \
	"Hamall|hamall|Haxhill|haxhill|Horrll|horrll|" + \
	"Jeshill|jeshill|" + \
	"Kapadaill|kapadaill|Karagjozll|karagjozll|Kapsll|kapsll|Krr|krr|" + \
	"Maskarall|maskarall|Matrapazll|matrapazll|" + \
	"Nikoqirll|nikoqirll|" + \
	"Pashall|pashall|Pazarll|pazarll|Pisll|pisll|" + \
	"Spiunll|spiunll|Synetll|synetll|" + \
	"Shejtanll|shejtanll|" + \
	"Tarafll|tarafll|Tersll|tersll|" + \
	"Xhamll|xhamll"

## fjalë që përmbajnë ËLL por shpesh shkruhen me ELL - majasell -> majasëll
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_ell = "Majas|majas"

## fjalë që përmbajnë ËM por shpesh shkruhen me EM - jashtem -> jashtëm
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_em = "fis|fund|" + \
	"jasht|" + \
	"Kalldr|kalldr|" + \
	"Llag|llag|" + \
	"moç|moc|" + \
	"pafund|" + \
	"Tak|tak"

## fjalë që përmbajnë ËQE por shpesh shkruhen me EQE - Pashalleqe -> Pashallëqe
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_eqe = "Agall|agall|Avashll|avashll|" + \
	"Bejll|bejll|Beqarll|beqarll|Boll|boll|Budallall|budallall|" + \
	"Dembell|dembell|" + \
	"Fodull|fodull|Fukarall|fukarall|" + \
	"Gomarll|gomarll|" + \
	"Hamall|hamall|Haxhill|haxhill|Horll|horll|" + \
	"Jeshill|jeshill|" + \
	"Kapadaill|kapadaill|Karagjozll|karagjozll|Kapsll|kapsll|Krr|krr|" + \
	"Maskarall|maskarall|Matrapazll|matrapazll|" + \
	"Nikoqirll|nikoqirll|" + \
	"Pashall|pashall|Pazarll|pazarll|Pisll|pisll|" + \
	"Spiunll|spiunll|Synetll|synetll|" + \
	"Shejtanll|shejtanll|" + \
	"Tarafll|tarafll|Tersll|tersll|" + \
	"Xhamll|xhamll"

## fjalë që përmbajnë ËR por shpesh shkruhen me ER - seder -> sedër
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_er = "Ashp|ashp|" + \
	"Fëmij|Femij|fëmij|femij|" + \
	"Hasm|hasm|Hat|hat|" + \
	"Kat|kat|Ket|ket|Kod|kod|" + \
	"Lak|lak|Last|last|Let|let|Lib|lib|Lod|lod|" + \
	"Mbret|mbret|Met|\w{0,7}met|Mjed|mjed|Mjesht|mjesht|Mot|mot|" + \
	"Orkest|orkest|" + \
	"Pjep|pjep|Posht|posht|" + \
	"Qend|qend|" + \
	"Sed|sed|Skllev|skllev|Shtret|shtret|Shqip|Sof|sof|" + \
	"Teat|teat|Tjet|tjet|Thjesht|Thjesht|" + \
	"Varf|varf|Vat|vat|Vjet|vjet"

## fjalë që përmbajnë ËROR por shpesh shkruhen me EROR - femeror -> femëror
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_eror = "Burr|burr|" + \
	"Fem|fem|Fëmij|fëmij|Femij|femij|" + \
	"Kafsh|kafsh|" + \
	"Vëllaz|vëllaz|Vellaz|vellaz"

## fjalë që përmbajnë ËRSI por shpesh shkruhen me ERSI - kaltersi -> kaltërsi
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_ersi = "Çilt|çilt|Kalt|kalt|Vjet|vjet"

## fjalë që përmbajnë ËSI por shpesh shkruhen me ESI - largesi -> largësi
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_esi = "Aft|aft|An|an|Armiq|armiq|At|at|" + \
	"Bardh|bardh|But|but|" + \
	"Drejt|drejt|" + \
	"Fort|fort|Ftoht|ftoht|" + \
	"Gjat|gjat|Gjer|gjer|Fshatar|fshatar|" + \
	"Kenaq|kenaq|Kënaq|kënaq|Kot|kot|Krip|krip|" + \
	"Larg|larg|Lart|lart|Lasht|lasht|Leht|leht|" + \
	"Madh|madh|Mend|mend|Mëm|mëm|Miq|miq|Mir|mir|Mjek|mjek|" + \
	"Ngroht|ngroht|Nxeht|nxeht|" + \
	"Pjerr|pjerr|Pron|pron|" + \
	"Qart|qart|" + \
	"Rast|rast|Rënd|rënd|Rend|rend|" + \
	"Shëndet|shëndet|Shendet|shendet|Shpejt|shpejt|" + \
	"Thjesht|thjesht|" + \
	"Var|var|Verdh|verdh|Vërtet|vërtet|Vertet|vertet|Vrazhd|vrazhd|" + \
	"Zhdërvjell|zhdërvjell"

## fjalë që përmbajnë ËSO por shpesh shkruhen me ESO - puneso -> punëso
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_eso = "Pun|pun|Hamend|hamend|Armiq|armiq|Jet|jet"

## fjalë që përmbajnë ËSOR por shpesh shkruhen me ESOR - rastesor -> rastësor
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_esor = "Armiq|armiq|Jet|jet|Paq|paq|Rast|rast|Shkak|shkak"

## fjalë që përmbajnë SHTË por shpesh shkruhen me SHTE - kreshte -> kreshtë
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_shte = "Ava|ava|" + \
	"Bri|bri|" + \
	"Fildi|fildi|" + \
	"Gja|gja|" + \
	"He|he|" + \
	"Ja|ja|" + \
	"Ka|ka|Kre|kre|" + \
	"La|la|Le|le|" + \
	"Mbrap|mbrap|Mef|mef|" + \
	"Ngu|ngu|" + \
	"Po|po|" + \
	"She|she|Shpe|shpe|" + \
	"Thje|thje|Tri|tri|" + \
	"U|u|" + \
	"Vje|vje"

## fjalë që përmbajnë ËSHT por shpesh shkruhen me ESHT - qumesht -> qumësht
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_esht = "Lag|lag|" + \
	"Plog|plog|" + \
	"Qum|qum"

## fjalë që përmbajnë ËTI por shpesh shkruhen me ETI - pipetij -> pipëtij
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_eti = "Pip|pip|Vet|vet"

## fjalë që përmbajnë ËTOR por shpesh shkruhen me ETOR - shërbetor -> shërbëtor
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
fund_me_etor = "Pun|pun|Shërb|shërb|Sherb|sherb"

## sasior - dyja treja trija gjithë gjitha
sasior = "dy|tre|tri|katër|pes|gjith|paktën|shumtën"


## fjalë që shkruhen me E/e në vend të Ë/ë-së te ndonjë parashtesë
def pa_e_para(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0

	## fjalë që nisin me Bë/bë - bejmë -> bëjmë ; Beshtinë -> Bështinë
	t, c = re.subn(fr"(\b)(B|b)(e)({nis_me_be})(\b)", r"\2ë\4", t) ; e_subs += c

	## fjalë që nisin me Dë/dë - dergoj -> dërgoj ; Deshpërim -> Dëshpërim
	t, c = re.subn(fr"(\b)(D|d)(e)({nis_me_de})({albprapa_1_12})(\b)", r"\2ë\4\5", t) ; e_subs += c

	## fjalë që nisin me Dhë/dhë - e dhenë -> e dhënë ; Dhendër -> Dhëndër
	t, c = re.subn(fr"(\b)(D|d)(he)({nis_me_dhe})({albprapa_0_7})(\b)", r"\2hë\4\5", t) ; e_subs += c

	## fjalë që nisin me Fë/fë - ferkoj -> fërkoj ; Femijëri -> Fëmijëri
	t, c = re.subn(fr"(\b)(F|f)(e)({nis_me_fe})({albprapa_0_12})(\b)", r"\2ë\4\5", t) ; e_subs += c

	## fjalë që nisin me Gë/gë - germoj -> gërmoj ; Germim -> Gërmim
	t, c = re.subn(fr"(\b)(G|g)(e)({nis_me_ge})({albprapa_0_12})(\b)", r"\2ë\4\5", t) ; e_subs += c

	## fjalë që nisin me Gjë/gjë - gjera -> gjëra ; Gjendër -> Gjëndër
	t, c = re.subn(fr"(\b)(G|g)(je)({nis_me_gje})(\b)", r"\2jë\4", t) ; e_subs += c

	## fjalë që nisin me Kë/kë - keput -> këput ; Kendoj -> Këndoj
	t, c = re.subn(fr"(\b)(K|k)(e)({nis_me_ke})({albprapa_0_7})(\b)", r"\2ë\4\5", t) ; e_subs += c

	## fjalë që nisin me Lë/lë - leviz -> lëviz ; Levizje -> Lëvizje
	t, c = re.subn(fr"(\b)(L|l)(e)({nis_me_le})({albprapa_0_7})(\b)", r"\2ë\4\5", t) ; e_subs += c

	## fjalë që nisin me Llë/llë - leviz -> lëviz ; Levizje -> Lëvizje
	t, c = re.subn(fr"(\b)(L|l)(le)({nis_me_lle})({albprapa_0_12})(\b)", r"\2lë\4\5", t) ; e_subs += c

	## fjalë që nisin me Marrë/marrë - marreveshje -> marrëveshje ; Marres -> Marrës
	t, c = re.subn(fr"(\b)(M|m)(arre)({nis_me_marre})({albprapa_0_5})(\b)", r"\2arrë\4\5", t) ; e_subs += c

	## fjalë që nisin me Më/më - mesoj -> mësoj ; Mesues -> Mësues
	t, c = re.subn(fr"(\b)(M|m)(e)({nis_me_me})({albprapa_0_5})(\b)", r"\2ë\4\5", t) ; e_subs += c

	## fjalë që nisin me Në/në - nensistem -> nënsistem ; Nentor -> Nëntor
	t, c = re.subn(fr"(\b)(N|n)(e)({nis_me_ne})({albprapa_1_12})(\b)", r"\2ë\4\5", t) ; e_subs += c

	## fjalë që nisin me Ndër/ndër - ndertoj -> ndërtoj ; Nderkombësi -> Ndërkombësi
	t, c = re.subn(fr"(\b)(N|n)(der)({nis_me_nder})({albprapa_1_12})(\b)", r"\2dër\4\5", t) ; e_subs += c

	## fjalë që nisin me Një/një - njekohshëm -> njëkohshëm ; Njekohësi -> Njëkohësi
	t, c = re.subn(fr"(\b)(N|n)(je)({nis_me_nje})({albprapa_0_7})(\b)", r"\2jë\4\5", t) ; e_subs += c

	## fjalë që nisin me Për/për - permend -> përmend ; Perdorimi -> Përdorimi
	t, c = re.subn(fr"(\b)(P|p)(er)({nis_me_per_shper})({albprapa_0_12})(\b)", r"\2ër\4\5", t) ; e_subs += c

	## fjalë që nisin me Shpër/shpër - shperhap -> shpërhap ; Shperqendrim -> Shpërqendrim
	t, c = re.subn(fr"(\b)(S|s)(hper)({nis_me_per_shper})({albprapa_0_7})(\b)", r"\2hpër\4\5", t) ; e_subs += c

	## fjalë që nisin me Që/që - qeroj -> qëroj ; Qellim -> Qëllim
	t, c = re.subn(fr"(\b)(Q|q)(e)({nis_me_qe})({albprapa_0_12})(\b)", r"\2ë\4\5", t) ; e_subs += c

	## fjalë që nisin me Rë/rë - renie -> rënie ; Rendësi -> Rëndësi
	t, c = re.subn(fr"(\b)(R|r)(e)({nis_me_re})({albprapa_0_7})(\b)", r"\2ë\4\5", t) ; e_subs += c

	## fjalë që nisin me Rrë/rrë - rrekëllej -> rrëkëllej ; Rrshqitje -> Rrëshqitje
	t, c = re.subn(fr"(\b)(R|r)(re)({nis_me_rre})({albprapa_0_7})(\b)", r"\2rë\4\5", t) ; e_subs += c

	## fjalë që nisin me Së/së - semurë -> sëmurë ; Semundje -> Sëmundje
	t, c = re.subn(fr"(\b)(S|s)(e)({nis_me_se})({albprapa_0_7})(\b)", r"\2ë\4\5", t) ; e_subs += c

	## fjalë që nisin me Shë/shë - sherbej -> shërbej ; Shendet -> Shëndet
	t, c = re.subn(fr"(\b)(S|s)(he)({nis_me_she})({albprapa_0_7})(\b)", r"\2hë\4\5", t) ; e_subs += c

	## fjalë që nisin me Të/të - terheq -> tërheq ; Terheqja -> Tërheqja
	t, c = re.subn(fr"(\b)(T|t)(e)({nis_me_te})({albprapa_0_12})(\b)", r"\2ë\4\5", t) ; e_subs += c

	## fjalë që nisin me Vë/vë - venie -> vënie ; Vemendja -> Vëmendja
	t, c = re.subn(fr"(\b)(V|v)(e)({nis_me_ve})({albprapa_0_7})(\b)", r"\2ë\4\5", t) ; e_subs += c

	## fjalë që nisin me Zë/zë - zenkë -> zënke ; Zevendësim -> Zëvendësim
	t, c = re.subn(fr"(\b)(Z|z)(e)({nis_me_ze})({albprapa_0_12})(\b)", r"\2ë\4\5", t) ; e_subs += c

	return (t, e_subs, c_subs, pj_subs, tj_subs)


## fjalë që shkruhen me E/e në vend të Ë/ë-së te ndonjë prapashtesë 
def pa_e_prapa(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0

	## fjalë që mbarojnë me dhës ; hedhes -> hedhës
	t, c = re.subn(fr"(\b)({albpara_0_7})({fund_me_dhes})(dhes)({albprapa_0_5})(\b)", r"\2\3dhës\5", t) ; e_subs += c

	## fjalë që mbarojnë me ëk ; pisllek -> pisllëk
	t, c = re.subn(fr"(\b)({fund_me_ek})(ek)({albprapa_0_5})(\b)", r"\2ëk\4", t) ; e_subs += c

	## fjalë që mbarojnë me ëll ; majasell -> majasëll
	t, c = re.subn(fr"(\b)({fund_me_ell})(ell)({albprapa_0_5})(\b)", r"\2ëll\4", t) ; e_subs += c

	## fjalë që mbarojnë me ëm ; hershem -> hershëm
	t, c = re.subn(fr"(\b)({fund_me_em})(em)({albprapa_0_5})(\b)", r"\2ëm\4", t) ; e_subs += c

	## fjalë që mbarojnë me ëqe ; Pashalleqe -> Pashallëqe
	t, c = re.subn(fr"(\b)({fund_me_eqe})(eqe)({albprapa_0_5})(\b)", r"\2ëqe\4", t) ; e_subs += c

	## fjalë që mbarojnë me ër ; seder -> sedër
	t, c = re.subn(fr"(\b)({fund_me_er})(er)({albprapa_0_5})(\b)", r"\2ër\4", t) ; e_subs += c

	## fjalë që përmbajnë ërsi ; kaltersi -> kaltërsi
	t, c = re.subn(fr"(\b)({fund_me_ersi})(ersi)({albprapa_0_5})(\b)", r"\2ërsi\4", t) ; e_subs += c

	## fjalë që përmbajnë ësi ; largesi -> largësi
	t, c = re.subn(fr"(\b)(Pa|pa)?({fund_me_esi})(esi)({albprapa_0_5})(\b)", r"\2\3ësi\5", t) ; e_subs += c

	## fjalë që përmbajnë ëso ; puneso -> punëso
	t, c = re.subn(fr"(\b)({fund_me_eso})(eso)({albprapa_1_5})(\b)", r"\2ëso\4", t) ; e_subs += c

	## fjalë që përmbajnë ësor ; paqesor -> paqësor
	t, c = re.subn(fr"(\b)({fund_me_esor})(esor)({albprapa_0_5})(\b)", r"\2ësor\4", t) ; e_subs += c

	## fjalë që përmbajnë ëror ; femeror -> femëror
	t, c = re.subn(fr"(\b)({fund_me_eror})(eror)({albprapa_0_5})(\b)", r"\2ëror\4", t) ; e_subs += c

	## fjalë që mbarojnë me ësht ; qumesht -> qumësht 
	t, c = re.subn(fr"(\b)({fund_me_esht})(esht)({albprapa_0_5})(\b)", r"\2ësht\4", t) ; e_subs += c

	## fjalë që përmbajnë ëti ; pipetij -> pipëtij
	t, c = re.subn(fr"(\b)({fund_me_eti})(eti)({albprapa_0_5})(\b)", r"\2ëti\4", t) ; e_subs += c

	## fjalë që përmbajnë ëtor ; shërbetor -> shërbëtor
	t, c = re.subn(fr"(\b)({fund_me_etor})(etor)({albprapa_0_5})(\b)", r"\2ëtor\4", t) ; e_subs += c

	## gjithë fjalët që mbarojnë me SHËM - nuk ka fjalë me SHEM
	t, c = re.subn(fr"(\b)({albpara_1_12})(shem)(\b)", r"\2shëm", t) ; e_subs += c

	## gjithë fjalë që mbarojnë me AJTËS - nuk ka fjalë me AJTES
	t, c = re.subn(fr"(\b)({albpara_1_12})(ajtes)(\w?)(\b)", r"\2ajtës\4", t) ; e_subs += c

	## gjithë fjalët që mbarojnë me SHMËRI - nuk ka fjalë me SHMERI
	t, c = re.subn(fr"(\b)({albpara_1_12})(shmeri)(\b)", r"\2shmëri\4", t) ; e_subs += c

	## fjalë që përmbajnë shtë ; kashte -> kashtë
	t, c = re.subn(fr"(\b)({fund_me_shte})(shte)({albprapa_0_12})(\b)", r"\2shtë\4", t) ; e_subs += c

	return (t, e_subs, c_subs, pj_subs, tj_subs)


## funksion për zëvendësime e -> ë 
def redakto_e(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0
	
	## Është
	t, c = re.subn(fr"(\b)(E|Ë)(sht)(e|ë)?(\b)", r"Ë\3ë", t) ; e_subs += c
	## është
	t, c = re.subn(fr"(\b)(e|ë)(sht)(e|ë)?(\b)", r"ë\3ë", t) ; e_subs += c

	## të të + folje - te te them -> të të them
	t, c = re.subn(fr"(\b)(te |të )(te |të )({folje_zgj_1}|{folje_zgj_2}|{folje_zgj_3})({albprapa_0_3})(\b)", r"të të \4\5", t) ; e_subs += c

	## te të + sasior - te te dyja -> te të dyja
	t, c = re.subn(fr"(\b)(te |të )(te |të )({sasior})({albprapa_0_3})(\b)", r"te të \4\5", t) ; e_subs += c

	## problemet me ë-të fundore
	t, e_c, c_c, p_c, tj_c = pa_e_fundore(t)
	c_subs += c_c ; e_subs += e_c ; pj_subs += p_c ; tj_subs += tj_c

	## fjalët me e brenda para - mesoj -> mësoj
	t, e_c, c_c, p_c, tj_c = pa_e_para(t)
	c_subs += c_c ; e_subs += e_c ; pj_subs += p_c ; tj_subs += tj_c

	## fjalët me e brenda prapa - qumesht -> qumësht
	t, e_c, c_c, p_c, tj_c = pa_e_prapa(t)
	c_subs += c_c ; e_subs += e_c ; pj_subs += p_c ; tj_subs += tj_c
	
	return (t, e_subs, c_subs, pj_subs, tj_subs)
