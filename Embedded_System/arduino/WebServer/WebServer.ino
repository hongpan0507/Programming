/*
  Web Server
 
 A simple web server that shows the value of the analog input pins.
 using an Arduino Wiznet Ethernet shield. 
 
 Circuit:
 * Ethernet shield attached to pins 10, 11, 12, 13
 * Analog inputs attached to pins A0 through A5 (optional)
 
 created 18 Dec 2009
 by David A. Mellis
 modified 9 Apr 2012
 by Tom Igoe
 
 */

#include <SPI.h>
#include <Ethernet.h>

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = { 0x90, 0xA2, 0xDA, 0x00, 0x47, 0x6D };
IPAddress ip(192,168,1, 177);
int serverPort = 2013;
int pin = 8;
// Initialize the Ethernet server library
// with the IP address and port you want to use 
// (port 80 is default for HTTP):
EthernetServer server(serverPort);

void setup() {
 // Open serial communications and wait for port to open:
  Serial.begin(9600);
  Ethernet.begin(mac, ip);
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());
  
  pinMode(pin, OUTPUT);
  }

void loop() {
  // listen for incoming clients
  EthernetClient client = server.available();
  if (client) {
    String clientMsg = null;
  
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        clientMsg += c;        
        if (c == '\n') {
          // you're starting a new line
          if(clientMsg == "yes" || clientMsg == "Yes" || clientMsg == "YES"){
            digitalWrite(pin, HIGH);
          } else if (clientMsg == "no" || clientMsg == "no" || clientMsg == "NO"){
             digitalWrite(pin, LOW);
          }//end of else if
        }// end of if 
      }// end of if
    }//end of while
    // give the web browser time to receive the data
    delay(1);
    // close the connection:
    client.stop();
    Serial.println("client disonnected");
  }
}

