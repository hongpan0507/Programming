/*
 * mega328.cpp
 *
 * Created: 2/2/2016 11:06:24 AM
 * Author : hpan
 */ 

#define F_CPU 16e6	//arudino uno clk speed = 16MHz; UL=unsigned long

#include <avr/io.h>
#include <util/delay.h>

int main(void)	//turn on LED on pin13 of arduino uno
{	
	/*
    DDRB |= 1<<DDB5;	//set PB5 as output
    while (1) {
		PORTB |= 1<<PORTB5;		//pull PB5 high
		_delay_ms(1000);
		PORTB &= ~(1<<PORTB5);	//pull PB5 low
		_delay_ms(1000);
    }*/
	DDRD |= 1<<DDD7;	//set PB5 as output
	while (1) {
		PORTD |= 1<<PORTD7;		//pull PB5 high
		_delay_ms(100);
		PORTD &= ~(1<<PORTD7);	//pull PB5 low
		_delay_ms(100);
	}
}



