from PyCpp import *

_file = ofstream("Output.txt")

_file << "This is some very, very nice output.\nIt's poggers!"

fileContent = ifstream("Output.txt")

for line in getline(fileContent):
    cout << line