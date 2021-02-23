
class vector():

    def __init__(self, data: list) -> None:
        self.data_ = data
        return

    def __getitem__(self, key: int):
        return self.data_[key]

    def __setitem__(self, key: int, value) -> None:
        self.data_[key] = value
        return

    def push_back(self, val) -> None:
        "Adds an element to the end of the vector"
        self.data_.append(val)

    def pop_back(self) -> None:
        "Removes the last element of the vector"
        self.data_.pop(-1)

    def at(self, index: int):
        "Gets the element at specified index"
        return self.data_[index]

    def size(self) -> int:
        "Returns the size of the vector"
        return len(self.data_)

    def empty(self) -> bool:
        "Test whether vector is empty"
        return len(self.data_) == 0

    def front(self):
        "Returns the first element of a vector"
        return self.data_[0]

    def back(self):
        "Returns the last element of a vector"
        return self.data_[-1]

    def data(self):
        "Returns the data the vector holds"
        return self.data_
    
    def insert(self, position: int, val) -> None:
        "Insert a value at the specified index"
        self.data_.insert(position, val)
        return

    def clear(self) -> None:
        "Clear all data from the vector"
        self.data_ = []
        return

    def erase(self, position: int, end_position: int = None) -> None:
        "Clear all data from the vector at the specified index or throughout the range"
        end_position = (end_position if not end_position == None else position) + 1
        for i in range(position, end_position):
            self.data_.pop(i)
        return
