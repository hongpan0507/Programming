/*
 * utilities.cpp
 *
 *  Created on: Sep 10, 2014
 *      Author: hpan
 */

#include <sstream>	//stringstream
#include <stdlib.h>	// strtod() string to double
#include "utilities.h"

//find the temperature in the txt file; do the convert to kelvin; return the line to replace the one in the txt file
string temp_convert(string buff1, bool cel_fah) {
	double temp = 0;
	for (unsigned int i=0; i<buff1.size(); ++i) {
		if(buff1[i] == ':') {
			string buff2 = buff1.substr(i+1, buff1.size()-1);
			char* temp_ptr;
			temp = strtod(buff2.c_str(), &temp_ptr);
			if (cel_fah) temp = cel_kel(temp);	//if cel_fah = true, the unit is celsius; otherwise, it's in fahrenheit
			else temp = fah_kel(temp);
			stringstream ss;
			ss << temp;
			buff2 = ss.str();
			buff1.replace(i+1, buff1.size()-i-2, buff2);
			break;
		} //end of if
	}	//end of for
	return buff1;
}	//end of temp_convert

//convert Celsius to Kelvin
double cel_kel (double temp_cel) {
	double temp_kel = 0.0;
	temp_kel = temp_cel + 273.15;
	return temp_kel;
}	//end of temp_kel

//convert Fahrenheit to Kelvin
double fah_kel (double temp_fah) {
	double temp_kel = 0.0;
	temp_kel = (temp_fah-32.0) * 5.0/9.0 +273.15;
	return temp_kel;
}	//end of fah_kel
