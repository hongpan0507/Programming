int baud_rate = 9600;
int count_byte = 0;
int xbee_in = 0;
int start_delimiter = 0x7E;
int frame_len = 0;  //size of frame data in bytes excluding checksum, length, start delimiter
int frame_len_MSB = 0;
int frame_len_LSB = 0;
int API_id = 0;
int source_addr = 0;
int source_addr_MSB = 0;
int source_addr_LSB = 0;
int RSSI_val = 0;
int option = 0;
int data_byte = 0;
int check_sum = 0;
boolean FS = false;

void setup() {
  // put your setup code here, to run once:
  Serial1.begin(baud_rate);
  Serial.begin(baud_rate);
}

void loop() {
  // put your main code here, to run repeatedly: 
  if(Serial1.available()){
    xbee_in = Serial1.read();
    if(FS == true){
      ++count_byte;
      if(count_byte == 2){  //2nd byte = MSB of length
        frame_len_MSB = xbee_in; 
        //frame_len_MSB = frame_len_MSB << 8;  //1 byte = 8 bits
        Serial.print("frame Length MSB = ");
        Serial.println(frame_len_MSB, DEC);        
        FS = false;
        count_byte = 0;
      }
      /*
      if(count_byte == 3){  //3rd byte = LSB of length
        frame_len_LSB = xbee_in; 
        frame_len = frame_len_MSB | frame_len_LSB;  //bitwise or to get the length of frame data
        Serial.print("frame Length = ");
        Serial.println(frame_len, DEC);
        FS = false;
        count_byte = 0;
      } 
      */    
    } else if(xbee_in == start_delimiter){  //1st byte = start delimiter
      FS = true;      
      Serial.print("Start Delimiter = ");
      Serial.println(xbee_in, HEX);
    }
  }
}
