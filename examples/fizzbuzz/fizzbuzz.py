from PyCpp import *

def main() -> int:

    end = cin >> "Enter end of fizzbuzz: "

    try:
        end = stringstream(end) >> 1 # convert 'end' to int
    except Exception as e:
        raise e

    for i in range(1, end+1):
        if i%3 == 0 and i%5 == 0:
            cout << "Fizzbuzz" << endl
        elif i%3 == 0:
            cout << "Fizz" << endl
        elif i%5 == 0:
            cout << "Buzz" << endl
        else:
            cout << i << endl

    return 0;

main()