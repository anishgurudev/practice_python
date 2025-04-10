"""Doubly Link List"""


class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class DLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start == None

    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.isEmpty():
            self.start.prev = n
        self.start = n


    def insert_at_last(self, data):
        n = Node(self.prev, data, self.next)
        if not self.isEmpty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            self.prev = temp.next.next
        else:
            self.start = n

    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp == data:
                return temp
            temp=temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node()


#
#     def delete_first(self):
#
#     def delete_last(self):
#
#     def delete_item(self):
#
#     def print_list(self):
#
#     def __iter__(self):
#         return SSl_Itrator(self.start)
#
#
# class SSl_Itrator:
#     def __init__(self,start):
#         self.current = start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if not self.current:
#             raise StopIteration
#         data = self.current.item
#         self.current =self.current.next
#         return data
#
#

# Driver_code
myList = DLL()
myList.insert_at_start(30)
myList.insert_at_start(10)
myList.insert_at_last(50)
myList.insert_after(myList.search(50), 45)
myList.print_list()
print()
myList.delete_item(10)

for X in myList:
    print(X, end=" ")
