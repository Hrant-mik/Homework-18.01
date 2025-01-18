class Node:
    def __init__(self, element, next = None):
        self.element = element
        self.next = next
        
    
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def __getitem__(self, index):
        current_node = self.head
        for i in range(index):
            if current_node.next:
                current_node = current_node.next
        return current_node.element
    
    def __setitem__(self, index, element):
        current_node = self.head
        for i in range(index):
            if current_node.next:
                current_node = current_node.next
        current_node.element = element
    
    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    
    def out(self):
        current_node = self.head
        if not current_node:
            print(None, end=", ")
        else:
            while current_node.next:
                print(current_node.element, end=", ")
                current_node = current_node.next
            print(current_node.element) 

    def copy(self):
        linked_list_copy = LinkedList()
        for i in range(len(self)):
            linked_list_copy.append(self[i])
        return linked_list_copy

    def extend(self, other):
        # for i in range(len(other)):
        #     self.append(other[i])
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = other.head
            

    def index(self, index):
        current_node = self.head
        count = 0
        while current_node.next:
            if count == index:
                return current_node.element
            current_node = current_node.next
            count += 1 
        if count == index:
                return current_node.element
        
    
    def insert(self, index, element):
        current_node = self.head
        new_node = Node(element)
        count = 0
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            
        while current_node.next:
            if count == index - 1:
                new_node.next = current_node.next
                print(count)
                current_node.next = new_node
            current_node = current_node.next
            count += 1 
        if count == index - 1:
            new_node.next = current_node.next
            print("a")
            current_node.next = new_node
            
            
    
    def pop(self, index):
        current_node = self.head
        count = 0
        a = 0
        while current_node.next:
            count += 1
            if count == index:
                a = current_node.next.element
                current_node.next = current_node.next.next
            current_node = current_node.next 
            if not current_node:
                break
        count += 1 
        if count == index:
            a = current_node.next.element
            current_node.next = current_node.next
        if index == 0:
            first = self.head
            self.head = self.head.next
            return first.element
        return a
    
    def remove(self, element):
        current_node = self.head
        if element == self.head.element:
            self.head = self.head.next
        while current_node.next:
            if current_node.next.element == element:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next 
    
    def reverse(self):
        new_linked_list = LinkedList()
        for i in range(len(self) - 1, -1, -1):
            new_linked_list.append(self[i])
        self.head = new_linked_list.head
            
    
    def sort(self):
        for i in range(len(self)):
            is_sorted = True
            for j in range(1, len(self)):
                if self[j] < self[j - 1]:
                    self[j], self[j - 1] = self[j - 1], self[j]
                    is_sorted = False
            if is_sorted:
                break
    def clear(self):
        self.head = None
        
    def __len__(self):
        current_node = self.head
        count = 0
        if not current_node:
            return 0
        else:
            while current_node.next:
                count += 1
                current_node = current_node.next
            count += 1 
        return count
    
class Iterator:
    def __init__(self, current_node):
        self.current_node = current_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_node:
            element = self.current_node.element
            self.current_node = self.current_node.next
            return element
        else:
            raise StopIteration

def __iter__(self):
        return self.Iterator(self.head)
    
    
            
        
        
# linked_list = LinkedList()

# linked_list.append(5)
# linked_list.append(4)
# linked_list.append(1)
# linked_list.append(16)
# linked_list.append(15)

# linked_list.sort()

# linked_list.out()

