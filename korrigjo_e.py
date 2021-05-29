
import re, string

## fjalë që shkruhen pa ë fundore ose me e në vend të saj -- mir(e) -> mirë
no_e_end = [
# a
['mplitud', 'naliz', 'rk', 'rn', 'rr'],
# b															
['alt', 'arn', 'ibliotek', 'im', 'oj', 'rek', 'ritm', 'ubullim', 'uk', 'uj'],
# c		
['ip'],
# d															
['ardh', 'at', 'eg', 'epozit', 'er', 'ig', 'isfat', 'ispozit', 'it',
'or', 'rejt', 'rit'],
# e
['kspedit', 'kspozit', 'n', 'r'],
# f								
['am', 'jal', 'lam', 'rik', 'urk', 'ush'],
# g													
['af', 'ar', 'jat', 'j(e|ë)m', 'jer', 'jell', 'jiz', 'ril', 'rop', 'un',],
# h
['apësir', 'er', 'ipotek', 'umb(e|ë)sir', 'umb(e|ë)tir', 'umner', 'urm'],
# i									
['j'],	
# j
['av', 'et'],	
# k																										
['afk', 'al', 'apic', 'arfic', '(e|ë)rthiz', 'lim', 'lithm', 'ov', 'urv'],	
# l								
['lim', 'ir', 'op', 'uft'],
# m											
['akin', 'ark', 'atric', 'ij', 'in', 'ir', 'iz', 'oll', 'uzik'], 
# n					
['aft', 'ap', 'djes', 'gjyr', 'inull', 'ism', 'j'],	
# o							
['rt', 'pozit'],		
# p								
['adrejt', 'ag', 'akic', 'em', '(e|ë)shtym', 'jeshk', 'levic', 'ozit',
'remis', 'rik', 'un', 'ushk'],
# q		
['ukm'],		
# r											
['(e|ë)r', 'imt', 'rug', 'rugic', 'rugin' ],
# s												
['fid', 'heg', 'hkreptim', 'hpejt', 'hpell', 'hum', 'humic', 'hqis', 
'htrenjt', 'intez', 'it', 'ob', 'tuf',],
# t
['han', 'ap', 'arg', 'hik', 'razir'],		
# u											
['j', 'n'],
# v												
['al', 'et(e|ë)tim', 'vezullim', 'iktim', 'il', 'jeg', 'ler', 'rim'],
# x								
['ix', 'hung'],	
# y														
['n', 'ndyr'],	
# z										
['an', 'gjyr', 'hdrejt', 'orr'],												
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
['mvis'],
# b															
[],
# c		
[],
# d															
[],
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
['aj', ], 
# n					
[],	
# o							
[],		
# p								
[],
# q		
['ep'],		
# r											
[],
# s												
[],
# t
[],		
# u											
[],
# v												
[],
# x								
[],	
# y														
[],	
# z										
[],												
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
def replace_e(text):
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

	
	