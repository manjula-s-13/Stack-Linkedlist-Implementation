class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack_Linked_List:
    def __init__(self):
        self.head=None
    def Push(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node
    def Pop(self):
        if (self.head==None):
            print("NO nodes to delete")
        elif self.head.next==None:
            self.head=None
        else:
            temp=self.head
            while(temp.next.next!=None):      
                temp=temp.next
            temp.next=None
    def Peek(self):
        if (self.head==None):
            print("stack empty")
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            print("Peek item is-->",temp.data)
    def Search(self,data):
        if (self.head==None):
            print("Stack empty")
        else:
            temp=self.head
            count=0
            while(temp!=None):
                if (temp.data==data):
                    print(data," ----> element EXISTS at index",count)
                    return
                count=count+1
                temp=temp.next
            print("Element not found")
    def Isempty(self):
        if self.head==None:
            print("Stack empty")
        else:
            print("Stack is not empty")
    
    def Display(self):
        temp=self.head
        if (temp==None):
            print("Single linked list is empty")
        else:
            while(temp!=None):
                print(temp.data,"->",end='')
                temp=temp.next
print("Implementation of Stack using Linkedlist")
obj=Stack_Linked_List()
while True:
    print("1) Push \n2) Pop  \n3) Peek\n4) Search  \n5) Display \n6) Isempty")
    choice=int(input())
    if choice==1:
        size=int(input("Enter Size of stack : "))
        for item in range (size):
            n=int(input("Enter element to add : "))
            obj.Push(n)
        obj.Display()
        print()
    elif choice==2:
        obj.Pop()
        obj.Display()
        print()
    elif choice==3:
        obj.Peek()
        print()
    elif choice==4:
        n1=int(input("Enter element to Search for : "))
        obj.Search(n1)
        print()
    elif choice==5:
        obj.Display()
        print()
    elif choice==6:
        obj.Isempty()
        print()
    else:
        print("Enter correct choice..!!!")
        print()
