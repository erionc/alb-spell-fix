# Vetëkorrigjues për gjuhën shqipe

Ky program korrigjimesh automatike për gjuhën shqipe është konceptuar si
një mjet softuer i hapur dhe falas (shih skedarin LICENSA.txt), në dobi të
gjithkujt që shkruan nëpër faqe ueb, forume, rrjete shoqërore virtuale, etj.
Motivi kryesor për zhvillimin e tij ka qenë domosdoshmëria e pastrimit të
faqeve te Wikipedia në gjuhën shqipe, veçanërisht për të tejkaluar problemin
e mprehtë të mospërdorimit të shkronjave ë dhe ç dhe pasojave të shumta 
negative që rrjedhin. Programi ndjek një përqasje thuajse shteruese 
zëvendësimesh me anë të shprehjeve të rregullta. Kriteri themelor i hartimit
të tyre është shmangia e çdo ndryshimi që do të çonte në përplasje apo
dykuptimësi të fjalëve. Për këtë arsye, ekzekutimi i programit në çfarëdo 
teksti hyrës jo vetem që nuk sjell asnjë gabim shtesë, por nuk shkakton as 
devijime në stilin apo formatin e shkrimit. Me zgjerimet leksikore të 
parashikuara, programi do të jetë në gjendje të korrigjojë shumicën e
gabimeve drejtshkrimore që ndeshen në shkrimet e sotme.

## Parakushte

Kodi i programit është shkruar dhe testuar me libraritë e mëposhtëme:
- python >= 3.7.6
- re >= 2.2.1
- argparse >= 1.1
- tkinter >= 8.6

## Përdorimi

Programi mund të përdoret me dritare grafike ose direkt nga terminali. Për
ta përdorur duke ndërvepruar me dritaren grafike nevojitet libraria *tkinter*,
ndërsa libraria *argparse* nuk është e domosdoshme. Programi aktivizohet duke
shtypur komandën e mëposhtëme:

```
$ python dritare.py
```

Do të hapet dritarja grafike me dy fusha të mëdha teksti. Te fusha e sipërme 
shkruhet ose ngjitet teksti të kemi për të redaktuar. Shtypet butoni *Redakto* 
dhe teksti i redaktuar do të shfaqet menjëherë te dritarja e poshtëme nga ku 
mund të kopjohet. Në qoshen poshtë, djathtas do të shfaqet numri i 
zëvendësimeve korrigjuese të kryera. Nëse dëshirojmë ta fshijmë përmbajtjen 
aktuale të fushave të tekstit shtypim butonin *Shuaj*. Në këtë pikë, programi 
mund të përdoret për të redaktuar një shkëputje tjetër teksti, pa qenë nevoja 
për ta mbyllur dhe ekzekutuar nga e para. Nëse dëshirojmë ta përdorim 
programindirekt nga terminali, libraria *tkinter* nuk nevojitet ndërsa libraria
*argparse* është e domosdoshme. Në këtë rast mund t'i kalojmë programit tekstin 
me gabime që gjendet te skedari i hyrjes dhe skedarin e daljes ku të shkruhet teksti i redaktuar. Komanda që duhet shtypur është:

```
$ python terminal.py --input skedar_hyrës --output skedar_dalës
```

Nëse tekstin me gabime e kemi te skedari hyrës por tekstin e redaktuar
duam ta shfaqim në ekran, atëherë e ekzekutojmë komandën si më poshtë:

```
$ python terminal.py --input skedar_hyrës
```

Nëse dëshirojmë që tekstin e hyrjes ta shtypim në terminal e po në 
terminal të marrim edhe tekstin e daljes, atëherë e ekzekutojmë komandën
si më poshtë:

```
$ python terminal.py
```

Në këtë rast duhet patur kujdes që teksti të shkruhet në mënyrë të vijueshme,
pa shtypur butonin "enter" i cili nënkupton përfundimin e futjes së tekstit
dhe aktivizimin e korrigjimeve. Programi do të përdorej me siguri më lehtë
dhe më shpejtë i ndërtuar si një mbishtim për shfletuesin Firefox, çka do
bënte të mundur thirrjen e tij mbi të gjithë tekstin e fushës së shfletuesit.
Një realizim i tillë ngelet në prespektivë.