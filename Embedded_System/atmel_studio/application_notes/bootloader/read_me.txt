Bootloader concept
http://electronics.stackexchange.com/questions/27486/what-is-a-boot-loader-and-how-would-i-develop-one

Steps:
1. Write the bootloader program
2. Use "avr-gcc" to compile the program into .hex file
3. Figure out the fuse bit for the MCU
4. Use "avr dude" to program the fuse bit
5. Connect the ISP (Arduino ISP, AVRISP mkII ect.) to program

Bootloader Reference:

1. http://letsmakerobots.com/node/31379
2. https://voidyourwarranty.wordpress.com/2014/08/17/using-arduino-as-an-isp-to-program-a-standalone-atmega-328p-including-fuses/
3. https://learn.adafruit.com/arduino-tips-tricks-and-techniques/bootloader
4. http://www.gammon.com.au/bootloader
5. http://www.hackersworkbench.com/intro-to-bootloaders-for-avr
6. http://www.engineersgarage.com/embedded/avr-microcontroller-projects/How-To-Write-a-Simple-Bootloader-For-AVR-In-C-language
7. https://www.arduino.cc/en/Hacking/Bootloader?from=Tutorial.Bootloader
8.

Arduino Bootloader Location: C:\Program Files (x86)\Arduino\hardware\arduino\bootloaders