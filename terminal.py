
import re, sys, argparse	# paketa të domosdoshme

# importimi i funksioneve korrigjuese nga modulet përkatëse
from redakto import *

## funksioni kryesor i korrigjimeve që thërret funksionet e tjera
def redaktime(in_text):
	# merret përmbajtja e kutizës së parë
	input_text = in_text
	t = input_text ; total_sub = 0
	
	## thirret funksioni kryesor i redaktimeve
	t, e_subs, c_subs, tj_subs = redakto(t)
	total_sub = c_subs + e_subs + tj_subs

	output_text = t
	
	# output_message = f"Zëvendësime të ë-ve:\t\t\t{e_subs}\n" + \
	# 	f"Zëvendësime të ç-ve:\t\t\t{c_subs}\n" + \
	# 	f"Zëvendësime të tjera:\t\t\t{tj_subs}\n" + \
	# 	f"Zëvendësime totale:\t\t\t{total_sub}"
	
	# shfaqet totali i zëvendësimeve të kryera
	output_message = f"Zëvendësime totale:\t{total_sub}\n"

	return output_text, output_message
	
# argumentet për ekzekutimin nga terminali
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Skedari Hyrës')
parser.add_argument('-o', '--output', help='Skedari Dalës')
args = parser.parse_args()

## pikënisja e ekzekutimit
if __name__ == "__main__":
	
	# nëse jepet edhe hyrja edhe dalja
	if args.input and args.output:
		# lexohet dhe përpunohet hyrja
		in_file = open(args.input, 'r')
		in_text = in_file.read()
		text, message = redaktime(in_text)
		in_file.close()
		
		# shkruhet dalja te skedari dalës
		out_file = open(args.output, 'w')
		out_file.write(text)
		in_file.close()
		print(f"\n{message}\n")
	
	# nëse jepet hyrja por jo dalja
	elif args.input and not args.output:
	
		# lexohet dhe përpunohet hyrja
		in_file = open(args.input, 'r')
		in_text = in_file.read()
		text, message = redaktime(in_text)
		in_file.close()
		
		# afishohet dalja te terminali
		print("\nTeksti dalës:\n", text)
		print(f"\n{message}\n")
	
	# nëse nuk jepen as hyrja as dalja
	elif not args.input and not args.output:
		# hyrja merret nga terminali
		in_text = input("\nTeksti hyrës:\n")
		text, message = redaktime(in_text)
		# dalja afishohet në terminal
		print(f"\nTeksti dalës:\n{text}")
		print(f"\n{message}\n")

	# komandë e shkruar gabim
	else:
		print("Komandë e shkruar gabim...")
		sys.exit(1)

