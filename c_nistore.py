
import re, string

## temat që shkruhen me C/c në vend të Ç/ç-së nistore
## ruhen prapashtesat ndaj nuk pranohen tema me grupe alternative me |
## cafk, caj, cajnik, canak, cibuk, cift, cimk, cmim, co, corap, cudi, cun, cup 
pa_c_nis = "afk|aj|ajnik|anak|akerdis|akmak|allm|arcaf|arçaf|art|ati|" + \
"ibuk|ift|imk|izme|" + \
"mend|mim|" + \
"o|orap|orodit|" + \
"udi|un"

	
	