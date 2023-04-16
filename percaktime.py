
import re, string

## 0-2 simbole shtesë në fillim të fjalëve për parashtesa
para_shkurt = "[a-zA-Z0-9çÇëË_-]{0,2}"

## 0-5 simbole shtesë në fillim të fjalëve për parashtesat
para_gjat = "[a-zA-Z0-9çÇëË_-]{0,5}"

## 1-5 simbole shtesë në fillim të fjalëve për parashtesa
para_jo_bosh = "[a-zA-Z0-9çÇëË_-]{1,5}"

## 0-12 simbole shtesë në fillim të fjalëve për parashtesat
para_me_gjat = "[a-zA-Z0-9çÇëË_-]{0,12}"

## 1-12 simbole shtesë në fillim të fjalëve për parashtesat
para_me_gjat_jo_bosh = "[a-zA-Z0-9çÇëË_-]{1,12}"


## 0-5 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
prapa_gjat = "[a-zA-Z0-9çÇëË_-]{0,5}"

## 0-7 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
prapa_me_gjat = "[a-zA-Z0-9çÇëË_-]{0,7}"

## 0-2 simbole shtesë në fund të fjalëve për mbaresa të shkurtra
prapa_shkurt = "[a-zA-Z0-9çÇëË_-]{0,2}"

## 1-5 simbole shtesë në fund të fjalëve për mbaresa 
prapa_jo_bosh = "[a-zA-Z0-9çÇëË_-]{1,5}"
