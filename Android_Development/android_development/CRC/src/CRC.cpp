/*============================================================================
// Name        : CRC.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
Notes:
ctrl + / = comment
operators: http://www.cplusplus.com/doc/tutorial/operators/
============================================================================*/

#include <iostream>
using namespace std;

int CRC_cal (int data, int data_size, int current_CRC, int CRC_size, int poly);

int main() {
	int seed = 0;
	int poly = 0x0700;
	int data = 0xaa;
	int data_size = 8;	//size of data in bits
	int CRC = 0;
	int CRC_size = 16;	//size of CRC in bits
	int CRC_display = 0;

	CRC = seed;
	cout << "Seed (in hex) = " << hex << seed << endl;
	cout << "Poly (in hex) = " << hex << poly << endl;

	while (true) {
		cout << "data (in hex) = ";
		cin >> hex >> data;
		if	(data==0xffff) {
			CRC = seed;
			cout << '\n' <<"Seed (in hex) = " << hex << seed << endl;
			cout << "Poly (in hex) = " << hex << poly << endl;
		} else {
			CRC = CRC_cal(data, data_size, CRC, CRC_size, poly);
			CRC_display = CRC >> 8;	// the last 8 bits are always 0
			cout <<"CRC = " << hex << CRC_display << endl;
		}	//end of if
	}	//end of while

	return 0;
}	//end of main

int CRC_cal (int data, int data_size, int current_CRC, int CRC_size, int poly) {
	int temp_data = 0;
	int temp_CRC = 0;
	int MSB_CRC = 0;	//most significant bit of CRC

	for (int i = data_size - 1; i >= 0; i --) { //perform calculation 8 times (from MSB to LSB)
		temp_data = data >> i;
		temp_data = temp_data & 1;	//"bit-wise and" to get individual bit of the data
		MSB_CRC = current_CRC >> (CRC_size - 1);
		MSB_CRC = MSB_CRC & 1;	//"bit-wise and" to get MSB of each CRC
		temp_CRC = current_CRC << 1; //add zero to the end to "XOR" ploy or 0
		if (temp_data ^ MSB_CRC) {	// if data bit "XOR" MSB_CRC bit = 1; use poly
			temp_CRC = temp_CRC ^ poly;
		} else if (!(temp_data^MSB_CRC)){	// if data bit "XOR" MSB_CRC bit = 0; use zero
			temp_CRC = temp_CRC ^ (0x0000);
		}
		current_CRC = temp_CRC & (0xffff); //only keep the least significant 16 bit as CRC
	}	//end of for

	return current_CRC;
}	//end of CRC_cal


