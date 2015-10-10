#ifndef interface_h
#define interface_h
#include "Arduino.h"

class interface
{
  public:
    interface(int pin);
    void serialConnect();
	void ethernetConnect(int port);
	
  private:
    int ledpin;
	int _port;
	
};

#endif
