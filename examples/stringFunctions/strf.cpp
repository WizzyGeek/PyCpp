#include <iostream>

using namespace std;

int main() {

    string str;

    cout << "Enter string: ";
    cin >> str;

    cout << "'" << str << "' has " << str.length() << " characters!" << endl;

    return 0;
}