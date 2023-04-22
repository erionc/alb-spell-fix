# Vetëkorrigjues për gjuhën shqipe

Ky program korrigjimesh automatike për gjuhën shqipe është konceptuar si një mjet softuer i hapur dhe falas (shih skedarin LICENSA.txt), në dobi të gjithkujt që shkruan nëpër faqe ueb, forume, rrjete shoqërore virtuale etj. Motivi kryesor për zhvillimin e tij ka qenë domosdoshmëria e pastrimit të faqeve te Wikipedia-s në gjuhën shqipe, veçanërisht për të tejkaluar problemin e mprehtë të mospërdorimit të shkronjave Ë/ë dhe Ç/ç dhe pasojave të shumta negative që rrjedhin. Programi ndjek një përqasje thuajse shteruese zëvendësimesh me anë të shprehjeve të rregullta. Kriteri themelor i hartimit të tyre është shmangia e çdo ndryshimi që do të çonte në përplasje apo dykuptimësi të fjalëve. Për këtë arsye, ekzekutimi i programit në çfarëdo teksti hyrës jo vetem që nuk sjell asnjë gabim shtesë, por nuk shkakton as devijime në stilin apo formatin e shkrimit. Korrigjimet e koduara dhe zgjerimet që parashikohet të shtohen gradualisht bazohen te libri:

Erion Çano, Edmond Tupja: [Terminologji informatike: problematika dhe zgjidhje.](https://zenodo.org/record/6378930) ISBN: 978-9928-320-83-4, DOI: 10.5281/zenodo.6378930, Tiranë, mars 2022

versioni elektronik i të cilit mund të shkarkohet falas. Programi është në gjendje që në versionin aktual që të korrigjojë shumicën e gabimeve drejtshkrimore të cilat ndeshen në shkrimet e sotme.

## Parakushte

Kodi i programit është shkruar dhe testuar me paketat e mëposhtëme:
- python >= 3.10.6
- re >= 2.2.1
- argparse >= 1.1
- tkinter >= 8.6

## Përdorimi

Programi mund të përdoret me klikim të dyfishtë te skedarët e parakompiluar ose nga terminali. Për ta thirrur nga skedarët e parakompiluar mjafton një klikim i dyfishtë te skedari **dritare.exe** në sistemet Windows. Në sistemet GNU/Linux dhe MacOS, e njëjta gjë arrihet në duke shtypur në terminal komandën e mëposhtëme:

```
$ python dritare.py
```

Do të hapet dritarja grafike me dy fusha të mëdha teksti. Te fusha e sipërme shkruhet ose ngjitet teksti që kemi për të redaktuar. Shtypet butoni **Redakto** dhe teksti i redaktuar do të shfaqet menjëherë te dritarja e poshtëme nga ku mund të kopjohet. Në qoshen poshtë, djathtas do të shfaqet numri i zëvendësimeve korrigjuese të kryera. Nëse dëshirojmë ta fshijmë përmbajtjen aktuale të fushave të tekstit shtypim butonin **Shuaj**. Në këtë pikë, programi mund të përdoret për të redaktuar një shkëputje tjetër teksti, pa qenë nevoja për ta mbyllur dhe ekzekutuar nga e para. Nëse dëshirojmë ta përdorim programin direkt nga terminali, paketa **tkinter** nuk nevojitet ndërsa paketa **argparse** është e domosdoshme. Në këtë rast mund t'i kalojmë programit tekstin me gabime që gjendet te skedari i hyrjes dhe skedarin e daljes ku të shkruhet teksti i redaktuar. Komanda që duhet shtypur është:

```
$ python terminal.py --input <skedar_hyrës> --output <skedar_dalës>
```

Nëse tekstin me gabime e kemi te skedari hyrës por tekstin e redaktuar duam ta shfaqim në ekran, e ekzekutojmë komandën si më poshtë:

```
$ python terminal.py --input <skedar_hyrës>
```

Nëse dëshirojmë që tekstin e hyrjes ta shtypim apo ta ngjitim në terminal, e po në terminal të marrim edhe tekstin e daljes, e ekzekutojmë komandën si më poshtë:

```
$ python terminal.py
```

Kjo mënyrë e fundit e përdorimit nuk sugjerohet, sepse duhet bërë kujdes që teksti të shkruhet në mënyrë të vijueshme, pa shtypur tastin "Enter" i cili nënkupton përfundimin e futjes së tekstit dhe aktivizimin e redaktimeve. Programi do të përdorej me siguri më mirë nëse do të qe i ndërtuar si një mbishtim për shfletuesin Firefox, çka do bënte të mundur thirrjen e tij mbi të gjithë tekstin e fushës së shfletuesit. Një realizim i tillë ngelet në prespektivë.
