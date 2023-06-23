
from percaktime import *


## XH -> GJ
def permban_gj(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0

	## dixhital -> digjital
	t, c = re.subn(fr"(\b)(Di|di)(xh)(ital)({albprapa_0_5})(\b)", r"\2gj\4\5", t) ; tj_subs += c 

	## axhendë -> agjendë
	t, c = re.subn(fr"(\b)(A|a)(xh)(end)({albprapa_0_5})(\b)", r"\2gj\4\5", t) ; tj_subs += c 

	## axhenci -> agjenci
	t, c = re.subn(fr"(\b)(A|a)(xh|gj)(en)(c|s)({albprapa_0_5})(\b)", r"\2gj\4c\6", t) ; tj_subs += c 

	## tangent -> tangjent
	t, c = re.subn(fr"(\b)(Tan|tan)(g|xh)(ent)({albprapa_0_5})(\b)", r"\2gj\4\5", t) ; tj_subs += c 

	## xhiraf -> gjiraf
	t, c = re.subn(fr"(\b)(Xh|Zh)(iraf)({albprapa_0_5})(\b)", r"Gj\3\4", t) ; tj_subs += c 
	t, c = re.subn(fr"(\b)(xh|zh)(iraf)({albprapa_0_5})(\b)", r"gj\3\4", t) ; tj_subs += c 

	## genetik -> gjenetik
	t, c = re.subn(fr"(\b)(G)(enetik)({albprapa_0_5})(\b)", r"Gj\3\4", t) ; tj_subs += c 
	t, c = re.subn(fr"(\b)(g)(enetik)({albprapa_0_5})(\b)", r"gj\3\4", t) ; tj_subs += c 

	## genocid -> gjenocid
	t, c = re.subn(fr"(\b)(G)(enocid)({albprapa_0_5})(\b)", r"Gj\3\4", t) ; tj_subs += c 
	t, c = re.subn(fr"(\b)(g)(enocid)({albprapa_0_5})(\b)", r"gj\3\4", t) ; tj_subs += c 

	return (t, e_subs, c_subs, pj_subs, tj_subs)


## funksion për shqipërime
def shqiperime(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0

	## kthimi i pikës në presje dhjetore 0.345 -> 0,345 ; 3.6e6 -> 3,6e6 ; -34.4e-4 -> -34,4e-4
	t, c = re.subn(fr"(\b)([-+]?)([0-9]*)(\.)([0-9]+)([eE][-+]?[0-9]+)?(\b)", r"\2\3,\5\6", t) ; 
	## shprehja e mëposhtëme zëvendëson edhe numrat e shkruar në formën .345 -> ,345
	# t, c = re.subn(fr"([-+]?)([0-9]*)(\.)([0-9]+)([eE][-+]?[0-9]+)?(\b)", r"\1\2,\4\5", t)
	tj_subs += c 

	## XH -> GJ
	t, e_c, c_c, p_c, tj_c = permban_gj(t)
	c_subs += c_c ; e_subs += e_c ; pj_subs =+ p_c ; tj_subs += tj_c
	
	return (t, e_subs, c_subs, pj_subs, tj_subs)


## funksion për zëvendësimin e fjalëve angleze 
def perkthime(text):
	## vlerënisje 
	t = text ; c_subs, e_subs, pj_subs, tj_subs = 0, 0, 0, 0

	## link -> lidhje ; Hyperlink -> Hiperlidhje
	t, c = re.subn(fr"(\b)({albpara_0_5})(L|l)(ink)(\b)", r"\2\3idhje", t) ; tj_subs += c 
	t, c = re.subn(fr"(\b)({albpara_0_5})(L|l)(inku)(\b)", r"\2\3idhja", t) ; tj_subs += c 
	t, c = re.subn(fr"(\b)({albpara_0_5})(L|l)(ink|inq)(e|et)(\b)", r"\2\3idhj\5", t) ; tj_subs += c 

	## text -> tekst ; Hypertext -> Hipertekst
	t, c = re.subn(fr"(\b)({albpara_0_5})(T|t)(ext)(\b)", r"\2\3ekst", t) ; tj_subs += c 
	t, c = re.subn(fr"(\b)({albpara_0_5})(T|t)(exti)(\b)", r"\2\3eksti", t) ; tj_subs += c 
	t, c = re.subn(fr"(\b)({albpara_0_5})(T|t)(exte|extet)(\b)", r"\2\3ekste\5", t) ; tj_subs += c 

	return (t, e_subs, c_subs, pj_subs, tj_subs)