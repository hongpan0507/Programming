#include "Arduino.h"
#include "interface.h"
#include "SPI.h"
#include "Ethernet.h"

interface::interface(int pin) {
	pinMode(pin, OUTPUT);
        ledpin = pin;		
}

void interface::serialConnect(){
	char val;
	
	if(Serial.available()){
		val = Serial.read();
	
		if(val == 'H'){
			digitalWrite(ledpin, HIGH);
		}else if(val == 'L'){
			digitalWrite(ledpin,LOW);
		}
		else{
			Serial.println("Invalid Input");
		}
	}
}

void interface::ethernetConnect(int port){
	_port = port;
	EthernetServer server(_port);	
	boolean incoming = 0;
	
	EthernetClient client = server.available();  
	
	if (client) {
    incoming=0;
    
    while (client.connected()) {
      if (client.available()) {
		char c = client.read();
        
        if(incoming && c == ' '){ 
          break;
        }  
        
        if(c == '/'){ 
          incoming = 1; 
        } 
		
        if(incoming == 1){
          if(c == '1'){
            Serial.println("ON");
            digitalWrite(ledpin, HIGH); 
            break;        
          }
          if(c == '2'){
            Serial.println("OFF");
            digitalWrite(ledpin, LOW);
            break;
          }     
        }
      }
    }
    delay(1);
    client.stop();
    Serial.println("Client stopped");
  }
}