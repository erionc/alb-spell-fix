
import re, string

## fjalë që shkruhen pa ë fundore ose me e në vend të saj - mir(e) -> mirë
no_e_end = [
['rr'],															# a
['ubullim', 'uk', 'uj', 'im', 'ritm'],							# b
['ak'],															# c
['epozit', 'ispozit', 'it', 'or', 'rejt', 'rit'],				# d
['r', 'ekspedit', 'kspozit'],									# e
['rik'],														# f
['un', 'jell', 'ril'],											# g
['apësir', 'urm'],												# h
['j'],															# i
['et'],															# j
['lim', 'ov'],													# k
['lim', 'ir', 'uft'],											# l
['atric', 'ij', 'ir', 'oll', 'uzik'], 							# m
['gjyr', 'ism', 'j'],											# n
['rt', 'pozit'],												# o
['adrejt', 'akic', 'em', 'ozit', 'remis', 'un'],				# p
['ukm'],														# q
['rug'],														# r
['fid', 'hpejt', 'hum', 'humic', 'hqis', 'htrenjt', 			# s
'it'],
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

	
	