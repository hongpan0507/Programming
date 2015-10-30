/*************************Notes********************************
All page number is referred to ATtiny 85 datasheet unless state otherwise 
1. To run assembly in Arduino: __asm__("nop"); __asm__("ldi r16, 0x02"); 
2. To set a bit: bitwise or; Ex. PORTB |= 1 << PORTB3; pull PB3 high
3. To clear a bit: invert, then bitwise and; Ex. PORTB &= ~(1 << PORTB3); 
4. PB5 cannot be set as input when using arduino bootloader
5. When using three-wire mode as SPI, DO pin must be set as output manually if simultaneous receive and transmit is required; Ex. DDRB |= 1<<PORTB1; p117
6. In this code, CLK falling edge has been used to trigger SPI comm. SPI master needs to use MODE3
7. Data Structure: Byte0=0xFF(Start Delimiter); Byte1=Address; Byte2 = Data;
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


void spi_master_setup();
void spi_slave_setup();
void spi_transfer(uint8_t *DI, uint8_t *DO, boolean state);

int main(void){
  DDRB |= 1<<DDB3;  //set PB3 as output;  p55
  PORTB &= ~(1<<PORTB3);  //pull PB3 low

  DDRB |= 1<<DDB4;  //set PB4 as output; p55
  PORTB &= ~(1<<PORTB4);  //pull PB4 low  
  
  spi_slave_setup();
    
  uint8_t spi_start = 0;    
  uint8_t data_in = 0;
  uint8_t data_out = 0x90;
  uint8_t count = 0;
  uint8_t data_out_array[5] = {0xAB,0xCD,0xEF,0x01,0x02};
  uint8_t data_in_array[5] = {0x00,0x00,0x00,0x00,0x00};
  boolean count_trig = false;
  boolean data_trig = false;
  
  while (1) {           
    spi_start = USISR & (1<<USISIF);
    if(spi_start != 0){       //if start condition flag is set; spi transaction detection
      //PORTB |= 1<<PORTB3;    //pull PB4 high = turn on LED at PB4                      
      spi_transfer(&data_in_array[count], &data_out_array[count], SLAVE);  //spi transaction         
                       
      if(data_in_array[0] == 0xFF){  //detect start delimiter
        count_trig = true;    //start counting up
        data_in_array[0] = 0x00; //reset for start delimiter detection       
      }        
      if(count_trig == true){  //count up if start delimiter detected
        ++count;
      } 
      if(data_in_array[1] == 0x09){  //detect address              
        data_trig = true;    //if address is correct, start data collection
        data_in_array[1] = 0x00;  //reset for address detection           
      } else if(count == 2){  //if address is wrong, start over
        count_trig = false;  
        count = 0;
      }
      if(count == 5 && data_trig == true){ //process data; then start over   
        //PORTB |= 1<<PORTB3;    //pull PB3 high = enable high-z to isolate the arduino clk              
        if(data_in_array[2]==0xE6){
          PORTB |= 1<<PORTB4;    //pull PB4 high = turn on LED at PB4  
          _delay_ms(50);    
          if(data_in_array[3]==0x0C){
            PORTB &= ~(1<<PORTB4);  //pull PB4 low
            _delay_ms(50);    
            if(data_in_array[4]==0xFF){
              PORTB |= 1<<PORTB4;    //pull PB4 high = turn on LED at PB4  
              _delay_ms(50);    
            }
          }
        }
        data_trig = false;  
        count_trig = false;
        count = 0;                
      }           
    } else {
      PORTB &= ~(1<<PORTB4);  //pull PB4 low
      PORTB &= ~(1<<PORTB3);  //pull PB3 low
    }    
  }  
}

void spi_master_setup(){

}

void spi_slave_setup(){
  USICR &= ~(1<<USIWM1);  //three-wire mode; p117
  USICR |= 1<<USIWM0;  //three-wire mode; p117  
  DDRB |= 1<<PORTB1;  //use spi as bi-directional setup, set DO pin as output = receive and transmit at the same time; p117
  //DDRB &= ~(1<<PORTB1); //use spi as uni-directional setup, set DO pin as input = do not output any data when receving; p117
  
  USICR |= 1<<USICS1;  //External CLK; Positive edge; count both edges; p118
  USICR &= ~((1<<USICS0)|(1<<USICLK)); //External CLK; Positive edge; count both edges; p118
  
  USISR |= 1<<USISIF;  //clear Start Condition flag
  USISR |= 1<<USIOIF;  //clear counter overflow flag
}

/*
void spi_transfer(uint8_t *DI, uint8_t *DO, uint8_t array_size){  
  int8_t USI_SR = USISR & (1<<USIOIF);  //store overflow flag  
  for(uint8_t i=0; i<array_size; ++i){
    USIDR = *DO;  //store the content of DO to Data Reg
    ++DO;  ////increment array pointer
    while(USI_SR == 0){  //if overflow flag is not set
      USI_SR = USISR & (1<<USIOIF);
    }        
    *DI = USIBR;  //store data into array
    ++DI;  //increment array pointer
    USISR |= 1<<USIOIF;  //clear counter overflow flag
  }
  USISR |= 1<<USISIF;  //clear Start Condition flag
}*/

void spi_transfer(uint8_t *DI, uint8_t *DO, boolean state){
  USIDR = *DO;  //store the content of DO to Data Reg
  int8_t USI_SR = USISR & (1<<USIOIF);  //store overflow flag
  
  while(USI_SR == 0){
    if(state == true) USICR |= 1<<USITC;
    USI_SR = USISR & (1<<USIOIF);
  }
  
  /*
  do{
    if(state == true) USICR |= 1<<USITC;
    USI_SR = USISR & (1<<USIOIF);    
  }while(USI_SR == 0);  //if overflow flag is not set */
  
  *DI = USIBR;
  USISR |= 1<<USISIF;  //clear Start Condition flag
  USISR |= 1<<USIOIF;  //clear counter overflow flag
}
/*
void spi_transfer(uint8_t *DI, uint8_t *DO){  //state == master or slave
  USIDR = *DO;  //store the content of DO to Data Reg
  int8_t USI_SR = USISR & (1<<USIOIF);  //store overflow flag
  do{
    USI_SR = USISR & (1<<USIOIF);    
  }while(USI_SR == 0);  //if overflow flag is not set    
  *DI = USIBR;
  USISR |= 1<<USISIF;  //clear Start Condition flag
  USISR |= 1<<USIOIF;  //clear counter overflow flag
}*/


 /*********************Using C Style****************************************
 //------------------------Ex. 3: SPI transaction---------------------------
int main(void){
  DDRB |= 1<<DDB3;  //set PB3 as output;  p55
  PORTB &= ~(1<<PORTB3);  //pull PB3 low

  DDRB |= 1<<DDB4;  //set PB4 as output; p55
  PORTB &= ~(1<<PORTB4);  //pull PB4 low  
  
  spi_slave_setup();
    
  uint8_t spi_start = 0;    
  uint8_t data_in = 0;
  uint8_t data_out = 0xAB;
  
  while (1) {           
    spi_start = USISR & (1<<USISIF);
    if(spi_start != 0){       //if start condition flag is set
      PORTB |= 1<<PORTB4;    //pull PB4 high = turn on LED at PB4

      spi_transfer(&data_in, &data_out);
      
      if(data_in == 0x09){  //if the address = 0x09
        PORTB |= 1<<PORTB3;  //pull PB3 high = turn on LED at PB3
        _delay_ms(500);
      }
    } else {
      PORTB &= ~(1<<PORTB4);  //pull PB4 low
      PORTB &= ~(1<<PORTB3);  //pull PB3 low
    }    
  }  
}

void spi_slave_setup(){
  USICR &= ~(1<<USIWM1);  //three-wire mode; p117
  USICR |= 1<<USIWM0;  //three-wire mode; p117  
  DDRB |= 1<<PORTB1;  //use spi as bi-directional setup, set DO pin as output = receive and transmit at the same time; p117
  
  USICR |= 1<<USICS1;  //External CLK; Positive edge; count both edges; p118
  USICR &= ~((1<<USICS0)|(1<<USICLK)); //External CLK; Positive edge; count both edges; p118
  
  USISR |= 1<<USISIF;  //clear Start Condition flag
  USISR |= 1<<USIOIF;  //clear counter overflow flag
}

void spi_transfer(uint8_t *DI, uint8_t *DO){
  USIDR = *DO;  //store the content of DO to Data Reg
  int8_t USI_SR = USISR & (1<<USIOIF);  //store overflow flag
  while(USI_SR == 0){  //if overflow flag is not set
    USI_SR = USISR & (1<<USIOIF);
  }
  *DI = USIBR;
  USISR |= 1<<USISIF;  //clear Start Condition flag
  USISR |= 1<<USIOIF;  //clear counter overflow flag
}

 //-------Ex. 2; read from PortB0--------------
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
 //-------Ex. 1; flash LED-----------------
DDRB = 0b00001000;    // set PB3 to be output  
while (1) {
  // flash# 2:
  // set PB3 high
  PORTB = 0b00001000; 
  _delay_ms(500);
  // set PB3 low
  PORTB = 0b00000000;
  _delay_ms(500);
}
 ********************************************************************************/
/*********************Using Arudino Style****************************************
  init();  //must be called before using arduino function; declared in Arduino.h; defined in wiring.c
  int led = 0;
  pinMode(led, OUTPUT);
  
  for(;;){
    digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000);               // wait for a second
    digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
    delay(1000);
  }
 ********************************************************************************/

