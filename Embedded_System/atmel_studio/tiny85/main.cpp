/*
 * tiny85.cpp
 *
 * Created: 10/28/2015 3:56:34 PM
 * Author : hpan
 
 Notes:
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
		
 */ 

#define F_CPU 8e6

#include <util/delay.h>
#include <avr/io.h>

int main(void){
	DDRB |= 1<<DDB3;  //set PB3 as output;  p55
	PORTB &= ~(1<<PB3);  //pull PB3 low

	DDRB |= 1<<DDB4;  //set PB4 as output; p55
	PORTB &= ~(1<<PB4);  //pull PB4 low
		
	while (1) {
		PORTB |= 1<<PB3;    //pull PB3 high
		PORTB |= 1<<PB4;    //pull PB4 high
		_delay_ms(1000);
		PORTB &= ~(1<<PB3);  //pull PB3 low
		PORTB &= ~(1<<PB4);  //pull PB4 low
		_delay_ms(1000);
	}
}

