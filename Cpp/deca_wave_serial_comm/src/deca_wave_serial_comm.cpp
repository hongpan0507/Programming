//============================================================================
// Name        : deca_wave_serial_comm.cpp
// Author      : hpan
// Version     :
// Copyright   : no right
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
#include "serial_comm/TimeoutSerial.h"

using namespace std;

#define manual_input 1
#define file_input 2

int main() {
	cout << "Enter serial port number: (ex. /dev/ttyACM0)" << endl;
	cout << "cmd << ";
	string serial_port_loc = "/dev/ttyACM0";
	//cin >> serial_port_loc;
	TimeoutSerial teensy_serial(serial_port_loc, 9600); //*initialize serial port
	cout << "connecting to teensy..." << endl;



	fstream cmd_input;
	string cmd_read;
	string cmd_tx = "";
	string cmd_rx = "";
	cout << "Enter command txt file location: " << endl;
	cout << "(ex. /home/hpan/workspace_github/Programming/Cpp/deca_wave_serial_comm/deca_wave_cmd.txt)" << endl;
	cout << "cmd << ";
	string file_loc = "/home/hpan/workspace_github/Programming/Cpp/deca_wave_serial_comm/deca_wave_cmd.txt";
	//cin >> file_loc;

	int switch_case = 0;
	while(true){
		cout << "1. manual cmd input (Enter 'EXIT' to return to main menu)" << endl;
		cout << "2. select a text file with cmds" << endl;
		cout << "cmd >> ";
		cin >> switch_case;

		switch(switch_case){
			case manual_input:
				while(cmd_tx != "EXIT"){
					cout << "cmd >> ";
					cin >> cmd_tx;
					teensy_serial.write(cmd_tx.c_str(),cmd_tx.size());
					cmd_rx = teensy_serial.readStringUntil(";");
					cout << "Received from Teensy: " << cmd_rx << endl;
					if(cmd_rx != "$$"){
						cmd_rx = teensy_serial.readStringUntil(";");
						int temp = strtol(&cmd_rx[0], NULL, 10);
						cout << "Received from Deca_wave: " << hex << temp << endl;
					}
				}
				break;
			case file_input:
				try {
					cmd_input.open(file_loc.c_str(), fstream::in);	//read cmds from a file
					while(!cmd_input.eof()){
						string buff = "";
						getline(cmd_input,buff);	//store each cmd to a string
						cmd_read = buff.substr(0,2);	//only take in first 2 characters as a cmd
						cmd_tx += cmd_read;
					}

					teensy_serial.write(cmd_tx.c_str(),cmd_tx.size());
					cmd_rx = teensy_serial.readString(cmd_tx.size());
					if(cmd_rx != "no_new_data"){
						cout << "Received from Teensy: " << cmd_rx << endl;
					}
					cmd_input.close();
				} catch(fstream::failure &e){
					cerr << "Exception: " << e.what();
				}
				break;
		}
		cmd_tx = "";
	}

	return 0;
}
