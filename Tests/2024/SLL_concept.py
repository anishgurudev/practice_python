"""Singly Link List"""


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    # if the start is none/empty then it will return True else False
    def isEmpty(self):
        return self.start == None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.isEmpty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

    def __iter__(self):
        return SSL_Itrator(self.start)


class SSL_Itrator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# Driver_code
myList = SLL()
myList.insert_at_start(30)
myList.insert_at_start(10)
myList.insert_at_last(50)
myList.insert_after(myList.search(50), 45)
myList.print_list()
print()
myList.delete_item(10)
myList.print_list()

for X in myList:
    print(X, end=" ")
