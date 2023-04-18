
import re, string

## 0-1 simbole shtesë në fillim të fjalëve për parashtesa
para_0_1 = "[a-zA-Z0-9çÇëË_-]{0,1}"

## 0-2 simbole shtesë në fillim të fjalëve për parashtesa
para_0_2 = "[a-zA-Z0-9çÇëË_-]{0,2}"

## 1-2 simbole shtesë në fillim të fjalëve për parashtesa
para_1_2 = "[a-zA-Z0-9çÇëË_-]{1,2}"

## 0-5 simbole shtesë në fillim të fjalëve për parashtesa
para_0_5 = "[a-zA-Z0-9çÇëË_-]{0,5}"

## 0-2 simbole shtesë në fillim të fjalëve për parashtesa
para_1_5 = "[a-zA-Z0-9çÇëË_-]{1,5}"

## 0-2 simbole shtesë në fillim të fjalëve për parashtesa
para_0_7 = "[a-zA-Z0-9çÇëË_-]{0,7}"

## 1-7 simbole shtesë në fillim të fjalëve për parashtesa
para_1_7 = "[a-zA-Z0-9çÇëË_-]{1,7}"

## 0-12 simbole shtesë në fillim të fjalëve për parashtesa
para_0_12 = "[a-zA-Z0-9çÇëË_-]{0,12}"

## 1-12 simbole shtesë në fillim të fjalëve për parashtesa
para_1_12 = "[a-zA-Z0-9çÇëË_-]{0,12}"


## 0-1 simbole shtesë në fund të fjalëve për mbaresa të shkurtra
prapa_0_1 = "[a-zA-Z0-9çÇëË_-]{0,1}"

## 0-2 simbole shtesë në fund të fjalëve për mbaresa të shkurtra
prapa_0_2 = "[a-zA-Z0-9çÇëË_-]{0,2}"

## 1-2 simbole shtesë në fund të fjalëve për mbaresa të shkurtra
prapa_1_2 = "[a-zA-Z0-9çÇëË_-]{1,2}"

## 0-5 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
prapa_0_5 = "[a-zA-Z0-9çÇëË_-]{0,5}"

## 1-5 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
prapa_1_5 = "[a-zA-Z0-9çÇëË_-]{1,5}"

## 0-7 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
prapa_0_7 = "[a-zA-Z0-9çÇëË_-]{0,7}"

## 1-7 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
prapa_1_7 = "[a-zA-Z0-9çÇëË_-]{1,7}"

## 0-12 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
prapa_0_12 = "[a-zA-Z0-9çÇëË_-]{0,12}"

## 1-12 simbole shtesë në fund të fjalëve për prapashtesat dhe lakesat
prapa_1_12 = "[a-zA-Z0-9çÇëË_-]{1,12}"
