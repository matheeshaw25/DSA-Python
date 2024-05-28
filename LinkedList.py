class Node:
    def __init__(self, value):
        self.value = value # value of data in node
        self.next = None #pointed to the next node

class LinkedList:
    def __init__(self, value):
        new_node = Node(value) # creates new node with given value
        self.head = new_node # set head of linked list to new node
        self.tail =  new_node # set tail of the linked list to new node
        self.length =1 # initialize the length of the linked list to 1

    def print_list(self):
        temp = self.head # assign the temp variable to head
        while temp is not None: # until the temp becomes None (end of list)
            print(temp.value) # print temp value
            temp = temp.next # move the temporary pointer to the next node

    def append(self, value):
        new_node = Node(value) #created the new node
        if self.length==0: #if list is empty
            self.head = new_node #head will be new node
            self.tail = new_node # tail will be new node
        else: # else
            self.tail.next = new_node # the tail.next will be the new_node
            self.tail = new_node #then setting the new node as tail

        self.length+=1 # length is increased by 1
        # return True
    

    def pop(self):

        # pop if the length of the linked list is zero
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head

        while(temp.next): # while temp.next is not none
            pre = temp # pre will be set to temp
            temp = temp.next # temp will be set to temp.next
        self.tail = pre # when temp.next is none , tail will be set to pre
        self.tail.next = None  #next will be none because the item was removed   
        self.length-=1 # decrement the length by 1

        if self.length ==0:
            self.head = None
            self.tail =None
        return temp.value    

    def pop_first(self):
        #if no items in LL
        if self.length == 0:
            return None
        
        # if two or more items in list
        temp = self.head # set temp to head
        self.head = self.head.next # move head by 1
        temp.next = None # set temps next to None
        self.length-=1 # decrement the LL length by 1 

        # only one item in the list
        if self.length ==0:
            self.tail = None
        return temp.value 

my_linked_list = LinkedList(2) # create a linked list with a value 1
# print(my_linked_list.head.value)

my_linked_list.append(1)

# print(my_linked_list.pop()) # returns 2 node
# print(my_linked_list.pop()) # returns 1 node
# print(my_linked_list.pop()) # returns None

print(my_linked_list.pop_first()) # returns 2 node
print(my_linked_list.pop_first()) # returns 1 node
print(my_linked_list.pop_first()) # returns None
