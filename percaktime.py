
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
