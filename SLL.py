# singli linked list

class node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, item):
        n = node(item, self.start)
        self.start = n

    def insert_at_last(self, item):
        n = node(item)
        temp = self.start
        while (temp.next != None):
            temp = temp.next
        temp.next = n

    def search(self, data):
        if self.is_empty():
            return None
        temp = self.start
        while (temp is not None):
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, ref, data):
        n = node(data)
        if self.is_empty():
            print("list to empty hai")
        else:
            temp = self.start
            while (temp != None):
                if temp == ref:
                    n.next = temp.next
                    temp.next = n
                    break
                temp = temp.next
            if temp == None:
                raise ValueError("given reference not present")

    def delete_first(self):
        if self.is_empty():
            print("list to khali hai")
        else:
            self.start = self.start.next
            print("ho gaya delete")

    def delet_last(self):
        temp = self.start
        if self.is_empty():
            print("list empty hai bhai")
        else:
            if temp.next == None:
                self.start = None
            else:
                while (temp.next.next != None):
                    temp = temp.next
                temp.next = None

    def delete_item(self, data):
        temp = self.start
        if self.is_empty():
            print("already empty")
        else:
            if temp.item == data:
                self.start = None
            else:
                while (temp.next.next != None):
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        print("delete ho gaya")
                    temp = temp.next

    def print_items(self):
        temp = self.start
        if self.is_empty():
            print("koi items nahi hai bhai")
        else:
            while (temp != None):
                print(temp.item,end=" ")
                temp=temp.next
            print()


obj = SLL()
obj.insert_at_start(50)
obj.insert_at_start(40)
obj.insert_at_start(30)
obj.insert_at_start(20)
obj.insert_at_last(70)
obj.insert_at_last(80)
obj.insert_after(obj.search(50), 60)
obj.print_items()
obj.delet_last()
obj.delete_first()
obj.delete_item(50)
obj.print_items()