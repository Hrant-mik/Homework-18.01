
class Node:
    def __init__(self, key, element, next=None):
        self.key = key
        self.element = element
        self.next = next


class LinkedList:
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
    
    def append(self,key, element):
        new_node = Node(key, element)
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
            return
        else:
            while current_node.next:
                print(current_node.element)
                current_node = current_node.next
            print(current_node.element) 

    def copy(self):
        linked_list_copy = LinkedList()
        for i in range(len(self)):
            linked_list_copy.append(self[i])
        return linked_list_copy

    def extend(self, other):
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


class HashTable:
    def __init__(self):
        self.size = 6
        self.my_heshtable = [LinkedList() for _ in range(self.size)]
        
    def out(self):
        for i in self.my_heshtable:
            i.out()
    
    def search(self, key):
        for arrey in self.my_heshtable:
            current_node = arrey.head
            if not current_node:
                continue
            else:
                while current_node.next:
                    if current_node.key == key:
                        print(current_node.element)
                    current_node = current_node.next
                if current_node.key == key:
                        print(current_node.element)
    
    def append_hash(self, key, element):
        index = hash(key) % self.size
        self.my_heshtable[index].append(key, element)
        self.my_heshtable[index].key = key
        
    def insert(self, key, element):
        for arrey in self.my_heshtable:
            current_node = arrey.head
            if not current_node:
                continue
            else:
                while current_node.next:
                    if current_node.key == key:
                        current_node.element = element
                    current_node = current_node.next
                if current_node.key == key:
                        current_node.element = element

hash_table = HashTable()

hash_table.append_hash("hrant", "vazgen")
hash_table.append_hash(44, 12)
hash_table.append_hash("hrant1555", "vazgen00")

hash_table.insert(44, 4)
hash_table.search(44)
