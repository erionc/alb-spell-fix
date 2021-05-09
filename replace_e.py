
import re, string

## fjalë që shkruhen pa ë fundore ose me e në vend të saj - mir(e) -> mirë
no_e_end = [
# a
['rk', 'rn', 'rr'],
# b															
['alt', 'arn', 'ibliotek', 'im', 'rek', 'ritm', 'ubullim', 'uk', 'uj'],
# c		
['ip'],
# d															
['ardh', 'at', 'eg', 'epozit', 'isfat', 'ispozit', 'it', 'or', 'rejt', 'rit'],
# e
['r', 'kspedit', 'kspozit'],
# f								
['am', 'rik'],
# g													
['jat', 'jell', 'ril', 'un',],
# h
['apësir', 'ipotek', 'urm'],
# i									
['j'],	
# j
['av', 'et'],	
# k																										
['lim', 'lithm', 'ov'],	
# l								
['lim', 'ir', 'uft'],
# m											
['ark', 'atric', 'ij', 'ir', 'iz', 'oll', 'uzik'], 
# n					
['aft', 'gjyr', 'ism', 'j'],	
# o							
['rt', 'pozit'],		
# p								
['adrejt', 'ag', 'akic', 'em', 'jeshk', 'ozit', 'remis', 'rik', 'un', 'ushk'],
# q		
['ukm'],		
# r											
['rug', 'imt'],
# s												
['fid', 'heg', 'hpejt', 'hpell', 'hum', 'humic', 'hqis', 'htrenjt', 'it'],
# t
['ap', 'arg', 'hik'],		
# u											
['j', 'n'],
# v												
['al', 'vezullim', 'iktim', 'il', 'rim'],
# x								
['ix', 'hung'],	
# y														
['n'],	
# z										
['an', 'hdrejt', 'orr'],												
]

## preparing the e replacement regular expression
no_e_exp = [] ; upp = string.ascii_uppercase.replace('W', '')
low = string.ascii_lowercase.replace('w', '')
initials = ['(' + upp[i] + '|' +  low[i] + ')' for i in range(0, 25)]
for i in range(0, 25):
	no_e_exp.extend(map((lambda x: initials[i] + x), no_e_end[i]))
no_e_regex = '|'.join(no_e_exp)

## function for e -> ë substitutions
def replace_e(text):
	## initializations 
	t = text ; e_subs = 0
	
	## Është
	t, c = re.subn(fr"(\b)(E|Ë)(sht)(e|ë)?(\b)", r"Ë\3ë", t) ; e_subs += c
	## është
	t, c = re.subn(fr"(\b)(e|ë)(sht)(e|ë)?(\b)", r"ë\3ë", t) ; e_subs += c
	
	## fjalë që shkruhen pa ë fundore ose me ë të shkruar e - mir(e) -> mirë
	t, c = re.subn(fr"(\b)({no_e_regex})(e)?(\b)", r"\2ë", t) ; e_subs += c
	# t, c = re.subn(r"(Mir|mir)(e?)( |\.)", r"\1ë\3", t) ; e_subs += c
	
	return (t, e_subs)

	
	