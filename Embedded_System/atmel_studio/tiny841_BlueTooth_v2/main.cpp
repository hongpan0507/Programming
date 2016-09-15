/*
 * tiny841_BlueTooth.cpp
 * ECEN 452 final project
 * Created: 4/3/2016 9:04:18 PM
 * Author : hpan
 * All page numbers are referred to ATtiny 841 datasheet unless state otherwise
 * program function:		
		1. Receive command from PC via bluetooth (UART0 RX)
		2. Configure DAC via SPI
		3. measure the output of the DAC via ADC
		4. report the ADC measurement back to PC via bluetooth (UART0 TX)
		5. adjust DAC output based on the measurement from PNA
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
 * SPI programming notes:	 
	 # Output port must be defined as in Table 17-1 page 153
	 # disable SPI mode, change SPI parameter, enable SPI mode; follow this order or MASTER/SLAVE mode cannot be changed
	 # clear SPIF interrupt flag by reading status register and access SPI data register; page 158
 -------------------------------------------------------------------------------------------
 */

#define F_CPU 8e6	//CPU clock must be defined first in order to use internal delay function
#define UDORD0 2	//not defined by the header file; define manually; page 195
#define UCPHA0 1	//not defined by the header file; define manually; page 195
#define UCPOL0 0	//not defined by the header file; define manually; page 195

#include <avr/interrupt.h>
#include <avr/io.h>
#include <util/delay.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h> 

void UART_TX(uint8_t TX_data);	//send data using UART0
void SPI_init();	//initialize SPI module 
void USART0_init(uint8_t baud_rate);	//initialize SPI module
double ADC_init();	//initialize ADC parameter

volatile uint8_t data_flush = 0;	//useless data
volatile uint8_t data_in = 0;	//receive data
volatile uint8_t data_out[] = {0x15, 0xAB, 0x04, 0x45};	//send data	
volatile bool received_signal = false;	//flash LED

volatile uint8_t ADC_val[2];	//ADC conversion value; high, low
volatile double volt = 0;	//place as global only for debugging purpose
volatile double v_ref = 0;	//place as global only for debugging purpose

int main(){					
	uint16_t volt_data = 0;		
	 DDRA |= 1<<DDRA0;	//set PB2 as output to flash LED
	
	cli();	//disable global interrupt; atmel built-in function
	//set the baud_rate to 9600 assuming sys clk = 8MHz; page 180
	USART0_init(51);	//initialize USART0 module; user defined function;
	//SPI_init();	//initialize SPI module; user defined function
	//v_ref = ADC_init();	
	sei();	//enable global interrupt; atmel built-in function
			 
	while(1){			
		_delay_ms(1000);
		
		//ADCSRA |= 1<<ADSC;	//start ADC conversion; page 148
		//while(!(ADCSRA & (1<<ADIF))){	//ADIF is set if conversion is complete, and the data is ready for reading; page 148
			//;	//wait until the ADC conversion is done
		//}
		//ADC_val[0] = ADCL;	//read low bits first
		//ADC_val[1] = ADCH;		//read high bits; refer to programming notes for more information
		//ADCSRA |= (1<<ADIF); //clear ADIF; page 148
		//
		//volt_data = ADC_val[1];	// combine high bits and low bits
		//volt_data = volt_data << 8;	// combine high bits and low bits
		//volt_data |= ADC_val[0];	// combine high bits and low bits
		//
		//volt = 	v_ref * double(volt_data) / 1024.0;		// conversion formula; page	143	
						//
		//UART_TX(ADC_val[1]); //send high bits first
		//UART_TX(ADC_val[0]); //send low bits		
		 PINA |= 1<<PINA0;
		
		// UART_TX(0x24);
	}
}

//------------------------------Interrupt Service Routine--------------------------------------------------------------
ISR(USART0_RX_vect, ISR_BLOCK){	//USART1 Receive complete interrupt service routine	
	////send data to digital phase shifter here
	//data_in = UDR0;		//receive data from the USART1 receiver buffer; page 180		
	//UDR0 = data_in;		//place data to USART0 data buffer and initiate data transfer; provide feedback to check bluetooth command page 190	
	//PORTA &= ~(1<<PORTA7);	//ss low; start SPI transfer
	//SPDR = data_in;	//place data to SPI data buffer and send to the DAC	
	//while(!(UCSR0A & (1<<TXC0))){	//TXC0 bit is set if USART0 transfer is complete; page 193
		//;	// wait until USART0 TX transfer is completed
	//}	
	//while(!(SPSR & (1<<SPIF))){	//SPIF bit is set if SPI transfer is complete; page 158
		//;	// wait until SPI transfer is completed
	//}	
	//data_flush = SPDR;		//clear SPI interrupt flag; page 158
	//UCSR0A |= 1<<TXC0;	//clear USART0 transmit complete signal; page 193		
	//PORTA |= (1<<PORTA7);	//ss high; stop SPI transfer
	//send data to digital phase shifter here
	data_in = UDR0;		//receive data from the USART1 receiver buffer; page 180
	UDR0 = data_in;		//place data to USART0 data buffer and initiate data transfer; provide feedback to check bluetooth command page 190		
	while(!(UCSR0A & (1<<TXC0))){	//TXC0 bit is set if USART0 transfer is complete; page 193
		;	// wait until USART0 TX transfer is completed
	}
		
	UCSR0A |= 1<<TXC0;	//clear USART0 transmit complete signal; page 193
	
	received_signal = true;	
}

//---------------------------------------------------------------------------------------------------------------------

//------------------------------User Defined Functions--------------------------------------------------------------
void UART_TX(uint8_t TX_data){	//send data using UART0
	UDR0 = TX_data;	//place data to USART0 data buffer and initiate data transfer; provide feedback to check bluetooth command page 190	
	while(!(UCSR0A & (1<<TXC0))){	//TXC0 bit is set if USART0 transfer is complete; page 193
		;	// wait until USART0 TX transfer is completed
	}							
	UCSR0A |= 1<<TXC0;	//clear USART0 transmit complete signal; page 193
}

void SPI_init(){	//initialize SPI module		
	PRR &= ~(1<<PRSPI); //enable SPI module in PRR; page 152; Page 39
	SPCR &= ~(1<<SPE);	//disable SPI module in SPI control Register in order to make changes; page 157	
	SPCR &= ~(1<<DORD);	//MSB to be transmitted first; page 157
	SPCR |= (1<<MSTR);	//enable SPI master mode; page 157
	SPCR &= ~(1<CPOL);	//SPI clk is low when idle; page 158
	SPCR &= ~(1<CPHA);	//Data is valid on leading edge; page 158
	REMAP &= ~(1<SPIMAP);	//use default pin map; page 159		
	DDRA |= 1<<DDRA4;	//set PA4 as output to use as SCK
	DDRA |= 1<<DDRA6;	//set PA6 as output to use as MOSI
	DDRA |= 1<<DDRA7;	//set PA7 as output to use as SS	
	SPCR |= 1<<SPE;	//enable SPI module in SPI control Register; page 157	
}

void USART0_init(uint8_t baud_rate){	//initialize USART0 to operate in asynchronous mode
	PRR &= ~(1<<PRUSART0);	//enable USART0 module in PRR; page39; page 160
	REMAP |= 1 << U0MAP;	//remap USART0 to use alternative location; PA7, PB2; page 186
	UBRR0 = 0;	//set the baud_rate to zero; page 189	
	UCSR0C &= ~((1<<UMSEL00) | (1<<UMSEL01));	//enable USART0 in asynchronous mode; page 195
	UCSR0C |= (1<<UPM01)|(1<<UPM00);	//enable parity check; odd parity; page 183
	UCSR0C |= (1<<USBS0);	//select 1 stop bit; page 184
	UCSR0B &= ~(1<<UCSZ02);	//character size; set tp 8 bit; page 184
	UCSR0C |= (1<<UCSZ01)|(1<<UCSZ00);	//character size; set tp 8 bit; page 184
	UCSR0C &= ~(1<<UCPOL0);	//set to zero when using asynchronous mode; page 184	
	UCSR0C |= (1<<UDORD0);	//LSB first; page 195	
	UCSR0A &= ~(1<<U2X0);	//do no double transmission speed; page 181	
	UBRR0 = baud_rate;	//set the baud_rate; baud_rate = 0 -> 1Mbps; page 180
	UCSR0B |= 1<<RXCIE0;	//enable RX complete Interrupt; page 182
	//UCSR0D |= 1<<RXSIE0;	//enable RX start interrupt; page 185
	UCSR0B |= (1<<TXEN0);	//enable transmitter; page 182
	UCSR0B |= (1<<RXEN0);	//enable receiver; page 182
}

double ADC_init(){	//assuming the system clk is 16MHz; otherwise change prescaler; do not go over 200khz; page 135
	//ADC setting
	PRR &= ~(1<<PRADC);		//write logic 0 to enable ADC module; page38; page134
	ADMUXB &= ~(1<<REFS2 | 1<<REFS1 | 1<<REFS0);	//select Vcc as reference; page 146
	ADCSRA |= (1<<ADPS2 | 1<<ADPS1 | 1<<ADPS0);		//set ADC prescaler to 128; ADC freq = 16MHz/128=125KHz; page 148
	DIDR1 |= 1<<ADC8D;	//disable digital input on PB2; page 150
	
	// measure Vcc
	ADMUXA = 0; //clear ADMUXA setting
	ADMUXA = (1<<MUX3 | 1<<MUX2 | 1<<MUX0);	//select internal Vref = 1.1v as input; use it to measurement Vcc
	ADCSRA |= 1<<ADEN;	//enable ADC; page 148; page 134
	_delay_ms(2);	//require at least 1ms settling time; page 145
	
	ADCSRA |= 1<<ADSC;	//start ADC conversion; page 148
	while(!(ADCSRA & (1<<ADIF))){	//ADIF is set if conversion is complete, and the data is ready for reading; page 148
		;	//wait until the ADC conversion is done
	}
	ADC_val[0] = ADCL;	//read low bits first
	ADC_val[1] = ADCH;		//read high bits; refer to programming notes for more information
	ADCSRA |= (1<<ADIF); //clear ADIF; page 148
	//discard the first Vcc measurement; use the second one
	ADCSRA |= 1<<ADSC;	//start ADC conversion; page 148
	while(!(ADCSRA & (1<<ADIF))){	//ADIF is set if conversion is complete, and the data is ready for reading; page 148
		;	//wait until the ADC conversion is done
	}
	ADC_val[0] = ADCL;	//read low bits first
	ADC_val[1] = ADCH;		//read high bits; refer to programming notes for more information
	ADCSRA |= (1<<ADIF); //clear ADIF; page 148
	
	uint16_t ADC_data = 0;
	ADC_data |= ADC_val[1];
	ADC_data = ADC_data << 8;
	ADC_data |= ADC_val[0];
	double vcc = 1024.0 * 1.1/double(ADC_data);	//1024.0 = ADC resolution; 1.1=internal voltage reference;
	
	ADMUXA = 1<<MUX3;	//select PB2 (ADC8) as ADC input channel; page 134; pgae 144
	
	return vcc;
}

/*
void ADC_init(){	//assuming the system clk is 16MHz; otherwise change prescaler; do not go over 200khz; page 135
	PRR &= ~(1<<PRADC);		//write logic 0 to enable ADC module; page38; page134
	ADMUXB &= ~(1<<REFS2 | 1<<REFS1 | 1<<REFS0);	//select Vcc as reference; page 146
	ADCSRA |= (1<<ADPS2 | 1<<ADPS1 | 1<<ADPS0);		//set ADC prescaler to 128; ADC freq = 16MHz/128=125KHz; page 148
	DIDR1 |= 1<<ADC8D;	//disable digital input on PB2; page 150
	ADMUXA |= 1<<MUX3;	//select PB2 (ADC8) as ADC input channel; page 134; pgae 144
	ADCSRA |= 1<<ADEN;	//enable ADC; page 148; page 134
}
*/
//---------------------------------------------------------------------------------------------------------------------
