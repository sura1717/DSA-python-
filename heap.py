class EmptyHeapException(Exception):
    def __init(self,msg="heap is empty"):
        self.msg=msg
    def __str__(self):
        return self.msg


class heap:
    def __init__(self):
        self.arr=[]

    def create_heap(self,nums):
        for e in nums:
            self.insert(e)
    def insert(self,data):
        index=len(self.arr)
        parent=(index-1)//2

        while(index>0 and self.arr[parent]<data):
            if index==len(self.arr):
                self.arr.append(self.arr[parent])
            else:
                self.arr[index]=self.arr[parent]
            index=parent
            parent=(index-1)//2
        if index==len(self.arr):
            self.arr.append(data)
        else:
            self.arr[index]=data


    def top(self):
        if self.arr==[]:
            raise EmptyHeapException()
        else:
            return self.arr[0]

    def delete(self):
        if self.arr==[]:
            raise EmptyHeapException()
        elif len(self.arr)==1:
            return self.arr.pop()
        else:
            max_value=self.arr[0]
            temp=self.arr.pop()
            index=0
            leftindex=2*index+1
            rightindex=2*index+2
            while(leftindex<len(self.arr)):
                if rightindex<len(self.arr):
                    if self.arr[leftindex]>self.arr[rightindex]:
                        if self.arr[leftindex]>temp:
                            self.arr[index]=self.arr[leftindex]
                            index=leftindex
                        else:
                            break
                    else:
                        if self.arr[rightindex]>temp:
                            self.arr[index]=self.arr[rightindex]
                            index=rightindex
                        else:
                            break
                else:  # no right child
                    if self.arr[leftindex] > temp:
                        self.arr[index] = self.arr[leftindex]
                        index = leftindex
                    else:
                        break
                leftindex=2*index+1
                rightindex=2*index+2
            self.arr[index]=temp
        return max_value

    def heap_sort(self,list1):
        answer=[]
        self.create_heap(list1)
        try:
            while True:
                answer.insert(0,self.delete())
        except EmptyHeapException:
            pass
        print(answer)

    def printheap(self):
        print(self.arr)



obj=heap()
obj.heap_sort([50,40,60,20,70,30,50,30])
obj.printheap()