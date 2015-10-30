/*************************Notes********************************
All page number is referred to ATtiny 85 datasheet unless state otherwise 
1. To run assembly in Arduino: __asm__("nop"); __asm__("ldi r16, 0x02"); 
2. To set a bit: bitwise or; Ex. PORTB |= 1 << PORTB3; pull PB3 high
3. To clear a bit: invert, then bitwise and; Ex. PORTB &= ~(1 << PORTB3); 
4. PB5 cannot be set as input when using arduino bootloader
5. When using three-wire mode as SPI, DO pin must be set as output manually if simultaneous receive and transmit is required; Ex. DDRB |= 1<<PORTB1; p117
6. In this code, CLK falling edge has been used to trigger SPI comm. SPI master (Not ATtiny85) needs to use MODE3
7. ATtiny85 SPI is compatible with SPI mode0 and mode3
***************************************************************/

#include <stdlib.h>
#include <inttypes.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <avr/io.h>

#define PINB5_set 0x20
#define PINB4_set 0x10
#define PINB3_set 0x08
#define PINB2_set 0x04
#define PINB1_set 0x02
//#define PINB0_set 0x01

#define MASTER true
#define SLAVE false
#define MODE0 0
#define MODE3 3

void spi_setup();
void spi_master_setup();
void spi_slave_setup();
void spi_transfer(uint8_t *DI, uint8_t *DO, boolean state);

int main(void){
  DDRB |= 1 << DDB3;  //set PB3 as output
  PORTB |= 1 << PORTB3;  //pull PB3 high
  
  DDRB &= ~(1 << DDB0);  //set PB0 as input
  PORTB &= ~(1 << PORTB0);   //PB0 = input, No pull-up, tri-state;  p55
  
  int8_t PB0_in = 0;    
    
  while (1) {    
    PB0_in = PINB;   //read Input Pin  
            
    if(PB0_in == 1){       //check input to PB0 
      PORTB |= 1 << PORTB3;  //pull PB3 high
    } else {
      PORTB &= ~(1 << PORTB3);  //pull PB3 low
    }      
  }
}
