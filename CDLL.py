#circulor doubleyn linked list
class node:
    def __init__(self,priv=None,item=None,next=None):
        self.priv=priv
        self.item=item
        self.next=next

class CDLL:
    def __init__(self):
        self.last=None

    def is_empty(self):
        return self.last is None
    
    def insert_at_start(self,data):
        n=node(None,data)
        if self.is_empty():
            n.priv=n
            n.next=n
            self.last=n
        else:
            self.last.next.priv=n
            n.next=self.last.next
            n.priv=self.last
            self.last.next=n

    def insert_at_last(self,data):
        n=node(None,data)
        if self.is_empty():
            n.next=n.priv=n
        else:
            self.last.next.priv=n
            n.next=self.last.next
            n.priv=self.last
            self.last.next=n
        self.last=n
    
    def search_item(self,data):
        temp=self.last
        while(temp.next is not self.last):
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp

    def insert_after(self,ref,data):
        n=node(ref,data,ref.next)
        if ref ==self.last:
            self.last=n
        ref.next.priv=n
        ref.next=n
    def delete_first(self):
        if self.last.next==self.last:
            return None
        else:
            self.last.next.next.priv=self.last
            self.last.next=self.last.next.next
    def delete_last(self):
        if self.last.next==self.last:
            return None
        else:
            self.last.next.priv=self.last.priv
            self.last.priv.next=self.last.next
            self.last=self.last.priv
    def delete_item(self,data):
        temp=self.last
        if temp.item==data:
            self.delete_last()
        else:
            while(temp.next is not self.last):
                if temp.next.item==data:
                    temp.next.next.priv=temp
                    temp.next=temp.next.next
                    break
                temp=temp.next
              
    def print_item(self):
        temp=self.last.next
        while(temp != self.last):
            print(temp.item,end=" ")
            temp=temp.next
        print(temp.item,end=" ")


obj=CDLL()

obj.insert_at_last(40)
obj.insert_at_start(30)
obj.insert_at_start(20)
obj.insert_at_start(10) 
obj.insert_at_last(50)
obj.insert_at_last(60)
obj.insert_after(obj.search_item(30),35)
obj.insert_after(obj.search_item(60),70)
obj.delete_first()
obj.delete_last()
obj.delete_item(60)
obj.delete_item(35)
obj.print_item()