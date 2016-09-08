/*

DPS = Digital Phase Shifter

 */ 

#define F_CPU 16e6

#define PORT1 1
#define PORT2 2
#define PORT3 3
#define PORT4 4

#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/cpufunc.h>
#include <util/delay.h>

volatile uint8_t SPI_data = 0xF1;
const uint8_t LE_t = 1;

void SPI_init();	//user defined function; send cmd to DPS
void SPI_TX(uint8_t DPS_cmd, uint8_t bit_sh, uint8_t PORT);	//user defined function; bit shift is built in the function

void USART1_init();	//user defined function; receive cmd from bluetooth

int main(void){
	const uint16_t delay_t = 1000;
	
	volatile uint8_t bit_sh = 2;
	volatile uint8_t port_num = 4;
	
	cli();//Disable Global Interrupt
	SPI_init();
	//USART1_init();
	sei();	//Enable Global Interrupt
	
	//short pulse to execute the cmd received by the phase shifter
	DDRB |= 1<<DDB6;	//LE1; set port as output
	DDRB |= 1<<DDB5;	//LE2; set port as output
	DDRB |= 1<<DDB4;	//LE3; set port as output
	DDRB |= 1<<DDB7;	//LE4; set port as output
	
	DDRB |= 1<<DDB0;	//debug; set port as output
	
    while (1){				
		SPI_TX(SPI_data, bit_sh, port_num);		
		PINB |= 1<<PINB0;				
		_delay_ms(delay_t);
    }
}


//----------------------------user defined functions---------------------------------
void SPI_init(){	//initialize SPI as master
	PRR0 &= ~(1<<PRSPI); //enable SPI module in PRR; page 167; Page 43
	
	SPCR |= 1<<SPIE;	//enable SPI interrupt; page 171
	SPCR &= ~(1<<DORD);	//MSB to be transmitted first; page 171		
	SPCR |= (1<<MSTR);	//enable master mode; page 171
	SPCR &= ~(1<<CPOL | 1<<CPHA);	//SPI clk is low when idle; Data is valid on leading edge; page 171
	DDRB |= 1<<DDB1 | 1<<DDB2;	//set PB2/MOSI and PB1/SCK as output
									// MISO is override as Input; p168
	
	SPCR &= ~(1<<SPR1 | 1<<SPR0);
	SPSR |= 1<<SPI2X;	//set SPI CLK frequency; p172; f_clk = f_osc/2
									
	SPCR |= 1<<SPE;	//enable SPI module in SPI control Register; page 171
}

//DPS_cmd = desired phase shift
//bit_sh = number of bit shift (left) to the DPS_cmd
//PORT = one of the four phase shifter to have LE pulse applied
void SPI_TX(uint8_t DPS_cmd, uint8_t bit_sh, uint8_t PORT){	
	DPS_cmd = DPS_cmd << bit_sh;	//shift bit according to the phase shifter datasheet
	
	SPDR = DPS_cmd;	//place data to SPI data buffer to start sending the data
	//SPIF bit is set when a SPI transfer is complete; p158
	//SPIF bit is cleared by reading SPSR register with SPIF set, then accessing SPDR; page 158
	while(!(SPSR & (1<<SPIF))){
		;
	}
	
	//selectively apply LE pulse after data is transmitted	
	/* delay is required by the phase shifter, but the hardware cannot create a pulse that is as short as 1 cpu cycle
	   assuming the clk is running at 16MHz because of the parasitic capacitance; consider adding an amp as a buffer
	   to remove the charges faster;
	   _delay_loop_1(count) time = 1/CPU_clk*3*count; or 3 CPU_clk time per loop  */	
	if(PORT == PORT1){	//LE1
		PINB |= 1<<PINB6;	//toggle high
		_delay_loop_1(LE_t);
		//_NOP();	//delay by 1 cpu cycle
		PINB |= 1<<PINB6;	//toggle low
	} else if (PORT == PORT2){	//LE2
		PINB |= 1<<PINB5;	//toggle high
		_delay_loop_1(LE_t);
		PINB |= 1<<PINB5;	//toggle low
	} else if (PORT == PORT3){	//LE3
		PINB |= 1<<PINB4;	//toggle high		
		_delay_loop_1(LE_t);
		PINB |= 1<<PINB4;	//toggle low
	} else if (PORT == PORT4){	//LE4
		PINB |= 1<<PINB7;	//toggle high		
		_delay_loop_1(LE_t);
		PINB |= 1<<PINB7;	//toggle low
	}	
}

void USART1_init(uint8_t baud_rate){	
	PRR1 &= ~(1<<PRUSART1);	//enable USART module in PRR; page43
	UCSR1C &= ~((1<<UMSEL11) | (1<<UMSEL10));	//enable asynchronous mode in USART1; page 194
	UCSR1C &= ~((1<<UPM11)|(1<<UPM10));	//disable parity check; page 195
	UCSR1C &= ~(1<<USBS1);	//use 1 stop bit; page 195
	UCSR1C |= ((1<<UCSZ11) | (1<<UCSZ10));	//use 8 character per frame; page 195
	UCSR1B &= ~(1<<UCSZ12);	//use 8 character per frame; page 195
	UCSR1C &= ~(1<<UCPOL1);		//Clk polarity; write zero when using asynchronous mode; page 195
	UBRR1 = baud_rate;	//set the baud_rate; page 196
	UCSR1B |= 1<<RXCIE1;	//enable RX complete Interrupt; page 193	
	UCSR1B |= (1<<TXEN1);	//enable transmitter; page 194
	UCSR1B |= (1<<RXEN1);	//enable receiver; page 194	
}



//----------------------------Interrupt Routine---------------------------------
//SPIF bit is set when a serial transfer is complete; p158
//SPIF bit is cleared by hardware when the corresponding interrupt is served; page 158
ISR(SPI_STC_vect, ISR_BLOCK){	//SPI Transfer Complete ISR; blocking all other interrupts
	//send data to digital phase shifter here
	SPI_data = SPDR;		//read data from SPI buffer
	
	PINB |= 1<<PINB0;	//toggle PORT output
	_delay_ms(100);
	PINB |= 1<<PINB0;	//toggle PORT output
	_delay_ms(100);
	//received_signal = true;
}

