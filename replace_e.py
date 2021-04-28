
import re, string

## fjalë që shkruhen pa ë fundore ose me e në vend të saj - mir(e) -> mirë
no_e_end = [
['rr'],															# a
['ibliotek', 'im', 'rek', 'ritm', 'ubullim', 'uk', 'uj'],		# b
['ak'],															# c
['at', 'eg', 'epozit', 'isfat', 'ispozit', 'it', 'or', 'rejt', 			# d
'rit'],
['r', 'kspedit', 'kspozit'],									# e
['rik'],														# f
['jat', 'jell', 'ril', 'un',],									# g
['apësir', 'ipotek', 'urm'],									# h
['j'],															# i
['et'],															# j
['lim', 'ov'],													# k
['lim', 'ir', 'uft'],											# l
['atric', 'ij', 'ir', 'iz', 'oll', 'uzik'], 					# m
['gjyr', 'ism', 'j'],											# n
['rt', 'pozit'],												# o
['adrejt', 'akic', 'em', 'ozit', 'remis', 'rik', 'un'],			# p
['ukm'],														# q
['rug'],														# r
['fid', 'heg', 'hpejt', 'hpell', 'hum', 'humic', 'hqis', 		# s
'htrenjt', 'it'],
['hik'],														# t
['j', 'n'],														# u
['vezullim', 'iktim', 'il', 'rim'],								# v
['ix'],															# x
['n'],															# y
['an', 'hdrejt'],												# z
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

	
	