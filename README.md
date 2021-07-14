# Vetëkorrigjues për gjuhës shqipe

Ky program korrigjimesh automatike është konceptuar si një mjet softuer
i hapur dhe falas, në dobi të gjithkujt që shkruan në faqe ueb, forume,
rrjete shoqërore virtuale, etj. Pikënisja ka qenë domosdoshmëria e 
pastrimit të faqeve shqip në Wikipedia, veçanërisht për të tejkaluar
problemin e mprehtë të mospërdorimit të shkronjave ë dhe ç dhe pasojave
të shumta negative që rrjedhin. Programi mbështetet te zëvendësimet
korrigjuese të bazuara te shprehjet e rregullta. Kriteri themelor i
hartimit të zëvenësimeve është shmangia e çdo ndryshimi që do të çonte në
përplasje apo dykuptimësi të fjalëve. Për këtë arsye, ekzekutimi i
programit në çfarëdo teksti hyrës jo vetem që nuk sjell asnjë gabim shtesë,
por nuk shkakton as devijime në stilin apo formatin e shkrimit. 

## Parakushte

Kodi i programit është shkruar dhe testuar me libraritë e mëposhtëme:
- python >= 3.7.6
- tkinter >= 8.6

## Përdorimi

**Ekzekutimi i programit kryhet me komandën e mëposhtëme:**

```
$ python dritare.py
```
Do të hapet dritarja grafike me dy fusha të mëdha teksti. Te fusha 
e sipërme shkruhet ose ngjitet teksti të kemi për të redaktuar. Shtypet
butoni *Redakto* dhe teksti i redaktuar do të shfaqet menjëherë te dritarja
e poshtëme nga ku mund të kopjohet. Në qoshen poshtë, djathtas do të 
shfaqet numri i zëvendësimeve korrigjuese të kryera. Nëse dëshirojmë ta
fshijmë përmbajtjen aktuale të fushave të tekstit shtypim butonin *Shuaj*.
Në këtë pikë, programi mund të përdoret për të redaktuar një shkëputje
tjetër teksti, pa qenë nevoja për ta mbyllur dhe ekzekutuar nga e para.

