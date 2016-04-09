/*
 * tiny841.cpp
 *
 * Created: 10/28/2015 2:49:14 PM
 * Author : hpan
 *
 * All page numbers are referred to ATtiny 841 datasheet unless state otherwise
 -------------------------------------------------------------------------------------------
	* Device Programming Notes:			
		# To set a bit: bitwise or; Ex. PORTB |= 1 << PORTB3; //pull PB3 high
		# To clear a bit: invert, then bitwise and; Ex. PORTB &= ~(1 << PORTB3); //pull PB3 high
		# PINx = Port x Data; Write 1 to PINx toggles the port data (1/0) regardless of DDRx
		# DDRx = Port x I/O
		# PORTx = Port x H/L
		# Fuse calculation {			//Not Programmed = 1; Programmed = 0;
			Extended bit 7-5: ULPOSCSEL; //Frequency selection for internall ULP oscillator
			Extended bit 4-3: BOD_DISABLED;	//BOD mode of operation when the device is in sleep mode
			Extended bit 2-1: BODACT;	//BOD mode of operation when the device is active or idle
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
	* Device Setting:
		# Fuse {
			Extended = 0xFF; 
			High = 0xD7; 
			Low = 0xC2;
		}
		# Lock Bit = 0xFF
-------------------------------------------------------------------------------------------					
	* SPI Programming Notes:
		# Mode 0 {
			CPOL = 0;	//CLK is low when inactive; CLK starts and ends low
			CPHA = 0;	//Data is valid on CLK leading edge
		}		
		# Mode 1 {
			CPOL = 0;	//CLK is low when inactive; CLK starts and ends low
			CPHA = 1;	//Data is valid on CLK trailing edge
		}		
		# Mode 2 {
			CPOL = 1;	//CLK is high when inactive; CLK starts and ends high
			CPHA = 0;	//Data is valid on CLK leading edge
		}
		# Mode 3 {
			CPOL = 1;	//CLK is high when inactive; CLK starts and ends high
			CPHA = 1;	//Data is valid on CLK trailing edge
		}	
		# Look up Pin direction at page 153; must be defined for both master and slave mode
-------------------------------------------------------------------------------------------					
	* USART0 in SPI mode:
		# f_max = f_cpu/2;
		# only master mode is supported; page 187
		
 */ 


#define F_CPU 16e6	//CPU clock must be defined first in order to use internal delay function
#define UDORD0 2	//not defined by the header file; define manually; page 195
#define UCPHA0 1	//not defined by the header file; define manually; page 195
#define UCPOL0 0	//not defined by the header file; define manually; page 195

#include <avr/interrupt.h>
#include <avr/io.h>
#include <util/delay.h>


void SPI_init();	//initialize SPI module
void USART0_SPI_init(uint8_t baud_rate);	//initialize SPI module

volatile uint8_t data_in = 0;	//receive data
volatile uint8_t data_out[] = {0x15, 0xAB, 0x04, 0x45};	//send data		
volatile bool received_signal = false;	

int main(){					
	DDRB |= 1<<DDRB2;	
	
	cli();	//disable global interrupt; atmel built-in function
	//USART0_SPI_init(0);	//initialize USART0 module; user defined function; set the baud_rate to 1Mbps; page 180
	SPI_init();	//initialize SPI module; user defined function
	sei();	//enable global interrupt; atmel built-in function
				
	while(1){		
		_delay_ms(100);
		PORTA &= ~(1<<PORTA7);
		SPDR = data_out[1];	//place data to SPI data buffer					
		PORTA |= (1<<PORTA7);
		if(received_signal){
			received_signal = false;
			PINB |= 1<<PINB2;	//toggle PORTB2
			_delay_ms(100);
			PINB |= 1<<PINB2;	//toggle PORTB2
			_delay_ms(100);			
		}	
	}
}

void SPI_init(){	//initialize SPI module	
	PRR &= ~(1<<PRSPI); //enable SPI module in PRR; page 152; Page 39	
	SPCR |= 1<<SPIE;	//enable SPI interrupt; page 157; page 158
	SPCR &= ~(1<<DORD);	//MSB to be transmitted first; page 157
	// SPCR &= ~(1<<MSTR);	//enable SPI slave mode; page 157	
	
	SPCR |= (1<<MSTR);	//enable master slave mode; page 157	
	SPCR &= ~(1<CPOL);	//SPI clk is low when idle; page 158
	SPCR &= ~(1<CPHA);	//Data is valid on leading edge; page 158
	REMAP &= ~(1<SPIMAP);	//use default pin map; page 159
	// DDRA &= ~(1<<DDRA7);	//set PA7/SS as input; in slave mode, ss is always input; probably not needed; page 155
	DDRA |= (1<<DDRA7);	//set PA7/SS as output
	DDRA |= 1<<DDRA6;	//set PA6/MOSI as output
	DDRA |= 1<<DDRA4;	//set PA4/SCK as output
	SPCR |= 1<<SPE;	//enable SPI module in SPI control Register; page 157
}

void USART0_SPI_init(uint8_t baud_rate){	//initialize USART0 to operate in SPI master mode
	PRR &= ~(1<<PRUSART0);	//enable USART0 module in PRR; page39; page 160
	UBRR0 = 0;	//set the baud_rate to zero; page 189
	DDRA |= 1<<DDRA3;	//set PA3 as output; XCK0 must be set as output; page 187
	UCSR0C |= (1<<UMSEL00) | (1<<UMSEL01);	//enable SPI mode in USART0; page 195
	UCSR0C &= ~((1<<UDORD0) | (1<<UCPHA0) | (1<<UCPOL0));	//MSB first; clk phase = 0, clk polarity = 0; page 195
	UCSR0A &= ~(1<<U2X0);	//set to zero to use synchronous mode; probably not needed because operating in SPI mode; page 181
	UCSR0B |= (1<<TXEN0);	//enable receiver and transmitter; page 194
	UCSR0B &= ~(1<<RXEN0);	//disable receiver; page 194
	UBRR0 = baud_rate;	//set the baud_rate; baud_rate = 0 -> 1Mbps; page 180
}

//SPIF bit is set when a serial transfer is complete; p158
//SPIF bit is cleared by hardware when the corresponding interrupt is served; page 158
ISR(SPI_vect, ISR_BLOCK){	//SPI interrupt service routine; blocking all other interrupts	
	//send data to digital phase shifter here	
	data_in = SPDR;		//read data from SPI buffer

	//UDR0 = data_in;		//place data to USART0 data buffer and initiate data transfer; page 190
	//while(!(UCSR0A & (1<<TXC0))){	//TXC0 bit is set if USART0_SPI transfer is complete; page 193
		//;
	//}		
	//UCSR0A |= 1<<TXC0;	//clear USART0_SPI transmit complete signal; page 193	
	PINB |= 1<<PINB2;	//toggle PORTB2
			_delay_ms(100);
			PINB |= 1<<PINB2;	//toggle PORTB2
			_delay_ms(100);	
	received_signal = true;	
}




/*
//SPI slave; USART0 as SPI master; No Interrupt 
#define F_CPU 16e6	//CPU clock must be defined first in order to use internal delay function
#define UDORD0 2	//not defined by the header file; define manually; page 195
#define UCPHA0 1	//not defined by the header file; define manually; page 195
#define UCPOL0 0	//not defined by the header file; define manually; page 195

#include <avr/interrupt.h>
#include <avr/io.h>
#include <util/delay.h>


void SPI_init();	//initialize SPI module
void USART0_SPI_init(uint8_t baud_rate);	//initialize SPI module

volatile uint8_t data_in = 0;

int main(){
	DDRA |= 1<<DDRA2;	//configure PA2 as output		
	
	cli();	//disable global interrupt; atmel built-in function
	USART0_SPI_init(0);	////set the baud_rate to 1Mbps; page 180
	SPI_init();	//initialize SPI module; user defined function
	sei();	//enable global interrupt; atmel built-in function
	
	uint8_t data_out[] = {0x15, 0xAB, 0x04, 0x45};	//SPI send data		
	
	while(1){
		for(uint8_t i=0; i<(sizeof(data_out)/sizeof(*data_out)); ++i){			
			SPDR = data_out[i];	//place data to SPI data buffer						
			
			//SPIF bit is set when a SPI transfer is complete; p158
			//SPIF bit is cleared by reading SPSR register with SPIF set, then accessing SPDR; page 158
			while(!(SPSR & (1<<SPIF))){
				;
			}
			data_in = SPDR;		//read data from SPI buffer						
			UDR0 = data_in;	//place data to USART0 data buffer and initiate data transfer; page 190				
			while(!(UCSR0A & (1<<TXC0))){	//TXC0 bit is set if USART0_SPI transfer is complete; page 193
				;
			}
			//data_in = UDR0;		//read received USART0_SPI data
			UCSR0A |= 1<<TXC0;	//clear USART0_SPI transmit complete signal; page 193													
		}		
		_delay_ms(1000);		
	}
}

void SPI_init(){	//initialize SPI module
	sei();	//enable global interrupt; atmel built-in function
	PRR &= ~(1<<PRSPI); //enable SPI module in PRR; page 152; Page 39
	SPCR |= 1<<SPE;	//enable SPI module in SPI control Register; page 157
	SPCR &= ~(1<<DORD);	//MSB to be transmitted first; page 157
	SPCR &= ~(1<<MSTR);	//enable SPI slave mode; page 157
	SPCR &= ~(1<CPOL);	//SPI clk is low when idle; page 158
	SPCR &= ~(1<CPHA);	//Data is valid on leading edge; page 158
	REMAP &= ~(1<SPIMAP);	//use default pin map; page 159
	//DDRA &= ~(1<<DDRA7);	//set PA7/SS as input; in slave mode, ss is always input; page 155
	DDRA |= 1<<DDRA5;	//set PA6/MISO as output
}

void USART0_SPI_init(uint8_t baud_rate){	//initialize USART0 to operate in SPI master mode
	PRR &= ~(1<<PRUSART0);	//enable USART0 module in PRR; page39; page 160
	UBRR0 = 0;	//set the baud_rate to zero; page 189
	DDRA |= 1<<DDRA3;	//set PA3 as output; XCK0 must be set as output; page 187
	UCSR0C |= (1<<UMSEL00) | (1<<UMSEL01);	//enable SPI mode in USART0; page 195
	UCSR0C &= ~((1<<UDORD0) | (1<<UCPHA0) | (1<<UCPOL0));	//MSB first; clk phase = 0, clk polarity = 0; page 195
	UCSR0A &= ~(1<<U2X0);	//set to zero to use synchronous mode; probably not needed because operating in SPI mode; page 181
	UCSR0B |= (1<<TXEN0);	//enable receiver and transmitter; page 194
	UCSR0B &= ~(1<<RXEN0);	//disable receiver; page 194
	UBRR0 = baud_rate;	//set the baud_rate; baud_rate = 0 -> 1Mbps; page 180
}
*/