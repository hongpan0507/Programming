//============================================================================
// Name        : csv_psi.cpp
// Author      : hpan
// Version     :
// Copyright   : no right
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>	//ifstream, ofstream
#include <sstream>	//stringstream
#include <string>	//to_string
#include <stdlib.h>	//strtod
#include <math.h>	//log10

using namespace std;

int main() {
	int state = 16;
	int data_row = 2001;
	int data_type = 4;
	int data_row_start = 8;	//data starts from row 8

	string row;
	string data_string;	//frequency; phase; s11; s21
	double data_num[state][data_row][data_type];	//frequency; phase; s11; s21

	ifstream csv_file;
	string file_read_name;


	ofstream phase_psi_file;
	ofstream s11_psi_file;
	ofstream s21_psi_file;

	//string phase_file_name = "/home/hpan/Desktop/Orange/phase.csv";
	//string s11_file_name = "/home/hpan/Desktop/Orange/s11.csv";
	//string s21_file_name = "/home/hpan/Desktop/Orange/s21.csv";

	string phase_file_name = "/home/hpan/Dropbox/Raven_Standard_LLC/digital_phase_shifter/data/CSV/Gen1/black/phase.csv";
	string s11_file_name = "/home/hpan/Dropbox/Raven_Standard_LLC/digital_phase_shifter/data/CSV/Gen1/black/s11.csv";
	string s21_file_name = "/home/hpan/Dropbox/Raven_Standard_LLC/digital_phase_shifter/data/CSV/Gen1/black/s21.csv";

	phase_psi_file.open(phase_file_name.c_str());
	s11_psi_file.open(s11_file_name.c_str());
	s21_psi_file.open(s21_file_name.c_str());

	for(int file_count = 0; file_count < state; ++ file_count){
		file_read_name = "/home/hpan/Dropbox/Raven_Standard_LLC/digital_phase_shifter/data/CSV/Gen1/black/black_" + to_string(file_count) + ".csv";
		//file_read_name = "/home/hpan/Desktop/Orange/" + to_string(file_count) + ".csv";
		csv_file.open(file_read_name.c_str());

		if(csv_file.is_open()){
			for(int row_dump = 0; row_dump < data_row_start; ++ row_dump){ //data starts from line 8
				getline(csv_file,row);
			}

			for(int line_count = 0; line_count < data_row; ++line_count){
				getline(csv_file,row);
				stringstream ss(row);
				string new_row = "";
				char* ptr;
				for(int i = 0; i < data_type; ++i){
					getline(ss,data_string, ',');
					//phase_psi_file<<data[file_count][line_count][i];
					if(i == 0){
						data_num[file_count][line_count][i] = (double)strtod(data_string.c_str(), &ptr) / 1000000000;	// convert the first number (frequency) to GHz
					} else {
						data_num[file_count][line_count][i] = (double)strtod(data_string.c_str(), &ptr);
					}
				}
			}
		} else {
			cout << "cannot read from files";
		}
		csv_file.close();
	}


	if(phase_psi_file.is_open() && s11_psi_file.is_open() && s21_psi_file.is_open()){
		string column_name = "Frequency (GHz),";
		for(int i = 0; i < state; ++i){
			if(i < state -1){
				column_name += "state_" + to_string(i) + ',';
			} else {
				column_name += "state_" + to_string(i ) + '\n';
			}
		}
		phase_psi_file << column_name;
		s11_psi_file << column_name;
		s21_psi_file << column_name;
		for(int i = 1; i < data_type; ++i){
			for(int j = 0; j < data_row; ++j){
				string line = "";
				for(int k = 0; k < state; ++k){
					/*
					if(i == 1){	//convert s21 to log scale
						data_num[k][j][i] = 10*log10(data_num[k][j][i]);
					}*/
					if(k < state-1){
						line += to_string(data_num[k][j][i]) + ",";
					} else {
						line += to_string(data_num[k][j][i]);
					}
				}
				if(i == 2){		//s21 phase
					line = to_string(data_num[0][j][0]) + "," + line + '\n';
					phase_psi_file << line;
					cout << line << endl;
				} else if (i == 3){	//s11 log mag
					line = to_string(data_num[0][j][0]) + "," + line + '\n';
					s11_psi_file << line;
					cout << line << endl;
				} else if (i == 1){	//s21 log mag
					line = to_string(data_num[0][j][0]) + "," + line + '\n';
					s21_psi_file << line;
					cout << line << endl;
				}

			}
		}
	} else {
		cout << "cannot write to files";
	}
	phase_psi_file.close();
	s11_psi_file.close();
	s21_psi_file.close();

	return 0;
}
