/*
 * mega328p.cpp
 *
 * Created: 10/27/2015 1:07:39 AM
 * Author : hpan
 */ 

#define F_CPU 16e6	//arudino uno clk speed = 16MHz; UL=unsigned long

#include <avr/io.h>
#include <util/delay.h>

int main(void)	//turn on LED on pin13 of arduino uno
{	
    DDRB |= 1<<DDB5;	//set PB5 as output
    while (1) {
		PORTB |= 1<<PORTB5;		//pull PB5 high
		_delay_ms(1000);
		PORTB &= ~(1<<PORTB5);	//pull PB5 low
		_delay_ms(1000);
    }
}

