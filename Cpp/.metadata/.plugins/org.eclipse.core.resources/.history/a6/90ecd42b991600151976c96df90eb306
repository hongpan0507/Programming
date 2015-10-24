//============================================================================
// Name        : deca_wave_serial_comm.cpp
// Author      : hpan
// Version     :
// Copyright   : no right
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "serial_comm/TimeoutSerial.h"

using namespace std;

int main() {
	char rx[4];
	string rx_str;
	cout << "connecting to teensy..." << endl;
	TimeoutSerial teensy_serial("/dev/ttyACM0", 9600); //*initialize serial port

	int count = 0;
	while(true){
		++count;
		teensy_serial.read(rx, sizeof(rx));
		//rx_str = teensy_serial.readString(2);

		cout << rx << count <<endl;
	}

	return 0;
}
