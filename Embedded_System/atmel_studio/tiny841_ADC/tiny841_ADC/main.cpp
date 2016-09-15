/*
 * tiny841_ADC.cpp
 *
 * Created: 4/9/2016 10:25:14 AM
 * Author : hpan
 ---------------------------------------------------------
 ADC Programming Notes:
	# 10-bit resolution
	# ADC minimum value represents GND; max represents reference voltage; page 134	
	# ADC from Power Reduction bit must be disabled (logic 0) in order to use ADC; page 134
	# select ADC input channel from ADMUXA; page 134
	# if multiple channels are used, select each channel before doing conversion and reading data
	# Write logical one to ADC start conversion bit to trigger a conversion; page 134
	# For right adjusted data, read Lower bits first, then higher bits; page 147
 */ 

#define F_CPU 16e6	//CPU clock must be defined first in order to use internal delay function

#include <avr/io.h>
#include <util/delay.h>

double ADC_init();	//initialize ADC parameter

volatile uint8_t ADC_val[2];	//ADC conversion value; high, low

int main(void){	
	double volt = 0;
	uint16_t volt_data = 0;
	
    double v_ref = ADC_init();	
	
    while (1){
		_delay_ms(500);
		ADCSRA |= 1<<ADSC;	//start ADC conversion; page 148
		while(!(ADCSRA & (1<<ADIF))){	//ADIF is set if conversion is complete, and the data is ready for reading; page 148
			;	//wait until the ADC conversion is done
		}
		ADC_val[0] = ADCL;	//read low bits first
		ADC_val[1] = ADCH;		//read high bits; refer to programming notes for more information
		ADCSRA |= (1<<ADIF); //clear ADIF; page 148
		
		volt_data = ADC_val[1];
		volt_data = volt_data << 8;
		volt_data |= ADC_val[0];
		volt = 	v_ref * double(volt_data) / 1024.0;	
    }
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
