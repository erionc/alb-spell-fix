import re
# importimi i funksioneve korrigjuese nga modulet përkatëse
from korrigjo import *
from korrigjo_pj import *
from korrigjo_e import *
from korrigjo_c import *

## funksioni kryesor i korrigjimeve që thërret funksionet e tjera
def redaktime(field_in):
	# merret përmbajtja e kutizës së parë
	input_text = field_in
	t = input_text ; total_sub = 0
	
	# thirren zëvendësimet paraprake
	t, c = para_korrigjime(t) ; total_sub += c
		
	# thirren zëvendësimet e e-së
	t, c = korrigjo_e(t) ; total_sub += c
	
	# thirren zëvendësimet e c-së
	t, c = korrigjo_c(t) ; total_sub += c
	
	# thirren zëvendësimet e pjesoreve
	t, c = korrigjo_pjes(t) ; total_sub += c
	
	# thirren zëvendësime e fjalëve
	t, c = korrigjo_terma(t) ; total_sub += c
	
	# thirren zëvendësime e fjalëve angleze
	t, c = korrigjo_eng(t) ; total_sub += c
	
	# thirren zëvendësimet përfundimtare
	t, c = pas_korrigjime(t) ; total_sub += c

	output_text = t
	
	# shfaqet totali i zëvendësimeve të kryera
	if total_sub == 1:
		output_message = str.format("{} zëvendësim. ", total_sub)
	else:
		output_message = str.format("{} zëvendësime. ", total_sub)

	return output_text, output_message

## pikënisja e ekzekutimit
if __name__ == "__main__":
	text1_field = input("\nTeksti hyrës:\n")
	text, message = redaktime(text1_field)

	print("\nTeksti dalës:\n", text)
	print(f"\n{message}\n")

