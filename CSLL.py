# corculor singly linked list
class node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class CSLL:
    def __init__(self,last=None):
        self.last = last

    def is_empty(self):
        return self.last is None

    def insert_at_start(self, data):
        n = node(data)
        if not self.is_empty():
            temp = self.last
            n.next = temp.next
            temp.next = n
        else:
            self.last = n
            n.next=n

    def insert_at_last(self, data):
        n = node(data)
        if not self.is_empty():
            n.next = self.last.next
            self.last.next = n
        self.last = n

    def insert_after(self, ref, data):
        n=node(data)
        if ref is not None:
            n.next=ref.next
            ref.next=n
        if ref==self.last:
            self.last=n


    def search_item(self, data):
        temp=self.last.next
        while temp != self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        return None

    def delete_first(self):
        self.last.next=self.last.next.next

    def delete_last(self):
        temp=self.last.next
        while(temp.next != self.last):
            temp=temp.next
        temp.next=self.last.next
        self.last=temp


    def delete_item(self, data):
        temp=self.last
        if self.last.item==data:
            self.delete_last()
            return
        while temp.next != self.last:
            if temp.next.item==data:
                temp.next=temp.next.next
            temp=temp.next

    def print_item(self):
        temp = self.last.next
        while temp != self.last:
            print(temp.item,end=" ")
            temp = temp.next
        print(temp.item)

obj = CSLL()
obj.insert_at_start(30)
obj.insert_at_start(20)
obj.insert_at_start(10)
obj.insert_at_last(70)
obj.insert_at_last(80)
obj.insert_after(obj.search_item(30),40)
obj.insert_after(obj.search_item(40),50)
obj.insert_after(obj.search_item(50),60)
obj.print_item()
obj.delete_first()
obj.delete_last()
obj.delete_item(50)
obj.print_item()