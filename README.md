# [ENG] Autocorrector for Albanian language
This program of automatic corrections for Albanian language is conceived as a free and open software tool (see LICENSA.txt file) to help anyone who writes in websites, forums, virtual social networks etc. The main motive for developing it is the need for cleaning the Albanian Wikipedia pages, especially for overcoming the acute problem of omitting the Ë/ë and Ç/ç letters and the many negative consequences it brings. The program follows an exhaustive approach of substitutions using regular expressions. The basic criterion of applying the substitutions is to avoid any change that would lead to word ambiguity. For this reason, running the program on any input text does not inject any extra errors and does not cause any change in writing format or style. The coded corrections and the expected extensions are based on the book: 

Ky program korrigjimesh automatike për gjuhën shqipe është konceptuar si një mjet softuer i hapur dhe falas (shih skedarin LICENSA.txt), në dobi të gjithkujt që shkruan nëpër faqe ueb, forume, rrjete shoqërore virtuale etj. Motivi kryesor për zhvillimin e tij ka qenë domosdoshmëria e pastrimit të faqeve te Wikipedia-s në gjuhën shqipe, veçanërisht për të tejkaluar problemin e mprehtë të mospërdorimit të shkronjave Ë/ë dhe Ç/ç dhe pasojave të shumta negative që rrjedhin. Programi ndjek një përqasje thuajse shteruese zëvendësimesh me anë të shprehjeve të rregullta. Kriteri themelor i hartimit të tyre është shmangia e çdo ndryshimi që do të çonte në përplasje apo dykuptimësi të fjalëve. Për këtë arsye, ekzekutimi i programit në çfarëdo teksti hyrës jo vetem që nuk sjell asnjë gabim shtesë, por nuk shkakton as devijime në stilin apo formatin e shkrimit. Korrigjimet e koduara dhe zgjerimet që parashikohet të shtohen gradualisht bazohen te libri:

Erion Çano, Edmond Tupja: [Terminologji informatike: problematika dhe zgjidhje.](https://zenodo.org/record/6378930) ISBN: 978-9928-320-83-4, DOI: 10.5281/zenodo.6378930, Tiranë, mars 2022

the electronic version of which can be downloaded for free. The current version of the program is able to correct most of the ortographical errors that are found in current writings. 

## Preconditions

The code has been writen and tested with the following packages:
- python >= 3.10.6
- re >= 2.2.1
- argparse >= 1.1
- tkinter >= 8.6

## Run

The program can be run by double clicking the precompiled files or from the terminal. To lunch it from the precompiled files you double cick the file **dritare.exe** on Windows systems. On GNU/Linux and MacOS systems you can do so by running the following command on the terminal:

```
$ python dritare.py
```

A graphical windows with two text fields will open. You write or paste the text to correct on the upper text field. You push the button **Redakto** and the corrected text will appear on the bottom window from where you can copy it. The numnber of corrective substitutions will appear in the bottom right corner. If you want to clear the current content of the two text fields, you push the **Shuaj** button. At this point, the programm can be used to correct another text excerpt, with no need to load it again. To use the program directly from the terminal, it is not necessary to have the package **tkinter** installed, but the **argparse** is mandatory. In such case, you should pass to the program the file with the text to correct as input and the corrected text file as output.The command to run is:    

```
$ python terminal.py --input <input_file> --output <output_file>
```

If the text to correct is in the input file, but you want the corrected text to appear on the screen, you run the command as follows:

```
$ python terminal.py --input <skedar_hyrës>
```

If you want to type or paste the text to correct on thge terminal and get the corrected text also on the terminal, you run the command as follows:

```
$ python terminal.py
```

The latest invocation should be avoided, since you have to be careful to type the input text continuosly, without pressing the "Enter" button which indicates end of text input and invokes the activation of the corrections. It would be easier to use the program as an addon for the Firefox brawser, which would invoke it on the whole text of the brawser. Such implementation is left as a future extension. 

# [ALB] Vetëkorrigjues për gjuhën shqipe

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

Do të hapet dritarja grafike me dy fusha të mëdha teksti. Te fusha e sipërme shkruhet ose ngjitet teksti që kemi për të redaktuar. Shtypet butoni **Redakto** dhe teksti i redaktuar do të shfaqet menjëherë te dritarja e poshtëme nga ku mund të kopjohet. Në qoshen poshtë, djathtas do të shfaqet numri i zëvendësimeve korrigjuese të kryera. Nëse dëshirojmë ta fshijmë përmbajtjen aktuale të fushave të tekstit shtypim butonin **Shuaj**. Në këtë pikë, programi mund të përdoret për të redaktuar një shkëputje tjetër teksti, pa qenë nevoja për ta mbyllur dhe ekzekutuar nga e para. Nëse dëshirojmë ta përdorim programin direkt nga terminali, paketa **tkinter** nuk nevojitet ndërsapaketa **argparse** është e domosdoshme. Në këtë rast mund t'i kalojmë programit tekstin me gabime që gjendet te skedari i hyrjes dhe skedarin e daljes ku të shkruhet teksti i redaktuar. Komanda që duhet shtypur është:

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