/*
 * tiny841_DPS.cpp
 *
 * Created: 11/9/2015 11:12:52 AM
 * Author : hpan
 * All page numbers are referred to ATtiny 841 datasheet unless state otherwise
 -------------------------------------------------------------------------------------------
 * Tiny841 Device Programming Notes:
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
 * Tiny841 Device Setting:
	 # Fuse {
		 Extended = 0xFF;
		 High = 0xD7;
		 Low = 0xC2;
	 }
	 # Lock Bit = 0xFF
-------------------------------------------------------------------------------------------
* Digital Phase shifter Note:	 
	# The 4-bit shifter must have D2, D1 data when using SPI mode{	
		use 0b00 as dummy bits for D2,D1 will work;
		When coding, use normal number, but left_shift 2 bit the spi command
		refer to the datasheet for more details
	}
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
	 
* USART0 in SPI mode:
	# f_max = f_cpu/2;
	# only master mode is supported; page 187
	 
 * I2C programming notes:
	# tiny841 only implements slave functionality; page 197
	# 7-bit and 10-bit addressing are supported; page 197
	# pull-up resistors are required
	
 * USART programming notes:
	 #	Clk_ext < Clk_osc/4;	// external clk speed limit in slave synchronous mode; page 163
	 # double speed available for asynchronous mode	 
 -------------------------------------------------------------------------------------------
 */

 #define F_CPU 16e6	//CPU clock must be defined first in order to use internal delay function
 #define UDORD0 2	//not defined by the header file; define manually; page 195
 #define UCPHA0 1	//not defined by the header file; define manually; page 195
 #define UCPOL0 0	//not defined by the header file; define manually; page 195

 #include <avr/interrupt.h>
 #include <avr/io.h>
 #include <util/delay.h>

 
 void SPI_init();	//initialize SPI module
 void I2C_init(uint8_t slave_addr);	//initialize I2C module
 void USART1_init(uint8_t baud_rate);	//initialize USART1 module
 void USART0_SPI_init(uint8_t baud_rate);	//initialize SPI module

 volatile uint8_t data_in = 0;	//receive data
 volatile uint8_t data_out[] = {0x15, 0xAB, 0x04, 0x45};	//send data
 volatile bool received_signal = false;	//flash LED

int main(){
	DDRB |= 1<<DDRB2;	//set PB2 as output to flash LED
	DDRA |= 1<<DDRA0;	//set PA0 as output to apply change to the digital phase shifter	
	PORTA &= ~(1<<PORTA0);	//pull PA0 low	
	
	cli();	//disable global interrupt; atmel built-in function
	USART0_SPI_init(0);	//initialize USART0 module; user defined function; set the baud_rate to 1Mbps; page 180
	//USART1_init(103);	//initialize USART1 module; user defined function; set the baud_rate to 9600; page 179
	I2C_init(0x08);		//initialize I2C module with address = 0x08; user defined function
	//SPI_init();	//initialize SPI module; user defined function
	sei();	//enable global interrupt; atmel built-in function
		 
	while(1){
		if(received_signal){
			received_signal = false;
			PINB |= 1<<PINB2;	//toggle PORTB2
			_delay_ms(100);
			PINB |= 1<<PINB2;	//toggle PORTB2
			_delay_ms(100);
		}
	}
}

//------------------------------Interrupt Service Routine--------------------------------------------------------------
//SPIF bit is set when a serial transfer is complete; p158
//SPIF bit is cleared by hardware when the corresponding interrupt is served; page 158
ISR(SPI_vect, ISR_BLOCK){	//SPI interrupt service routine; blocking all other interrupts
	//send data to digital phase shifter here
	data_in = SPDR;		//read data from SPI buffer
	UDR0 = data_in;		//place data to USART0 data buffer and initiate data transfer; page 190
	while(!(UCSR0A & (1<<TXC0))){	//TXC0 bit is set if USART0_SPI transfer is complete; page 193
		;
	}
	UCSR0A |= 1<<TXC0;	//clear USART0_SPI transmit complete signal; page 193
	received_signal = true;
}

ISR(TWI_SLAVE_vect, ISR_BLOCK){	//I2C interrupt service routine; blocking all other interrupts
	//send data to digital phase shifter here
	if(TWSSRA & (1<<TWASIF)){	//address/stop detection; page 206
		if(TWSSRA & (1<<TWAS)){		//address detection; page 207
			TWSCRB &= ~(1<<TWAA);	//send ACK; page 206
			TWSCRB |= ((1<<TWCMD0) | (1<<TWCMD1));		//ACK + clear TWI Address/Stop Interrupt Flag; page 206
		}
	}
	if(TWSSRA & (1<<TWDIF)){	//data receive complete detection; page 207
		TWSCRB |= 1<<TWAA;	//send NACK; page 206
		data_in = TWSD;		//automatic NACK in smart mode; page 206
		
		UDR0 = data_in<<2;		//place data to USART0 data buffer and initiate data transfer to the phase shifter; page 190; why left shift 2 bits: refer to digital phase shifter note
		while(!(UCSR0A & (1<<TXC0))){	//TXC0 bit is set if USART0_SPI transfer is complete; page 193
			;
		}				
		UCSR0A |= 1<<TXC0;	//clear USART0_SPI transmit complete signal; page 193
		TWSSRA |= 1<<TWDIF;		//clear TWI data interrupt flag; page 207
		PORTA |= (1<<PORTA0);	//pull PA0 high; apply changes
		_delay_us(1);	//delay required for the phase shifter 
		PORTA &= ~(1<<PORTA0);	//pull PA0 low; apply changes	
	}
	received_signal = true;
}

ISR(USART1_RX_vect, ISR_BLOCK){	//USART1 Receive complete interrupt service routine	
	//send data to digital phase shifter here
	data_in = UDR1;		//receive data from the USART1 receiver buffer; page 180
	UDR0 = data_in;		//place data to USART0 data buffer and initiate data transfer; page 190
	while(!(UCSR0A & (1<<TXC0))){	//TXC0 bit is set if USART0_SPI transfer is complete; page 193
		;
	}
	UCSR0A |= 1<<TXC0;	//clear USART0_SPI transmit complete signal; page 193
	received_signal = true;	
}

ISR(USART1_START_vect, ISR_BLOCK){	//USART1 start condition detection interrupt service routine
	if(UCSR1A & (1<<UDRE1)){	//check if the USART1 buffer is empty; page 181
		UDR1 = data_out[1];	//place data to the USART1 transmiter buffer; page 180
	}
	UCSR1D |= 1<<RXS1;	//clear start condition detection flag; page 185
}
//---------------------------------------------------------------------------------------------------------------------

//------------------------------User Defined Functions--------------------------------------------------------------
void USART1_init(uint8_t baud_rate){	//initialize USART1 module as asynchronous slave mode  
	PRR &= ~(1<<PRUSART1);	//enable USART1 module in PRR; page39; page 160		
	UCSR1C &= ~((1<<UMSEL11) | (1<<UMSEL10));	//enable asynchronous mode in USART1; page 183
	UCSR1C &= ~((1<<UPM11)|(1<<UPM10));	//disable parity check; page 184
	UCSR1C &= ~(1<<USBS1);	//use 1 stop bit; page 184
	UCSR1C |= ((1<<UCSZ11) | (1<<UCSZ10));	//use 8 character per frame; page 184
	UCSR1B &= ~(1<<UCSZ12);	//use 8 character per frame; page 184
	UCSR1C &= ~(1<<UCPOL1);		//Clk polarity; write zero when using asynchronous mode; page 184
	UBRR1 = baud_rate;	//set the baud_rate; page 179
	UCSR1B |= 1<<RXCIE1;	//enable RX complete Interrupt; page 182
	UCSR1D |= 1<<RXSIE1;	//enable RX start interrupt; page 185
	UCSR1B |= (1<<TXEN1);	//enable receiver; page 182
	UCSR1B |= (1<<RXEN1);	//enable receiver; page 182
}

void I2C_init(uint8_t slave_addr){	//initialize I2C module
	PRR &= ~(1<<PRTWI); //enable TWI module in PRR; page 152; page 39
	TWSCRA |= 1<<TWEN;	//enable Two-Wire imterface in slave mode; page 205
	TWSCRA |= 1<<TWDIE;	//enable TWI data interrupt; page 205
	TWSCRA |= 1<<TWASIE;	//enable TWI Address/Stop interrupt; page 205
	TWSCRA |= 1<<TWSME;	//enable TWI smart mode; automatic NACK after a data package is received; page 205
	TWSA = slave_addr<<1;	//7-bit address; setting the bit 0 enables general call address recognition logic; not used this in case; page 208
}

void SPI_init(){	//initialize SPI module
	PRR &= ~(1<<PRSPI); //enable SPI module in PRR; page 152; Page 39
	SPCR |= 1<<SPE;	//enable SPI module in SPI control Register; page 157
	SPCR |= 1<<SPIE;	//enable SPI interrupt; page 157; page 158
	SPCR &= ~(1<<DORD);	//MSB to be transmitted first; page 157
	SPCR &= ~(1<<MSTR);	//enable SPI slave mode; page 157
	SPCR &= ~(1<CPOL);	//SPI clk is low when idle; page 158
	SPCR &= ~(1<CPHA);	//Data is valid on leading edge; page 158
	REMAP &= ~(1<SPIMAP);	//use default pin map; page 159
	DDRA &= ~(1<<DDRA7);	//set PA7/SS as input; in slave mode, ss is always input; probably not needed; page 155
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
//---------------------------------------------------------------------------------------------------------------------

