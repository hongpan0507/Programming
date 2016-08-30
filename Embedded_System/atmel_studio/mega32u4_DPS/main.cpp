/*

DPS = Digital Phase Shifter

 */ 

#define F_CPU 16e6

#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/cpufunc.h>
#include <util/delay.h>

volatile uint8_t SPI_data = 0xF1;

void SPI_init();	//user defined function; send cmd to DPS
void SPI_send(uint8_t DPS_cmd, uint8_t bit_sh);	//user defined function; bit shift is built in the function

int main(void){
	const uint16_t delay_t = 1000;
	volatile uint8_t bit_sh = 2;
	
	SPI_init();
	
	//short pulse to execute the cmd received by the phase shifter
	//DDRB |= 1<<DDB6;	//LE1; set port as output
	//DDRB |= 1<<DDB5;	//LE2; set port as output
	//DDRB |= 1<<DDB4;	//LE3; set port as output
	//DDRB |= 1<<DDB7;	//LE4; set port as output
	
	DDRB |= 1<<DDB0;	//debug; set port as output
	
    while (1){				
		SPI_send(SPI_data, bit_sh);		
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

//send cmd to DPS
void SPI_send(uint8_t DPS_cmd, uint8_t bit_sh){	//bit_sh = number of bit shift (left) to the DPS_cmd
	DPS_cmd = DPS_cmd << bit_sh;	
	SPDR = DPS_cmd;	//place data to SPI data buffer
	//SPIF bit is set when a SPI transfer is complete; p158
	//SPIF bit is cleared by reading SPSR register with SPIF set, then accessing SPDR; page 158
	while(!(SPSR & (1<<SPIF))){
		;
	}
	//_NOP();	//delay by 1 cpu cycle
	PINB |= 1<<PINB4;	//pull LE3 pin high
	_delay_us(1);
	PINB |= 1<<PINB4;	//pull LE3 pin low
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