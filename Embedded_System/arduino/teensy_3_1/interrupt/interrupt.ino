/* Notes:  Teensy 3.1
1. MK20DX256VLH7 Interrupt function and Definitions of interrupt variable: 
   C:\Program Files\Arduino\hardware\teensy\cores\teensy3\kinetis.h
   look up kinetis.h and mk20dx128.c when program interrupt
2. Teensy 3.1 PIT clk frequency = Bus Clk (48 MHz?);
   freescale MK20DX page 161; table 5-2
  
3. MK20DX256VLH7 Timer Interrupt steps: 
   enable the clk in system clk gating control
   enable PIT
   set timer load value
   select chain mode, enable Timer Interrupt, enable Timer
   enable globe interrupt
   Timer Flag Register must be cleared at the end of each interrupt routine
4. 

*/

#include <avr/io.h>
#include <avr/interrupt.h> //C:\Program Files\Arduino\hardware\tools\avr\avr\include\avr
#include <kinetis.h>

int test = 0;
int current_time = 0;
int led = 13;

void setup() {
  Serial.begin(9600);
  timer0_interrupt();
  pinMode(led, OUTPUT); 
}

void loop() {
  debug();
  delay(1000);
}

void pit0_isr(void){  
  if(test == 1) {
    test = 0;
    digitalWrite(led,LOW);
  } else {
    ++test;  
    digitalWrite(led,HIGH);        
  }  
  current_time = millis();
  Serial.print("Test = ");  
  Serial.println(test);
  Serial.print("Time = ");  
  Serial.println(current_time);
  
  //Timer Flag Register; Timer Interrupt Flag (TIF) must be set to 1 to clear the flag                   
  PIT_TFLG0 = 1;   //very important!!!
}

void timer0_interrupt(){  
  SIM_SCGC6 |= 0x800000;  //System Clk Gating Control Register 6; PIT is on bit 23; freescale MK20DX page 256 and page 160  
  PIT_MCR = 0x00;  //0x(PIT enabled, Timer run in Debug mode); freescale MK20DX page 904
  PIT_LDVAL0 = 47999999;  //timer 0 load value = 48M in hex; timer counts down; freescale MK20DX page 904
  PIT_TCTRL0 = 0x03;  // 0x(Chain Mode, Timer Interrupt Enable, Timer Enable); freescale MK20DX page 905
  //PIT_CVAL0 has the value of the current timer; freescale MK20DX page 905
  NVIC_ENABLE_IRQ(IRQ_PIT_CH0);  //enable interrupt;   
}

void debug(){
  //PIT Module Control Register
  Serial.print("PIT_MCR = ");
  Serial.println(PIT_MCR);
  //PIT timer 0 load value
  Serial.print("PIT_LDVAL0 =");
  Serial.println(PIT_LDVAL0);
  //PIT Current Value
  Serial.print("PIT_CVAL0 =");
  Serial.println(PIT_CVAL0);
  //PIT Timer Control Register
  Serial.print("PIT_TCTRL0 = ");
  Serial.println(PIT_TCTRL0);
  //PIT Timer Flag Register
  Serial.print("PIT_TFLG0 = ");
  Serial.println(PIT_TFLG0);
  
  //-----------------Configuration of OSC-------------------------------------------------------------------
  //OSC Control Register
  //output = 10 -> Add 2 pF capacitor to the oscillator load
  //            -> Add 8 pF capacitor to the oscillator load 
  Serial.print("OSC0_CR = ");
  Serial.println(OSC0_CR);  //freescale MK20DX page 527;
  //---------------------------------------------------------------------------------------------------------
  //------------------Multiple-Purpose Clock Generator (MCG) frequency---------------------------------------------------
  //combine the following register setting and diagram on page 488 and page 156 to figure out MCG frequency
  //MCGOUTCLK = 16MHz OSC * 24 /4 = 96 MHz; Teensy 3.1 has 16MHz OSC as external reference clock
  //MCG Control 1 Register
  //output = 32 -> Output of FLL or PLL is selected
  Serial.print("MCG_C1 = ");
  Serial.println(MCG_C1);  //freescale MK20DX page 490;
  //MCG Control 6 Register
  //output = 64 -> PLL is selected
  //Multiply Factor = 24 because VDIV0 = 0;
  Serial.print("MCG_C6 = ");
  Serial.println(MCG_C6);  //freescale MK20DX page 496;
  //MCG Control 5 Register
  //Output = 3 -> PRDIV0 = 4 -> Dividing Factor = 4;
  Serial.print("MCG_C5 = ");
  Serial.println(MCG_C5);  //freescale MK20DX page 495;
  //MCG Status Register
  //output = 110 -> source of PLL is PLL clock
  Serial.print("MCG_S = ");
  Serial.println(MCG_S);  //freescale MK20DX page 497; 
 //--------------------------------------------------------------------------------------------------------  
 //--------------------System Intergration Module (SIM) Output Frequency-----------------------------------
 //combine the following register setting and page 156 to figure out System_Clk/Bus_Clk frequency
 // Page 160; Chapter 5.7, Module Clocks has info of the clk of different peripherals; i.e PIT uses Bus Clk
 //System Clock Divider Register 1 
 //ouput =  16973824 
 //OUTDIV1 = b0000 -> divide-by-1 -> Core/System Clk = 96MHz/1
 //OUTDIV2 = b0001 -> divide-by-2 -> Bus Clk =  = 96MHz/2
 //OUTDIV4 = b0011 -> divide-by-4 -> Flash Clk = 96MHz/4
  Serial.print("SIM_CLKDIV1 = ");
  Serial.println(SIM_CLKDIV1);  //freescale MK20DX page 259;  
 //-------------------------------------------------------------------------------------------------------  
     
  delay(100); 
}
