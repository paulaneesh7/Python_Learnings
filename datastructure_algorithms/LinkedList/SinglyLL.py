
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head
        
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        
        # If head is not None, List has elements
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            
            t1.next = new_node
        
        # If head is None, means List is empty
        else:
            self.head = new_node
    
    
    
    
    def insertAtBegining(self, data):
        new_node = Node(data)
        new_node.next = self.head  # If head is None, new_node.next becomes None
        self.head = new_node       # New node becomes the head
            
            
            
    def insertAtMiddle(self, data, pos):
        if pos < 0:
            print("Invalid position")
            return

        new_node = Node(data)

        # Insert at beginning (pos = 0)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse to the node before the insertion point
        current = self.head
        for _ in range(pos - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next

        if current is None:
            print("Position out of bounds")
            return

        # Insert the new node
        new_node.next = current.next
        current.next = new_node
        
    
    
    def deleteLL(self, data):
        t1 = self.head
        
        prev = t1
        
        while(t1.next != None):
            if (t1.data == data):
                prev.next = t1.next
            else:
                prev = t1
                t1 = t1.next
    
    
    def printLL(self):
        temp = self.head
        
        while(temp != None):
            print(temp.data, end=" -> ")
            temp = temp.next
        print()
            

ll_obj = SinglyLinkedList()

ll_obj.insertAtEnd(10)
ll_obj.insertAtEnd(20)
ll_obj.insertAtEnd(30)

ll_obj.printLL()