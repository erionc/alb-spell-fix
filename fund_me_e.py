
from percaktime import *

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
['ort', 'raj',],

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

## përgatitja e shprehjes së rregullt për zëvendësimin e e-së fundore me ë
with_e_exp = [] # # bashkësia e fjalëve më sipër
upp = string.ascii_uppercase.replace('W', '') # nistoret e mëdha
low = string.ascii_lowercase.replace('w', '') # nistoret e vogla

# bashkimi i nistoreve të mëdha e të vogla
initials = ['(' + upp[i] + '|' +  low[i] + ')' for i in range(0, 25)]

# bashkimi i nistoreve dhe fjalëve që fillojnë me secilën prej tyre
for i in range(0, 25):
	with_e_exp.extend(map((lambda x: initials[i] + x), with_e_end[i]))

# lidhja e fjalëve me operatorin | për formimin e shprehjes së rregullt
with_e_regex = '|'.join(with_e_exp)

## funksion për zëvendësime e -> ë 
def redakto_me_e(text):
	## velerënisje
	t = text ; e_subs = 0
	
	## fjalë që shkruhen me ë fundore të shkruar e -- maje -> majë
	t, c = re.subn(fr"(\b)({with_e_regex})(e)(\b)", r"\2ë", t) ; e_subs += c
	
	return (t, e_subs)
