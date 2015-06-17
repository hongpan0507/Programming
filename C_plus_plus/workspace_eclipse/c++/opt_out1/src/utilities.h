/*
 * utilities.h
 *
 *  Created on: Sep 10, 2014
 *      Author: hpan
 */


#ifndef UTILITIES_H_
#define UTILITIES_H_

#include <string>
using namespace std;

//find the temperature in the txt file; do the convert to kelvin; return the line to replace the one in the txt file
string temp_convert(string buff1, bool cel_fah);

//convert Celsius to Kelvin
double cel_kel (double temp);

//convert Fahrenheit to Kelvin
double fah_kel (double temp);

#endif /* UTILITIES_H_ */
