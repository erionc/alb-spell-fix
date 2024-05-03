
'''
timecl python terminal.py -c -i ./tmp/6000ht.txt -o /dev/null
Korrigjime totale:      2819
Runtime: 53.789 seconds
...
timecl python terminal.py -c -i ./tmp/9000hmt.txt -o /dev/null
Korrigjime totale:      4991
Runtime: 90.739 seconds
...
timecl python terminal.py -c -i ./tmp/15kh_20.10.2023.txt -o /dev/null
Korrigjime totale:      12872
Runtime: 194.953 seconds
'''

import re, sys, argparse	# paketa të domosdoshme

# importimi i funksioneve korrigjuese nga modulet përkatëse
from redakto import *

## funksioni kryesor i korrigjimeve që thërret funksionet e tjera
def redaktime(in_text):
	# merret përmbajtja e kutizës së parë
	input_text = in_text
	t = input_text ; total_sub = 0
	
	## thirret funksioni kryesor i redaktimeve
	t, e_subs, c_subs, pj_subs, tj_subs = redakto(t) 
	total_sub = c_subs + e_subs + pj_subs + tj_subs

	output_text = t
	
	output_message = f"-----------------------------\n" + \
		f"Korrigjime të ë-ve:\t{e_subs}\n" + \
		f"Korrigjime të ç-ve:\t{c_subs}\n" + \
		f"Korrigjime pjesoresh:\t{pj_subs}\n" + \
		f"Korrigjime të tjera:\t{tj_subs}\n" + \
		f"-----------------------------\n" + \
		f"Korrigjime totale:\t{total_sub}"
	
	## shfaqet totali i zëvendësimeve të kryera
	# output_message = f"Zëvendësime totale:\t{total_sub}\n"

	return output_text, output_message
	
# argumentet për ekzekutimin nga terminali
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--corrections', action="store_true", help="Shfaq korrigjimet e kryera")
parser.add_argument('-i', '--input', help='Skedari hyrës')
parser.add_argument('-o', '--output', help='Skedari dalës')
args = parser.parse_args()

## pikënisja e ekzekutimit
if __name__ == "__main__":
	
	# nëse jepet edhe hyrja edhe dalja
	if args.input and args.output:
		# lexohet dhe përpunohet hyrja
		in_file = open(args.input, 'r')
		in_text = in_file.read()
		in_file.close()
		text, message = redaktime(in_text)
		
		# shkruhet dalja te skedari dalës
		out_file = open(args.output, 'w')
		out_file.write(text)
		out_file.close()
		
		# afishohen korrigjimet e kryera
		if args.corrections:
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

		# afishohen korrigjimet e kryera
		if args.corrections:
			print(f"\n{message}\n")
	
	# nëse nuk jepen as hyrja as dalja
	elif not args.input and not args.output:
		# hyrja merret nga terminali
		in_text = input("\nTeksti hyrës:\n")
		text, message = redaktime(in_text)
		# dalja afishohet në terminal
		print(f"\nTeksti dalës:\n{text}")

		# afishohen korrigjimet e kryera
		if args.corrections:
			print(f"\n{message}\n")

	# komandë e shkruar gabim
	else:
		print("Komandë e shkruar gabim...")
		sys.exit(1)

