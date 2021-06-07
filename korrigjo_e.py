
import re, string

## fjalë që shkruhen pa ë fundore ose me e në vend të saj -- mir(e) -> mirë
no_e_end = [
# a
['jk', 'meb', 'mplitud', 'naliz', 'ngjin', 'rk', 'rn', 'rr', 'tkin',],

# b															
['alt', 'altin', 'arn', 'enzin', 'ibliotek', 'im', 'iskot', 'obin', 'oj',
'otin', 'rek', 'ritm', 'ubullim', 'uj', 'ujtin', 'uk', 'ul'],

# c		
['aher', 'ajk', 'apin', 'elin',],

# d															
['afin', 'ardh', 'at', 'eg', 'eltin', 'epozit', 'er', '(e|ë)llinj', 'h(e|ë)mball', 'hom',
'ig', 'isfat', 'ispozit', 'it', 'oktrin', 'or', 'rejt', 'rit', 'uzin', 'ymb(e|ë)dhjet',],

# e
['kspedit', 'kspozit', 'n', 'r', 'rzin',],

# f								
['am', 'jal', 'lam', 'rik', 'urk', 'ush'],

# g													
['af', 'ar', 'jasht', 'jasht(e|ë)mb(e|ë)dhjet', 'jat', 'j(e|ë)m', 'jer',
'jell', 'jithmon', 'jiz', 'lin', 'odin', 'oj', 'om', 'ril', 'rop', 'un',],

# h
['apësir', 'art', 'er', 'ipotek', 'umb(e|ë)sir', 'umb(e|ë)tir', 'umner', 'urm'],

# i									
['j'],	

# j
['av', 'et'],
	
# k																										
['afk', 'afsh', 'al', 'apic', 'arfic', 'asht', 'at(e|ë)rmb(e|ë)dhjet',
'(e|ë)rthiz', 'lim', 'lithm', 'ov', 'urv', 'ushtetut',],
	
# l								
['ënd', 'im', 'ir', 'oj', 'op', 'uft'],

# m											
['akin', 'ark', 'atric', 'ij', 'in', 'ir', 'iz', 'oll', 'uzik'], 

# n					
['aft', 'ap', 'djes', '(e|ë)nt', '(e|ë)nt(e|ë)mb(e|ë)dhjet', 'gjyr',
'inull', 'ism', 'j', 'j(e|ë)mb(e|ë)dhjet',
],
	
# o							
['rt', 'pozit'],	
	
# p								
['adrejt', 'ag', 'akic', 'arabim', 'arm', 'araman', 'armend', 'em', 'en',
'end', 'es', 'es(e|ë)mb(e|ë)dhjet', '(e|ë)shtym', 'in', 'jeshk', 'levic',
'ozit', 'redh', 'remis', 'rik', 'ron', 'rostitut', 'ul', 'un', 'ushk'],

# q		
['art', 'indark', 'ukm'],	
	
# r											
['(e|ë)r', 'ezolut', 'imt', 'rep', 'rob', 'rug', 'rugic', 'rugin' ],

# s												
['fid', 'fin', 'heg', 'hkreptim', 'hpejt', 'hpell', 'hport', 'hum', 'humic',
'hqis', 'htat', 'htat(e|ë)mb(e|ë)dhjet', 'htrenjt', 'intez', 'it', 'ob',
'pin', 'tin', 'tuf',],

# t
['han', 'ap', 'arg', 'et', 'et(e|ë)mb(e|ë)dhjet', 'hik', 'orb', 'razir',
'remb(e|ë)dhjet', 'rin'],	
	
# u											
['j', 'n'],

# v												
['al', 'et(e|ë)tim', 'vezullim', 'iktim', 'il', 'itamin', 'jeg', 'ler',
'on', 'rim'],

# x								
['hung', 'in', 'ix', ],	

# y														
['n', 'ndyr'],	

# z										
['an', 'gjyr', 'hdrejt', 'jarrt', 'orr'],												
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
[],

# h
[],

# i									
[],	

# j
[],	

# k																										
['am', 'ok'],
	
# l								
['ug', 'yr'],

# m											
['aj', 'ushk'], 

# n					
['j(e|ë)zet'],	

# o							
[],		

# p								
['ort'],

# q		
['ep', 'ok',],	
	
# r											
[],

# s												
['hin', 'htat'],

# t
['aks',],	
	
# u											
[],

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

	
	