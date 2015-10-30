cd /D C:\Program Files (x86)\Arduino\hardware\tools\avr\bin
avrdude -C"C:\Program Files (x86)\Arduino\hardware\tools\avr\etc\avrdude.conf" -F -v -v -v -v -pattiny85 -cstk500v1 -P\\.\COM9 -b19200 -e -Uefuse:w:0xFF:m -Uhfuse:w:0xD7:m -Ulfuse:w:0xE2:m
