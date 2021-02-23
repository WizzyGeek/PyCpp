
class Vector():

    def __init__(self, data: list) -> None:
        self.data = data
        return

    def push_back(self, val) -> None:
        "Adds an element to the end of the vector"
        self.data.append(val)

    def pop_back(self) -> None:
        "Removes the last element of the vector"
        self.data.pop(-1)

    def at(self, index: int):
        "Gets the element at specified index"
        return self.data[index]

    def size(self) -> int:
        "Returns the size of the vector"
        return len(self.data)

    def empty(self) -> bool:
        "Test whether vector is empty"
        return len(self.data) == 0

    def front(self):
        "Returns the first element of a vector"
        return self.data[0]

    def back(self):
        "Returns the last element of a vector"
        return self.data[-1]

    def data_(self):
        "Returns the data the vector holds"
        return self.data
    
    def insert(self, position: int, val) -> None:
        self.data.insert(position, val)
        return

    def clear(self) -> None:
        self.data = []
        return
