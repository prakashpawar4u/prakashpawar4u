class Node:
	def __init__(self, data):
		self.data = data #Assign  data
		self.next = None #initialize next as nul

class LinkedList:
    #Function to initialize head
    def __init__(self):
    	self.head = None


    def printList(self):
    	temp = self.head
    	while(temp):
    		print (temp.data)
    		temp = temp.next



if __name__ == '__main__':
         llist = LinkedList()
         llist.head = Node(1)
         second = Node(2)
         third = Node(3)
         llist.head.next = second; #Link first node with second 
         second.next = third;
         llist.printList()


