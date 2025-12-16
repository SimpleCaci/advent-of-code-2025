//Part 1 Solution for Advent of Code 2025 Day 3
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream inputFile("input.txt");
    if (!inputFile) {
        cerr << "Error opening file!" << endl;
        return 1;
    }

    int sum = 0;
    while (!inputFile.eof()) {
        string line;
        getline(inputFile, line);

        cout << "First Digit Loop" << endl;
        int maxDigit = line.at(0) - '0';
        int maxIndex = 0;
        //-2 to prevent the last character which is a newline from being included
        for (unsigned int i = 0; i < line.length()-2; ++i) {
            int currDigit = line.at(i) - '0';
            cout << "1.    Current Digit: " << currDigit << endl;
            if (currDigit > maxDigit) {
                cout << "1.        New Max Digit Found: " << currDigit << endl;
                maxDigit = currDigit;
                maxIndex = i;
            }
        }

        cout << endl;
        cout << "Second Digit Loop" << endl;
        int secondMaxDigit = line.at(maxIndex+1) - '0';
        cout << "2.    Initial Second Max Digit: " << secondMaxDigit << endl;
        //-1 to prevent the last character which is a newline from being included
        for (unsigned int i = maxIndex+1; i < line.length()-1; ++i) {
            int currDigit = line.at(i) - '0';
            cout << "2.    Current Digit: " << currDigit << endl;
            if (currDigit > secondMaxDigit) {
                cout << "2.    New Max Digit Found: " << currDigit << endl;
                secondMaxDigit = currDigit;
            }
        }
        cout << endl << endl;
        sum += (maxDigit*10 + secondMaxDigit);

        // the << "\033[31m" sets to red
        // the << "\033[0m" resets to default

        cout << "\033[31m" << "Max Digit: " << maxDigit << ", Second Max Digit: " << secondMaxDigit << "\033[0m"<< endl << endl;

    }
    cout << "The Sum of the largest voltages is " << sum << endl;
    inputFile.close();
    return 0;
}