/*

 */ 

#define F_CPU 16e6

#include <avr/io.h>
#include <util/delay.h>


int main(void){
	const uint16_t delay_t = 1000;
	
	DDRB |= 1<<DDB0;	//define the port output direction; 1=output, 0=input
	
	DDRC |= 1<<DDC6;	//define the port output direction; 1=output, 0=input	
    DDRC |= 1<<DDC7;	//define the port output direction; 1=output, 0=input	
	
	DDRD |= 1<<DDD5;	//define the port output direction; 1=output, 0=input
	DDRD |= 1<<DDD7;	//define the port output direction; 1=output, 0=input	
	
	DDRE |= 1<<DDE6;	//define the port output direction; 1=output, 0=input	
	
	
	
    while (1){
		PINB |= 1<<PINB0;	//toggle port x pin x
				
		PINC |= 1<<PINC6;	//toggle port x pin x
		PINC |= 1<<PINC7;	//toggle port x pin x
		
		PIND |= 1<<PIND5;	//toggle port x pin x
		PIND |= 1<<PIND7;	//toggle port x pin x
		
		PINE |= 1<<PINE6;	//toggle port x pin x		
		_delay_ms(delay_t);
    }
}
