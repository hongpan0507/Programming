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
		# Relevant bits, flags and registers {
			@ SPRR = Pow Reduction Register {
				PRSPI = Power Reduction SPI;	
			}
			
			@ SPSR = SPI Staus Register {
				SPIF = end of Transmission Flag;	
			}												
			@ SPCR = SPI Control Register {
				SPIE = SPI Interrupt Enable;
				MSTR = SPI Master/Slave Enable;
				
			}			
			@ SPDR = SPI Data Register {
				
			}
		}
-------------------------------------------------------------------------------------------					
 */ 

#define F_CPU 16e6	//CPU clock must be defined first in order to use internal delay function
#include <avr/interrupt.h>
#include <avr/io.h>
#include <util/delay.h>


void SPI_init();	//initialize SPI module

volatile uint8_t data_in = 0;

int main(){		
	DDRA |= 1<<DDRA2;	//configure PA2 as output		
	SPI_init();	//initialize SPI module; user defined function
	
	uint8_t data_out[] = {0x15, 0xAB, 0x04, 0x45};	//SPI send data	
	uint8_t  count = 0;
	
	while(1){		
		if(count < sizeof(data_out)/sizeof(*data_out)){			
			SPDR = data_out[count];	//place data to SPI buffer
		} else {
			count = 0;
		}
		++count;	
		_delay_ms(1000);
	}
}

void SPI_init(){	//initialize SPI module
	sei();	//enable global interrupt; atmel built-in function
	PRR &= ~(1<<PRSPI); //enable SPI module in PRR; page 152; Page 39
	SPCR |= 1<<SPE;	//enable SPI module in SPI control Register; page 157
	SPCR |= 1<<SPIE;	//enable SPI interrupt; page 157; page 158
	SPCR &= ~(1<<DORD);	//MSB to be transmitted first; page 157
	SPCR &= ~(1<<MSTR);	//enable SPI slave mode; page 157	
	SPCR &= ~(1<CPOL);	//SPI clk is low when idle; page 158
	SPCR &= ~(1<CPHA);	//Data is valid on leading edge; page 158
	REMAP &= ~(1<SPIMAP);	//use default pin map; page 159
	//DDRA &= ~(1<<DDRA7);	//set PA7/SS as input; in slave mode, ss is always input; page 155
	DDRA |= 1<<DDRA5;	//set PA6/MISO as output
}

//SPIF bit is set when a serial transfer is complete; p158
//SPIF bit is cleared by hardware when the corresponding interrupt is served; page 158
ISR(SPI_vect, ISR_BLOCK){	//SPI interrupt service routine; blocking all other interrupts
	//send data to digital phase shifter here
}


//SPI slave; No Interrupt
/* 
int main(){
	uint8_t data_out[] = {0x15, 0xAB, 0x04, 0x45};	//SPI send data
	uint8_t data_in = 0;	//SPI receive data
	uint16_t delay_time = 1000;
	
	DDRA |= 1<<DDRA2;	//configure PA2 as output
	SPI_init();	//initialize SPI module; user defined function
	
	uint8_t  count = 0;
	
	while(1){
		
		if(count < sizeof(data_out)/sizeof(*data_out)){
			SPDR = data_out[count];	//place data to SPI buffer
			} else {
			count = 0;
		}
		++count;
		
		//SPIF bit is set when a serial transfer is complete; p158
		//SPIF bit is cleared by reading SPSR register with SPIF set, then accessing SPDR; page 158		
		while(!(SPSR & (1<<SPIF)))
		;
		data_in = SPDR;		//read data from SPI buffer
		//_delay_ms(1);
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
*/