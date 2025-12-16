// Part 2 Solution for Advent of Code 2025 Day 3
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

    long long sum = 0; // final total joltage (VERY LARGE)

    while (true) {

        string line;
        getline(inputFile, line);

        if (!inputFile.good()) break;

        // FIX: remove trailing '\r' for Windows CRLF inputs
        if (!line.empty() && line.back() == '\r')
            line.pop_back();

        if (line.empty()) continue;

        int n = 12;   // number of digits we must pick

        long long bankValue = 0; // <-- this is the actual 12-digit number
        int maxDigit = -1;
        int maxIndex = -1;

        int loopDigit = 1;
        cout << loopDigit << " Digit Loop" << endl;

        // FIRST LOOP — pick largest digit in the valid window
        unsigned int searchEnd = (line.length() - 1) - (n - loopDigit);

        for (unsigned int i = 0; i <= searchEnd; ++i) {
            int currDigit = line.at(i) - '0';
            cout << "1.    Current Digit: " << currDigit << endl;

            if (currDigit > maxDigit) {
                cout << "1.        New Max Digit Found: " << currDigit << endl;
                maxDigit = currDigit;
                maxIndex = i;
            }
        }

        cout << "Loop 1 exited with maxIndex: " << maxIndex << endl << endl;

        // BUILD THE 12-DIGIT NUMBER CORRECTLY:
        bankValue = bankValue * 10 + maxDigit;
        cout << "BANK VALUE NOW: " << bankValue << endl;


        // REMAINING 11 LOOPS
        loopDigit++;

        while (loopDigit <= n) {
            cout << endl << endl;
            cout << "\033[34m" << loopDigit << " Digit Loop" << "\033[0m" << endl;

            int secondMaxDigit = -1;
            int secondIndex = -1;

            unsigned int searchStart = maxIndex + 1;
            unsigned int searchEnd = (line.length() - 1) - (n - loopDigit);

            for (unsigned int i = searchStart; i <= searchEnd; ++i) {

                int currDigit = line.at(i) - '0';
                cout << loopDigit << ".    Current Digit: " << currDigit << endl;

                if (currDigit > secondMaxDigit) {
                    cout << loopDigit << ".    New Max Digit Found: " << currDigit << endl;
                    secondMaxDigit = currDigit;
                    secondIndex = i;
                }
            }

            maxIndex = secondIndex;

            cout << "Loop " << loopDigit
                 << " exited with secondMaxDigit: " << secondMaxDigit << endl;
            cout << endl << endl;

            // APPEND DIGIT INTO THE 12-DIGIT NUMBER
            bankValue = bankValue * 10 + secondMaxDigit;

            cout << "\033[36m" << "BankValue Updated:" << endl;
            cout << "bankValue = (previous * 10) + " << secondMaxDigit << endl;
            cout << "bankValue now: " << bankValue << "\033[0m" << endl;

            loopDigit++;
        }

        cout << "\033[31mFinished Line. 12-Digit Bank Value: " 
             << bankValue << "\033[0m" << endl;

        sum += bankValue;
        cout << "Running Total Sum: " << sum << endl << endl;
    }

    cout << "====================================================" << endl;
    cout << "The Sum of the largest voltages is " << sum << endl;
    cout << "====================================================" << endl;

    inputFile.close();
    return 0;
}
