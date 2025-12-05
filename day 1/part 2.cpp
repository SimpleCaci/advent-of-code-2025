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
    char dir;
    int isAtZero = 0;
    int rotationAmt = 0;

    while(inputFile >> dir >> rotationAmt) {
        //cout << "Current Position Is " << pos << endl;
        for (int i = 0; i < rotationAmt; ++i){
            if (dir == 'L'){
                pos--;
            } else if (dir == 'R'){
                pos++;
            }
            
            if (pos == -1){
                pos = 99;
            } // left bound
            
            if (pos == 100){
                pos = 0;
            } // right bound
            
            if (pos == 0){
                isAtZero++;
            }
        }
    }

    cout << "The Amount of Zeros (aka the password) is " << isAtZero << endl;
    inputFile.close();
    return 0;
}