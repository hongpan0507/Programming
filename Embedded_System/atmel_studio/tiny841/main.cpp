/*
 * tiny841.cpp
 *
 * Created: 10/28/2015 2:49:14 PM
 * Author : hpan
 *
 * All page numbers are referred to ATtiny 841 datasheet unless state otherwise
 -------------------------------------------------------------------------------------------
	**Programming Notes:			
		# To set a bit: bitwise or; Ex. PORTB |= 1 << PORTB3; //pull PB3 high
		# To clear a bit: invert, then bitwise and; Ex. PORTB &= ~(1 << PORTB3); //pull PB3 high
		# PINx = Port x Data; Write 1 to PINx toggles the port data (1/0) regardless of DDRx
		# DDRx = Port x I/O
		# PORTx = Port x H/L
		# Fuse calculation {			//Not Programmed = 1; Programmed = 0;
			Extended bit 0: SELFPRGEN;	//Self-programming enable
			HIGH bit 7:	RESDISBL;		//External Reset Disable
			HIGH bit 6:	DWEN;			//Debug Wire Enable
			HIGH bit 5:	SPIEN;			//SPI Enable
			HIGH bit 4:	WDTON;			//Watch-dog Timer Always On
			HIGH bit 3:	EESAVE;			//Preserve EEPROM Through Chip Erase Cycle
			HIGH bit 2-0: BODLEVEL;		//Brown-out Detection Level
			LOW bit 7:	CKDIV8			//Divide CLK by 8 internally
			LOW bit 6:	CKOUT			//CLK output on PORTB4
			LOW bit 5-4: SUT;			//Start Up Time
			LOW bit 3-0: CKSEL;			//CLK Source Select
		}
		# To run assembly in Arduino: __asm__("nop"); __asm__("ldi r16, 0x02");
-------------------------------------------------------------------------------------------		
	**Device Setting:
		# Fuse {
			Extended = 0xFF; 
			High = 0xD7; 
			Low = 0xC2;
		}
		# Lock Bit = 0xFF
-------------------------------------------------------------------------------------------					
 */ 

#define F_CPU 8e6	//CPU clock must be defined first in order to use internal delay function

#include <avr/io.h>
#include <util/delay.h>

int main(void){		//LED on PA2 & PA7    
	
	//const uint16_t delay_time = 1000;
	//DDRA |= 1<<DDRA2;	//configure PA2 as output
	//DDRA |= 1<<DDRA7;	//configure PA7 as output
	//PORTA |= 1<<PORTA2;	//pull PA2 high
	//PORTA &= ~(1<<PORTA7);	//pull PA7 low
	//_delay_ms(delay_time);	//internal delay function
    //while (1){
		//PINA |= 1<<PINA2;	//toggle PA2
		//PINA |= 1<<PINA7;	//toggle PA7
		//_delay_ms(delay_time);	//internal delay function
		///*
		//PORTA |= 1<<PORTA2;	//pull PA2 high
		//PORTA &= ~(1<<PORTA7);	//pull PA7 low
		//_delay_ms(delay_time);	//internal delay function
		//PORTA &= ~(1<<PORTA2);	//pull PA2 low
		//PORTA |= 1<<PORTA7;	//pull PA7 high
		//_delay_ms(delay_time);	//internal delay function
		//*/				
    //}
	const uint16_t delay_time = 1000;
	DDRA |= 1<<DDRA0;	//configure PA0 as output	
	PORTA |= 1<<PORTA0;	//pull PA0 high	
	_delay_ms(delay_time);	//internal delay function
    while (1){
		PINA |= 1<<PINA0;	//toggle PA0		
		_delay_ms(delay_time);	//internal delay function
		/*
		PORTA |= 1<<PORTA2;	//pull PA2 high
		PORTA &= ~(1<<PORTA7);	//pull PA7 low
		_delay_ms(delay_time);	//internal delay function
		PORTA &= ~(1<<PORTA2);	//pull PA2 low
		PORTA |= 1<<PORTA7;	//pull PA7 high
		_delay_ms(delay_time);	//internal delay function
		*/				
    }
}

