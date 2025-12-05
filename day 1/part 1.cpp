//Part 1 Solution for Advent of Code 2025 Day 1
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream inputFile("input.txt");
    if (!inputFile) {
        cerr << "Error opening file!" << endl;
        return 1;
    }

    int pos = 50;
    char leftOrRight;
    int isAtZero = 0;
    int rotationAmt = 0;

    while(inputFile >> leftOrRight) {
        cout << "Current Position Is " << pos << endl;
        inputFile >> rotationAmt;
        if (leftOrRight == 'L') {
            cout << "Rotated Left By " << rotationAmt << endl;
            pos -= rotationAmt;
            while (pos < 0){
                pos += 100;
            }
        } else if (leftOrRight == 'R') {
            cout << "Rotated Right By " << rotationAmt << endl;
            pos += rotationAmt;
            while (pos > 99){
                pos -= 100; //wrap 100 not 99 since there are 100 positiuons
            }
        }
        if (pos == 0) {
            isAtZero++;
        }
    }

    cout << "The Amount of Zeros (aka the password) is " << isAtZero << endl;
    inputFile.close();
    return 0;
}