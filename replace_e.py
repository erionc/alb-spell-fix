
import re, string

## fjalë që shkruhen pa ë fundore ose me e në vend të saj - mir(e) -> mirë
no_e_end = [
['rr'],											# a
['uk', 'uj', 'im'],								# b
['ak'],											# c
['it', 'or'],									# d
['r'],											# e
['rik'],										# f
['un', 'jell', 'ril'],							# g
['apësir', 'urm'],								# h
['j'],											# i
['et'],											# j
['lim', 'ov'],									# k
['ir', 'uft'],									# l
['atric', 'ij', 'ir', 'oll', 					# m
'uzik'],
['gjyr', 'ism', 'j'],							# n
['rt'],											# o
['akic', 'em', 'remis', 'un'],					# p
['ukm'],										# q
['rug'],										# r
['fid', 'hum', 'humic', 'hqis', 'htrenjt'],		# s
['hik'],										# t
['j', 'n'],										# u
['iktim', 'il', 'rim'],							# v
['ix'],											# x
['n'],											# y
['an'],											# z
]

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

	
	