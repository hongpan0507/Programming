
/*============================================================================
// Name        : opt_out1.cpp
// Author      : Hong Pan
// Version     :
// Copyright   : NONE
// Description : ecen489_fall_2014 opt_out1 assignment
//notes:
    in = read from file
    out = write to file
	ofstream: Stream class to write on files
	ifstream: Stream class to read from files
	fstream: Stream class to both read and write from/to files.
			(didn't work for writing to the file)
	strtod(): http://www.cplusplus.com/reference/cstdlib/strtod/
============================================================================*/

#include <iostream>
#include <fstream>	//fstream
#include <vector>	//vector
#include <stdlib.h>	// strtod() string to double
#include <string>	//to_string()
#include <sstream>	//stringstream
#include <windows.h>
#include "utilities.h"	//user defined library

using namespace std;

int main() {
	fstream temp_txt_file;
	temp_txt_file.open("temp_file.txt", fstream::in);
	if (temp_txt_file.is_open()) {
		cout << "test";
		vector<string> msg_vector;
		string msg_string = " ";
		//store the content of the txt file to a vector and process
		while(!temp_txt_file.eof()) {
			getline(temp_txt_file, msg_string);
			if (msg_string == "\t\t\"tempunit\":\"Celsius\"") {
				msg_string = "\t\t\"tempunit\":\"Kelvin\"";
				msg_vector[msg_vector.size()-1] = temp_convert(msg_vector[msg_vector.size()-1], true);	//if the unit is in celsius, pass "true"
				cout << "Celsuis to Kelvin. ";
			} else if (msg_string == "\t\t\"tempunit\":\"Fahrenheit\"") {
				msg_string = "\t\t\"tempunit\":\"Kelvin\"";
				msg_vector[msg_vector.size()-1] = temp_convert(msg_vector[msg_vector.size()-1], false);	//if the unit is in fahrenheit, pass "false"
				cout << "Fahrenheit to Kelvin. ";
			}	//end of else if
			msg_vector.push_back(msg_string);
		}	//end of while
		temp_txt_file.close();

		temp_txt_file.open("temp_file.txt", fstream::out);
		//replace the content of txt file
		for(unsigned int i=0; i < msg_vector.size(); ++i) {
			if (i < msg_vector.size()-1) {
				temp_txt_file << msg_vector[i] << endl;
			} else {
				temp_txt_file << msg_vector[i];
			}
		}	//end of for
		cout << "success!" << endl;
		temp_txt_file.close();
	} else {
		cout << "Unable to open file";
	}

	return 0;
}
