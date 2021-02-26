#include <iostream>
#include <sstream>

using namespace std;

int main() {

    string endS;

    cout << "Enter end of fizzbuzz: ";
    cin >> endS;

    int end;

    stringstream convert(endS);

    convert >> end;

    for(int i=1; i<=end; i++) {
        if (i%3==0 && i%5 == 0) {
            cout << "Fizzbuzz" << endl;
        } else if (i%3==0) {
            cout << "Fizz" << endl;
        } else if (i%5==0) {
            cout << "Buzz" << endl;
        } else cout << i << endl;
    }

    return 0;
}