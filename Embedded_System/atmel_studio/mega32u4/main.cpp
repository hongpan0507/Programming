/*
Digital Phase Shifter

Data Format received from BlueTooth through USART: 
	"0xFF0xAA0xBB0xCC"
		0xFF == cmd start detection (cannot have phase shift of "0xFF")
		0xAA == Address (board level)
		0xBB == PORT # (DPS Chip)
		0xCC == DPS cmd (phase shift)
	
Data Format send to DPS chip by SPI:
	void SPI_TX(uint8_t PORT, uint8_t DPS_cmd, uint8_t bit_sh)
		PORT = one of the four phase shifter to have LE pulse applied
		DPS_cmd = desired phase shift
		bit_sh = number of bit shift (left) to the DPS_cmd
		
	

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

const uint8_t DPS_addr = 0x05;	//DPS hard coded address

uint8_t usart_byte_count = 0;	//count the # of bytes received through usart
bool cmd_start = false;		//start of cmd detection
uint8_t dest_addr = 0x00;	//DPS hard coded address
uint8_t port_num = 0;	//DPS port number
const uint8_t bit_sh = 2;	//digital phase shifter data bit shift

uint8_t data_dump = 0;	//flush usart buffer

volatile uint8_t LE1_led = 0;
volatile uint8_t LE2_led = 0;
volatile uint8_t LE3_led = 0;
volatile uint8_t LE4_led = 0;

const uint8_t LE_t = 1;		//LE pulse width
const uint8_t LEx_led_t = 50;		//LE pulse width

void SPI_init();	//user defined function; send cmd to DPS
void SPI_TX(uint8_t PORT, uint8_t DPS_cmd, uint8_t bit_sh);	//user defined function; bit shift is built in the function

void USART1_init(uint8_t baud_rate);	//user defined function; receive cmd from bluetooth
void USART1_TX(uint8_t TX_byte);	//user defined function; test USART1 comm

int main(void){
	const uint16_t delay_t = 1000;	//Debug LED flash
	bool less_delay = false;	//compensate for LEx_led delay
	
	cli();//Disable Global Interrupt
	SPI_init();
	USART1_init(103);	//9600 baud rate
	sei();	//Enable Global Interrupt
	
	//set port as output
	//short pulse to execute the cmd received by the phase shifter
	DDRB |= 1<<DDB6;	//LE1 pulse
	DDRB |= 1<<DDB5;	//LE2 pulse
	DDRB |= 1<<DDB4;	//LE3 pulse
	DDRB |= 1<<DDB7;	//LE4 pulse
	
	//LED flashes after LE1 pulse is applied
	DDRE |= 1<<DDE6;	//PE6; LE1 LED
	DDRC |= 1<<DDC7;	//PC7; LE2 LED
	DDRC |= 1<<DDC6;	//PC6; LE3 LED
	DDRD |= 1<<DDD7;	//PD7; LE4 LED
	
	DDRB |= 1<<DDB0;	//debug; set port as output
	
	DDRD |= 1<<DDD5;	//set as output
	PORTD |= 1<<DDD5;	//turn off LED
	
    while (1){							
		PINB |= 1<<PINB0;		
		
		USART1_TX(0x15);
		
		if(LE1_led == 1){
			LE1_led = 0;
			PINE |= 1<<PINE6;	//turn on
			_delay_ms(LEx_led_t);
			PINE |= 1<<PINE6;	//turn off
			less_delay = true;
		}
		if(LE2_led == 1){
			LE2_led = 0;
			PINC |= 1<<PINC7;	//turn on
			_delay_ms(LEx_led_t);
			PINC |= 1<<PINC7;	//turn off
			less_delay = true;
		}
		if(LE3_led == 1){
			LE3_led = 0;
			PINC |= 1<<PINC6;	//turn on
			_delay_ms(LEx_led_t);
			PINC |= 1<<PINC6;	//turn off
			less_delay = true;
		} 
		if(LE4_led == 1){
			LE4_led = 0;
			PIND |= 1<<PIND7;	//turn on
			_delay_ms(LEx_led_t);
			PIND |= 1<<PIND7;	//turn off
			less_delay = true;
		}				
		
		if(less_delay){
			_delay_ms(delay_t-LEx_led_t);	
			less_delay = false;
		} else{
			_delay_ms(delay_t);	
		}
    }
}


//----------------------------user defined functions---------------------------------
void SPI_init(){	//initialize SPI as master
	PRR0 &= ~(1<<PRSPI); //enable SPI module in PRR; page 167; Page 43
	
	//Do not enable interrupt if not necessary
	//SPCR |= 1<<SPIE;	//enable SPI interrupt; page 171
	SPCR &= ~(1<<DORD);	//MSB to be transmitted first; page 171		
	SPCR |= (1<<MSTR);	//enable master mode; page 171
	SPCR &= ~(1<<CPOL | 1<<CPHA);	//SPI clk is low when idle; Data is valid on leading edge; page 171
	DDRB |= 1<<DDB1 | 1<<DDB2;	//set PB2/MOSI and PB1/SCK as output
									// MISO is override as Input; p168
	
	SPCR &= ~(1<<SPR1 | 1<<SPR0);
	SPSR |= 1<<SPI2X;	//set SPI CLK frequency; p172; f_clk = f_osc/2
									
	SPCR |= 1<<SPE;	//enable SPI module in SPI control Register; page 171
}

//PORT = one of the four phase shifter to have LE pulse applied
//DPS_cmd = desired phase shift
//bit_sh = number of bit shift (left) to the DPS_cmd
void SPI_TX(uint8_t PORT, uint8_t DPS_cmd, uint8_t bit_sh){	
	DPS_cmd = DPS_cmd << bit_sh;	//shift bit according to the phase shifter datasheet
	
	SPDR = DPS_cmd;	//place data to SPI data buffer to start sending the data
	//SPIF bit is set when a SPI transfer is complete; p158
	//SPIF bit is cleared by reading SPSR register with SPIF set, then accessing SPDR; page 172
	while(!(SPSR & (1<<SPIF))){
		;
	}
	data_dump = SPDR;	//clear SPIF bit
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
		LE1_led = 1;
	} else if (PORT == PORT2){	//LE2
		PINB |= 1<<PINB5;	//toggle high
		_delay_loop_1(LE_t);
		PINB |= 1<<PINB5;	//toggle low
		LE2_led = 1;
	} else if (PORT == PORT3){	//LE3
		PINB |= 1<<PINB4;	//toggle high		
		_delay_loop_1(LE_t);
		PINB |= 1<<PINB4;	//toggle low
		LE3_led = 1;
	} else if (PORT == PORT4){	//LE4
		PINB |= 1<<PINB7;	//toggle high		
		_delay_loop_1(LE_t);
		PINB |= 1<<PINB7;	//toggle low
		LE4_led = 1;
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

void USART1_TX(uint8_t TX_byte){
	UDR1 = TX_byte;		//place data to USART1 data buffer and initiate data transfer; page
	while(!(UCSR1A & (1<<TXC1))){	//TXC1 bit is set if USART1 transfer is complete; page 
		;
	}
	UCSR1A |= 1<<TXC1;	//clear USART1 transmit complete signal; page 
}

//----------------------------Interrupt Routine---------------------------------
//USART1 Receive complete interrupt service routine
//clear RXCn bit by reading receiver buffer, UDR1
//send data using SPI to digital phase shifter here
ISR(USART1_RX_vect, ISR_BLOCK){		
	++usart_byte_count;		//expect to receive 4 commands
	uint8_t RX_byte = UDR1;	//read data from USART1 buffer
	if(usart_byte_count == 1){
		if(RX_byte == 0xFF){	//cmd sync
			cmd_start = true;
		} else {	//reset count if no start of cmd detected
			usart_byte_count = 0;
		}
	} else if(cmd_start){
		if(usart_byte_count == 2){		// second byte contains address
			if(RX_byte != DPS_addr){	//if address does not match
				usart_byte_count = 0;	//restart	
				cmd_start = false;
			}
		} else if(usart_byte_count == 3){	//port number
			port_num = RX_byte;	//read port number
		} else if(usart_byte_count == 4){				//phase shift		
			//read data from USART buffer 1 then send to DPS chip										
			SPI_TX(port_num, RX_byte, bit_sh);		
			usart_byte_count = 0;
			cmd_start = false;
		}	//end of else if
	}	//end of else if
}	//end of ISR

//ISR(USART1_RX_vect, ISR_BLOCK){
	//++usart_byte_count;		//expect to receive 4 commands
	////uint8_t RX_byte = UDR1;	//read data from USART1 buffer
	//if(usart_byte_count == 1){
		//if(UDR1 == 0xFF){	//cmd sync
			//cmd_start = true;
			//} else {	//reset count if no start of cmd detected
			//usart_byte_count = 0;
		//}
		//} else if(cmd_start){
		//if(usart_byte_count == 2){		// second byte contains address
			//if(UDR1 != DPS_addr){	//if address does not match
				//usart_byte_count = 0;	//restart
				//cmd_start = false;
			//}
			//} else if(usart_byte_count == 3){	//port number
			//port_num = UDR1;	//read port number
			//} else if(usart_byte_count == 4){				//phase shift
			////read data from USART buffer 1 then send to DPS chip
			//SPI_TX(port_num, UDR1, bit_sh);
			//usart_byte_count = 0;
			//cmd_start = false;
		//}	//end of else if
	//}	//end of else if
//}	//end of ISR
