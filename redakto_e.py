
import re, string

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
['aks', 'erin', 'errin', 'ulin',],	
	
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


## funksion për zëvendësime e -> ë 
def redakto_e(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, tj_subs = 0, 0, 0
	
	## Është
	t, c = re.subn(fr"(\b)(E|Ë)(sht)(e|ë)?(\b)", r"Ë\3ë", t) ; e_subs += c
	## është
	t, c = re.subn(fr"(\b)(e|ë)(sht)(e|ë)?(\b)", r"ë\3ë", t) ; e_subs += c
	
	## fjalë që shkruhen pa ë fundore ose me ë të shkruar e -- mir(e) -> mirë
	t, c = re.subn(fr"(\b)({no_e_regex})(e)?(\b)", r"\2ë", t) ; e_subs += c

	## fjalë që shkruhen me ë fundore të shkruar e -- maje -> majë
	t, c = re.subn(fr"(\b)({with_e_regex})(e)(\b)", r"\2ë", t) ; e_subs += c
	
	return (t, e_subs, c_subs, tj_subs)
