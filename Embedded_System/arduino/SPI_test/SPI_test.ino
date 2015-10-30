#include <SPI.h>
#include <stdlib.h>


using namespace std;

//int SPI_CS = 4000000; //125kHz = arudino  //SPI clock speed; DW1000 datasheet p23;
int SPI_CS = 200000; //125kHz = teensy  //SPI clock speed; DW1000 datasheet p23;
const int ss_pin = 10;  //SPI slave select

char cmd_char[2];
String cmd_rec = "";
String cmd_buff = "";
int cmd_hex;
long SPI_return = 0;  //store the data returned from decawave
boolean new_data = false;

boolean new_cmd = false;
boolean cmd_start = false;
boolean cmd_end = false;

boolean msg_start = false;

int byte_in[4];

void setup() {   
  pinMode(ss_pin, OUTPUT);
  digitalWrite(ss_pin,LOW);  
  Serial.begin(9600);
  SPI.begin();  
}

void loop() {  
  while(Serial.available()){    
    Serial.readBytes(cmd_char,2);     //read from serial monitor or serial port
    cmd_rec = (String)cmd_char;       //convert to string
    Serial.println(cmd_rec);          //debug
          
    if(cmd_rec == "XX" && msg_start == false){  //XX==the start of a group of commands
      cmd_start = true;          
    }else if(cmd_rec == "SS" && cmd_start == false){  //SS==the start of a group of message
      msg_start = true;
    }else if(cmd_rec == "YY"){  //YY==the end of a group of commands      
      cmd_start = false;     
      deca_wave_reg_write(cmd_buff);
      cmd_buff = "";
    }else if(cmd_start == true){  //use "else if" to prevent taking "XX" as a SPI command
      cmd_buff = cmd_buff + cmd_rec;
    }  
  }
  //SPI.beginTransaction(SPISettings(SPI_CS, MSBFIRST, SPI_MODE3));
  //deca_wave_reg_write("09E608F0"); //set GPIO as output  
  //SPI.endTransaction();
  //delay(500);
  SPI.beginTransaction(SPISettings(SPI_CS, MSBFIRST, SPI_MODE3));
  deca_wave_reg_write("09E608F0"); //set GPIO as output
  deca_wave_reg_write("FF09E60CFF");  
  SPI.endTransaction();
  delay(2000);
  SPI.beginTransaction(SPISettings(SPI_CS, MSBFIRST, SPI_MODE3));
  deca_wave_reg_write("09E608F0"); //set GPIO as output
  deca_wave_reg_write("FF09E60CFF");  
  SPI.endTransaction();
  delay(2000);
}


void deca_wave_reg_write(String reg_write_cmd_str){  //take in raw spi commands and configure DecaWave
  int reg_write_cmd = 0;
  if((reg_write_cmd_str.length() % 2) == 0){  //check if a command has even size        
    int j = 0;
    for(int i = 0; i < reg_write_cmd_str.length(); i+=2){  //break a string into 2 chars
      reg_write_cmd = strtol(reg_write_cmd_str.substring(i,i+2).c_str(), NULL, 16);
      int data_in = SPI.transfer(reg_write_cmd);
      Serial.println(data_in,HEX);
      ++j;
    }
  } else {
    Serial.println("Odd command size");
    Serial.println("Command not excuted");
  }  
}


/*
#include <SPI.h>

int buff = 3;

void setup() {
  // set the slaveSelectPin as an output:
  Serial.begin(9600);
  pinMode(10,OUTPUT);
  digitalWrite(10,LOW);
  SPI.begin(); 
}

void loop() {
  SPI.beginTransaction(SPISettings(400000, MSBFIRST, SPI_MODE3));
  buff = SPI.transfer(0x09);
  SPI.endTransaction();
  Serial.println(buff,HEX);
  delay(1000);
}
*/
