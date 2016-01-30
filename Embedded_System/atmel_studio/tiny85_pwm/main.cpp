/*
 * tiny85_pwm.cpp
 *
 * Created: 12/19/2015 9:13:52 PM
 * Author : hpan
 
 Programming Notes:
	# PWM generation (8-bit counter) {
		select clk source; synchronus/asynchronus mode; page 83; page86 {
			asynchronous mode { page86
				set time/counter in asynchronous mode
				enable PLL
				wait for 100us
				poll PLOCK bit
			}
			
		}
		set prescaler; page 83		
		set output compare register; page 85 {
			OCR1C stores Timer/Counter maximum value
		}
		enable PWM mode
		
	}
	
 */ 

#define F_CPU 8e6

#include <avr/io.h>
#include <util/delay.h>

int main(void) {	
	DDRB |= 1 << DDB4;	//set PB4 as output
	
	//-----------------select PCK as clk source------------------------
	PLLCSR |= 1 << PCKE;	//PCK enable = use 64MHz clk source; asynchronus mode
	PLLCSR |= 1 << PLLE;	//enable PLL
	_delay_us(100);		//refer to the programming note
	while(!(PLLCSR & (1<<PLOCK))){	//extract PLOCK bit; if not set, wait; if set, move forward; page 94
		;
	}
	//------------------------------------------------------------------
		
	TCCR1 |= 1 << CTC1;		//reset timer/counter after compare match with OCR1C register; page 89	
	TCCR1 |= ((1<<CS12) | (1<<CS10));	//select prescaler; page 89; page 88; pwm freq = 20kHz
	TCCR1 &= ~((1<<CS13) | (1<<CS11));	//select prescaler; page 89; page 88; pwm freq = 20kHz
	OCR1C = 199;	//output compare register value; page 92; page 88; pwm freq = 20kHz; refer to programming notes
	
	GTCCR |= 1 << PWM1B;	//enable PWM1B module
	GTCCR |= 1 << COM1B1;	//clear the OC1B output line when match is detected; page 90
	GTCCR &= ~(1 << COM1B0);	//clear the OC1B output line when match is detected; page 90
	OCR1B = 127;	//output compare register value; page 91
		
    /* Replace with your application code */
    while (1) {
		for(int i=0; i<200; ++i){
			OCR1B = i;
			_delay_ms(10);
		}
		
    }
}

