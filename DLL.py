class node:
    def __init__(self,priv=None,item=None,next=None):
        self.priv=priv
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self,item=None):
        n=node(None,item,self.start)
        if not self.is_empty():
            self.start.priv=n
        self.start=n
        

    def insert_at_last(self,data):
        temp=self.start
        n=node(temp,data,None)
        if self.is_empty():
            self.start=n
        else:
            while temp.next is not None:
                temp=temp.next
            n.priv=temp
            temp.next=n

    def search_item(self,data):
        temp=self.start
        if self.is_empty():
            print("list khali hai bhai")
            return
        else:
            while(temp is not None):
                if temp.item== data:
                    return temp
                temp=temp.next

    def insert_after(self,ref,data):
        if ref is not None:
            n=node(ref,data,ref.next)
            if ref.next is not None:
                ref.next.priv=n
            ref.next=n

    def delete_first(self):
        self.start=self.start.next
        self.start.priv=None

    def delete_last(self):
        temp=self.start
        if self.is_empty():
            return 
        else:
            while temp.next is not None:
                temp=temp.next
            temp.priv.next=None
            temp.priv=None


    def delete_item(self,data):
        temp=self.start
        while(temp.item != data):
            temp=temp.next
        temp.priv.next=temp.next
        temp.next.priv=temp.priv
            
    def print_item(self):
        temp=self.start
        while(temp is not None):
            print(temp.item,end=" ")
            temp=temp.next


obj=DLL()
obj.insert_at_start(30)
obj.insert_at_start(20)
obj.insert_at_start(10)
obj.insert_at_last(50)
obj.insert_at_last(60)
obj.insert_after(obj.search_item(30),40)
obj.insert_after(obj.search_item(40),45)
obj.insert_after(obj.search_item(60),70)
obj.print_item()
obj.delete_first()
obj.delete_item(45)
obj.delete_last()
obj.print_item()