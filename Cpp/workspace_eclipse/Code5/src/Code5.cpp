//============================================================================
// Name        : Code5.cpp
// Author      : hong
// Version     :
// Copyright   : no warranty; no guarantee
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	int firstNum = 0;
	int secondNum = 0;

	while (true) {
		try {
			cout << "Enter two numbers: ";
			cin >> firstNum >> secondNum;
			if (secondNum == 0) {
				throw 0;
			} else {
			cout << firstNum << " / " << secondNum << " = " << firstNum/secondNum << endl;
			}
		} catch (int error) {
			cout << "Cannot be divided by zero; Retry..." << endl;
		} // end of catch
	} // end of while
}
