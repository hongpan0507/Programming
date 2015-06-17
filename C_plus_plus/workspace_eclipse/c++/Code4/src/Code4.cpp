//============================================================================
// Name        : Code4.cpp
// Author      : hong
// Version     :
// Copyright   : no warranty; no guarantee
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	vector<double> PI;
	double arithmeticMean = 0.0;
	double arithmeticMeanTemp = 0.0;
	double median = 0.0;
	double mode = 0.0;
	double variance = 0.0;
	double varianceTemp = 0.0;
	int PIArray[] = { 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3,
					  8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8,
					  4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1};

	int size = (sizeof(PIArray)/sizeof(*PIArray));
	for(int i = 0; i < size; ++i){
		PI.push_back(PIArray[i]);
	}

	//mean
	for(double &PIPI : PI){
		arithmeticMeanTemp += PIPI;
	}
	arithmeticMean = arithmeticMeanTemp / PI.size();

	//median
	sort(PI.begin(), PI.end());
	int evenOrOdd = (PI.size())%2;
	if(evenOrOdd == 0){
		int temp = (PI.size())/2;
		median = (PI[temp] + PI[temp-1])/2;
	} else {
		int temp = PI.size()/2;
		median = PI[temp];
	}

	//mode
	int count = 0;
	int occurance = 0;
	int record = PI[0];
	for(unsigned int i = 0; i < PI.size(); ++i){
		if(record == PI[i]){
			++count;
			if(i == (PI.size()-1) && occurance < count){
				occurance = count;
				mode = PI[i - 1];
			}
		} else {
			if (occurance < count && i > 0) {
				occurance = count;
				mode = PI[i - 1];
			} //end of if
			count = 1;
		} //end of else
		record = PI[i];
	} //end of for

	//variance
	for(double &PIPI : PI){
		varianceTemp = PIPI - arithmeticMean;
		varianceTemp = varianceTemp * varianceTemp;
		variance += varianceTemp;
	}
	variance = variance / (PI.size()-1);

	//output
	cout << "arithmetic mean: " << arithmeticMean << endl;
	cout << "median: " << median << endl;
	cout << "mode: " << mode << endl;
	cout << "variance: " << variance << endl;
}
