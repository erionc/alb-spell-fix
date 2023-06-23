
import re, string

## 0-4 simbole shtesë në fillim të fjalëve për prapashtesat angleze
engpara_0_4 = "[a-zA-Z0-9çÇëË_-]{0,4}"

## 0-7 simbole shtesë në fillim të fjalëve për prapashtesat angleze
engpara_0_7 = "[a-zA-Z0-9çÇëË_-]{0,7}"

## 0-4 simbole shtesë në fund të fjalëve për prapashtesat angleze
engprapa_0_4 = "[a-zA-Z0-9çÇëË_-]{0,4}"

## 0-7 simbole shtesë në fund të fjalëve për prapashtesat angleze
engprapa_0_7 = "[a-zA-Z0-9çÇëË_-]{0,7}"


## 0-7 simbole shtesë në fillim të fjalëve për parashtesa 
albpara_0_1 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,1}"

## 0-2 simbole shtesë në fillim të fjalëve për parashtesa
albpara_0_2 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,2}"

## 1-2 simbole shtesë në fillim të fjalëve për parashtesa
albpara_1_2 = "[a-vx-zA-VX-Z0-9çÇëË_-]{1,2}"

## 0-3 simbole shtesë në fillim të fjalëve për parashtesa
albpara_0_3 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,3}"

## 1-3 simbole shtesë në fillim të fjalëve për parashtesa
albpara_1_3 = "[a-vx-zA-VX-Z0-9çÇëË_-]{1,3}"

## 0-5 simbole shtesë në fillim të fjalëve për parashtesa
albpara_0_5 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,5}"

## 0-2 simbole shtesë në fillim të fjalëve për parashtesa
albpara_1_5 = "[a-vx-zA-VX-Z0-9çÇëË_-]{1,5}"

## 0-2 simbole shtesë në fillim të fjalëve për parashtesa
albpara_0_7 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,7}"

## 1-7 simbole shtesë në fillim të fjalëve për parashtesa
albpara_1_7 = "[a-vx-zA-VX-Z0-9çÇëË_-]{1,7}"

## 0-12 simbole shtesë në fillim të fjalëve për parashtesa
albpara_0_12 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,12}"

## 1-12 simbole shtesë në fillim të fjalëve për parashtesa
albpara_1_12 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,12}"


## 0-1 simbole shtesë në fund të fjalëve për mbaresa të shkurtra
albprapa_0_1 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,1}"

## 0-2 simbole shtesë në fund të fjalëve për mbaresa të shkurtra
albprapa_0_2 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,2}"

## 1-2 simbole shtesë në fund të fjalëve për mbaresa të shkurtra
albprapa_1_2 = "[a-vx-zA-VX-Z0-9çÇëË_-]{1,2}"

## 0-3 simbole shtesë në fund të fjalëve për mbaresa të shkurtra
albprapa_0_3 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,3}"

## 1-3 simbole shtesë në fund të fjalëve për mbaresa të shkurtra
albprapa_1_3 = "[a-vx-zA-VX-Z0-9çÇëË_-]{1,3}"

## 0-5 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
albprapa_0_5 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,5}"

## 1-5 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
albprapa_1_5 = "[a-vx-zA-VX-Z0-9çÇëË_-]{1,5}"

## 0-7 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
albprapa_0_7 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,7}"

## 1-7 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
albprapa_1_7 = "[a-vx-zA-VX-Z0-9çÇëË_-]{1,7}"

## 0-12 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
albprapa_0_12 = "[a-vx-zA-VX-Z0-9çÇëË_-]{0,12}"

## 1-12 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
albprapa_1_12 = "[a-vx-zA-VX-Z0-9çÇëË_-]{1,12}"


## foljet e zgjedhimit të parë
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
folje_zgj_1 = "abuzo|acaro|admiro|adhuro|aftëso|akordo|aktivizo|akumulo|akuzo|analizo|anashkalo|ano|arno|aspiro|avanco|" + \
    "barazo|beso|blindo|blua|bre|" + \
    "cakto|cilëso|" + \
    "çliro|çmino|çmo|çmonto|" + \
    "dallo|darko|depërto|dëfre|dëfto|dëgjo|dëmshpërble|dëno|dërgo|dështo|dikto|diskuto|drejto|dreko|dreno|duro|" + \
    "dhuno|dhuro|" + \
    "emëro|emërto|" + \
    "ëndërro|" + \
    "falendero|falëndero|fërko|fërshëlle|filloj|flijo|formo|formulo|fshi|fto|" + \
    "gatua|gdhi|gënje|gërmo|gllabëro|" + \
    "gjurmo|" + \
    "hakërre|hamendëso|harro|harxho|hulumto|" + \
    "imito|intimido|injoro|" + \
    "jeto|jetëso|" + \
    "kallëzo|kapërce|kapërdi|karakterizo|këmbe|këndo|kërce|kërko|klasifiko|konsumo|kontrollo|kopjo|korrigjo|krijo|krye|kryqëzo|kthe|kufizo|kujto|kundërshto|kupto|kurorëzo|kurse|" + \
    "la|lajmëro|lexo|lëndo|lëpi|lëro|lëvro|livro|lua|lundro|" + \
    "mallëngje|mashtro|mbaro|mbërthe|mbij|mendo|mëso|mirato|mirëkupto|mpi|" + \
    "nda|ndërto|ndëshko|ndijo|ndje|ndriço|ndrysho|ndy|ngacmo|ngadhënje|ngashëre|ngazëlle|ngërthe|ngri|ngushto|nxi|" + \
    "pajto|parapëlqe|parashiko|pastro|pendo|pengo|pëlqe|përmba|përdhuno|përgjo|përjeto|përkthe|përlye|përto|përthye|pëso|piketo|pikëllo|pikturo|pleqëro|prano|profilizo|provo|punëso|puno|pusho|" + \
    "qarko|qarkullo|qëllo|qëro|qorto|qua|" + \
    "rekruto|rendo|rëndo|respekto|" + \
    "rreshto|rreziko|rrëfe|rrëmbe|rrëzo|" + \
    "saboto|sakrifiko|sfido|stërhollo|studio|sundo|" + \
    "shërbe|shfleto|shiko|shkatërro|shkëlqe|shkëmbe|shkrua|shkurto|shlye|shpenzo|shpërble|shpërnda|shpërqendro|shpëto|shpërthe|shpreso|shqipëro|shqipto|shqye|shqyrto|shtri|shtro|shty|" + \
    "tërbo|tështi|tingëllo|trajno|trazo|trego|trillo|" + \
    "tha|thye|" + \
    "urre|ushqe|" + \
    "vajto|varfëro|vazhdo|verifiko|vepro|vëre|vëzhgo|vizato|vlerëso|vlo|vrapo|vrojto|vua|" + \
    "zbardh|zbarko|zëvendëso|zgjero|zgjo|" + \
    "zhbiro|zhgënje"

## foljet e zgjedhimit të dytë
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
folje_zgj_2 = "arratis|" + \
    "bërtas|brengos|" + \
    "djeg|" + \
    "çakërdis|çmend|ço|" + \
    "flak|" + \
    "gërhas|" + \
    "hap|" + \
    "kap|korr|kurdis|" + \
    "lag|" + \
    "mat|mbjell|" + \
    "ndesh|ndrydh|ngas|ngrys|nis|nuhat|nxjer|" + \
    "prek|" + \
    "qëndis|" + \
    "she|shkreh|shtyp|" + \
    "thith|" + \
    "ul" + \
    "varro|vjedh|vjell|vulo|" + \
    "zbardh|zbyth|zgjat|zmbraps|zhyt"

## foljet e zgjedhimit të tretë
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
folje_zgj_3 = "fle|" + \
    "ha|" + \
    "ngre|" + \
    "pi|" + \
    "rri"

## të gjitha foljet
## ruhen prapashtesat ndaj nuk pranohen tema me grupe me | si (e|ë)
folje = f"{folje_zgj_1}|{folje_zgj_2}|{folje_zgj_3}"
