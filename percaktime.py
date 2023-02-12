
import re, string

## ndryshore globale për fundin e fjalëve - më mirë (\b) 
# we = " |\t|\n|\.|\?|:|;|,|!"

## 0-5 simbole shtesë në fund të fjalëve për prapashtesat shquese dhe lakesat - e shumta 5 simbole
prapa = "[a-zA-Z0-9çÇëË_-]{0,5}"

## fjalë që i paraprinë të-së -- do të, dua të, desha të 
para_te = "dua\s|do\s|duam\s|doni\s|duan\s|doja\s|doje\s|donte\s|" + \
	"donim\s|donit\s|donin\s|desha\s|deshe\s|deshte\s|deshëm\s|" + \
	"deshët\s|deshën\s|me\s|sapo\s|porsa\s|duhet\s|sikur\s|mund\s|" + \
	"kush\s|cil(i|a)\s|cil(ë|a)t\s|ku\sdo\s|kur\sdo\s|(c|ç)far(e|ë)\s|" 

## foljet ndihmëse kam/jam që paraprijnë pjesoret
kam_jam = "Kam\s|kam\s|Ke\s|ke\s|Ka\s|ka\s|Kemi\s|kemi\s|Keni\s|keni\s|" + \
	"Kanë\s|kanë\s|" + \
	"Jam\s|jam\s|Je\s|je\s|Është\s|është\s|Jemi\s|" + \
	"jemi\s|Jeni\s|jeni\s|Janë\s|janë\s|" + \
	"Kisha\s|kisha\s|Kishe\s|kishe\s|Kishte\s|kishte\s|Kishim\s" + \
	"kishim\s|Kishit\s|kishit\s|Kishin\s|kishin\s|" + \
	"Isha\s|isha\s|Ishe\s|ishe\s|Ishte\s|ishte\s|Ishim\s|ishim\s|" + \
	"Ishit\s|ishit\s|Ishin\s|ishin\s|" + \
	"Pata\s|pata\s|Pate\s|pate\s|Pati\s|pati\s|Patëm\s|patëm\s|" + \
	"Patët\s|patët\s|Patën\s|patën\s|" + \
	"Qeshë\s|qeshë\s|Qe\s|qe\s|Qemë\s|qemë\s|Qetë\s|qetë\s|" + \
	"Qenë\s|qenë\s|"

## format e pashtjelluara që paraprijnë pjesoret
form_pashtj = "për\stë\s|duke\s|pa\s|"

## të tjera forma që qëndrojnë para pjesores 
tjera_para_pjesor = "me\stë\s"

## forma që qëndrojnë para pjesores
para_pjesoreve = kam_jam + form_pashtj + tjera_para_pjesor



	
	