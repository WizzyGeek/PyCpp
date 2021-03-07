#include <iostream>
#include <fstream>

using namespace std;

int main() {

    ofstream File("Output.txt");

    File << "This is some very, very nice output.\nIt's poggers!";

    File.close();

    string Text;

    ifstream ReadFile("Output.txt");

    while (getline(ReadFile, Text)) {
        cout << Text << endl;
    }

    return 0;
}