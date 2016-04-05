Atmel MCU Programming Notes
	Interrupt
		Source1: http://www.nongnu.org/avr-libc/user-manual/group__avr__interrupts.html
		Source2: http://www.avrfreaks.net/forum/tut-newbies-guide-avr-interrupts?page=all
		ISR() Macro		
		interrupt vector table can be found in the datasheet
		When programming, pre-defined interrupt vector can be found in IO definition file; i.e C:\Program Files (x86)\Atmel\Studio\7.0\Packs\atmel\ATtiny_DFP\1.0.68\include\avr\iotn841.h
		pre-defined vector uses address(found in the datasheet) for the lookup table