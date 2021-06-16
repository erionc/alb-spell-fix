
import re, string

## fjalë që shkruhen pa ë fundore ose me e në vend të saj -- mir(e) -> mirë
no_e_end = [
# a
['drenalin', 'jk', 'lbumin', 'm', 'meb', 'mplitud', 'naliz', 'ngjin', 'nilin',
'rk', 'rn', 'rr', 'spirin', 'tkin',],

# b															
['ab', 'ac', 'alt', 'altin', 'alerin', 'arn', 'enzin', 'ib', 'ibliotek',
'im', 'iskot', 'lac', 'obin', 'oj', 'otin', 'rek', 'ritm', 'ubullim', 'uj',
'ujtin', 'uk', 'ul', 'unac'],

# c		
['aher', 'ajk', 'apin', 'elin',],

# d															
['afin', 'ardh', 'at', 'eg', 'eltin', 'epozit', 'er', '(e|ë)llinj', 'h(e|ë)mball', 'hom',
'ig', 'isfat', 'isiplin', 'ispozit', 'it', 'jegurin', 'oktrin', 'or', 'ordolin', 'rejt', 'rit', 'uzin', 'ymb(e|ë)dhjet',],

# e
['kspedit', 'kspozit', 'n', 'r', 'rzin',],

# f								
['am', 'jal', 'lam', 'rik', 'und(e|ë)rin', 'urk', 'ush'],

# g													
['ab', 'abardin', 'af', 'alin', 'ar', 'ardalin', 'azolin', '(e|ë)lqerin',
'ijotin', 'jasht', 'jasht(e|ë)mb(e|ë)dhjet', 'jat', 'eraqin', 'j(e|ë)m',
'jer', 'jell', 'jithmon', 'jiz', 'licerin', 'lin', 'odin', 'oj', 'om',
'remin', 'rib', 'ril', 'rop', 'un', 'urgac'],

# h
['apësir', 'art', 'artin', 'emoglobin', 'er', 'ipotek', 'umb(e|ë)sir',
'umb(e|ë)tir', 'umner', 'und(e|ë)k(e|ë)rrab', 'und(e|ë)shkab', 'urm'],

# i									
['j'],	

# j
['av', 'et'],
	
# k																										
['abin', 'afk', 'afsh', 'al', 'alt(e|ë)rin', 'amin', 'anarin', 'anavac',
'antin', 'apic', 'aptin', 'arabin', 'arakatin', 'arfic', 'artolin', 'asht',
'at(e|ë)rmb(e|ë)dhjet', '(e|ë)rrab', '(e|ë)rthiz', 'inin', 'lim', 'lithm',
'lla(c|ç)', 'odrin', 'okain', 'olesterin', 'omodin', 'opertin', 'orac',
'ov', 'rahin', 'undrin', 'ungac', 'urv', 'ushtetut', 'uzhin',],
	
# l								
['açk', 'agazin', 'akin', 'argin', 'eckurin', 'ënd', '(e|ë)ndin', 'igatin',
'im', 'imurin', 'ir', 'lamarin', 'oj', 'op', 'uft', 'ugin',],

# m											
['akin', 'andarin', 'andolin', 'argarin', 'ark', 'art', 'artin', 'atric',
'ij', 'in', 'ir', 'iz', 'oll', 'orfin', 'uzik'], 

# n					
['aft', 'aftalin', 'ap', 'djes', '(e|ë)nt', '(e|ë)nt(e|ë)mb(e|ë)dhjet',
'gjyr', 'ikotin', 'inull', 'ism', 'itroglicerin', 'j', 'j(e|ë)mb(e|ë)dhjet',
],
	
# o							
['fi(c|ç)in', 'rigjin', 'rt', 'pozit'],	
	
# p								
['adrejt', 'ag', 'akic', 'arabim', 'aradhom', 'arafin', 'arakthin', 'arm',
'araman', 'armend', 'atin', 'elerin', 'em', 'en', 'end', 'enicilin', 'es',
'es(e|ë)mb(e|ë)dhjet', '(e|ë)shtym', 'in', 'ishin', 'jac', 'jeshk', 'lastelin',
'levic', 'ozit', 'rapashpin', 'redh', 'remis', 'rik', 'ron', 'rostitut',
'rotein', 'ul', 'un', 'ushk'],

# q		
['af(e|ë)k(e|ë)rrab', 'art', 'indark', 'uk(e|ë)lin', 'ukm'],	
	
# r											
['ac', '(e|ë)r', 'etin', 'ezolut', 'imt', 'rangallin', 'rep', 'rib', 'rob', 'ozmarin',
'rug', 'rugic', 'rugin', 'utin',],

# s												
['akarin', 'fid', 'fin', 'hakullin', 'heg', 'hib', 'hkab', 'hkarravin',
'hkat(e|ë)rrin', 'hkrab', 'hkreptim', 'hkresurin', 'hpartallin', 'hpejt',
'hpell', 'hport', 'hum', 'humic', 'hqis', 'htat', 'htat(e|ë)mb(e|ë)dhjet',
'htrenjt', 'intez', 'it', 'kilifac', 'kutin', 'ob', 'pin', 'terlin', 'tin',
'treptomicin', 'tuf', 'uferin', 'ulin', 'yprin',],

# t
['han', 'ap', 'arab', 'arg', 'arrac', 'avolin', 'et', 'et(e|ë)mb(e|ë)dhjet',
'etraciklin', 'hatin', 'hellin', 'hik', 'oksin', 'orb', 'rampolin', 'razir',
'remb(e|ë)dhjet', 'r(e|ë)ndelin', 'rin', 'urbin',],	
	
# u											
['j', 'l(ë|e)rim', 'n', 'zin'],

# v												
['aksin', 'al', 'azelin', 'et(e|ë)tim', 'vezullim', 'iktim', 'il',
'iolin', 'itamin', 'itrin', 'jeg', 'jeturin', 'ler', 'og(e|ë)lin', 'on',
'orb(e|ë)tin', 'rim'],

# x								
['helatin', 'hung', 'in', 'ix', ],	

# y														
['n', 'ndyr'],	

# z										
['an', 'gjyr', 'hab', 'hdrejt', 'jarrt', 'orr'],												
]

## përgatitja e shprehjes së rregullt për korrigjimin e ë-së fundore
no_e_exp = [] ; upp = string.ascii_uppercase.replace('W', '')
low = string.ascii_lowercase.replace('w', '')
initials = ['(' + upp[i] + '|' +  low[i] + ')' for i in range(0, 25)]
for i in range(0, 25):
	no_e_exp.extend(map((lambda x: initials[i] + x), no_e_end[i]))
no_e_regex = '|'.join(no_e_exp)

## fjalë që shkruhen me e fundore në vend të ë-së -- maje -> majë  
## duhet të zëvendësohen vetëm kur shfaqen me e në fund, pra 
## në shembullin më sipër nuk duhet të ngatërohet maje me maj (muaji)
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
['ac', 'lac', 'ug', 'yr'],

# m											
['aj', 'arin', 'beturin', 'jegullin', 'ushk'], 

# n					
['grehin', 'j(e|ë)zet'],	

# o							
[],		

# p								
['ort'],

# q		
['ep', 'ok',],	
	
# r											
['rafshin', 'rethin',],

# s												
['hin', 'hpatin', 'htat'],

# t
['aks', 'erin', 'errin', 'ulin',],	
	
# u											
['rin',],

# v												
[],

# x								
[],	

# y														
[],	

# z										
['gjedh',],												
]

## përgatitja e shprehjes së rregullt për zëvendësimin 
## e e-së fundore me ë
with_e_exp = [] ; upp = string.ascii_uppercase.replace('W', '')
low = string.ascii_lowercase.replace('w', '')
initials = ['(' + upp[i] + '|' +  low[i] + ')' for i in range(0, 25)]
for i in range(0, 25):
	with_e_exp.extend(map((lambda x: initials[i] + x), with_e_end[i]))
with_e_regex = '|'.join(with_e_exp)

## funksion për zëvendësime e -> ë 
def korrigjo_e(text):
	## velerënisje
	t = text ; e_subs = 0
	
	## Është
	t, c = re.subn(fr"(\b)(E|Ë)(sht)(e|ë)?(\b)", r"Ë\3ë", t) ; e_subs += c
	## është
	t, c = re.subn(fr"(\b)(e|ë)(sht)(e|ë)?(\b)", r"ë\3ë", t) ; e_subs += c
	
	## fjalë që shkruhen pa ë fundore ose me ë të shkruar e -- mir(e) -> mirë
	t, c = re.subn(fr"(\b)({no_e_regex})(e)?(\b)", r"\2ë", t) ; e_subs += c
	# t, c = re.subn(r"(Mir|mir)(e?)( |\.)", r"\1ë\3", t) ; e_subs += c

	## fjalë që shkruhen me ë fundore të shkruar e -- maje -> majë
	t, c = re.subn(fr"(\b)({with_e_regex})(e)(\b)", r"\2ë", t) ; e_subs += c
	# t, c = re.subn(r"(Mir|mir)(e?)( |\.)", r"\1ë\3", t) ; e_subs += c
	
	return (t, e_subs)

	
	