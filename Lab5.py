import math
#LRU
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self,head=None, tail = None):
        self.head = head
        self.tail = tail
        
    def add_last(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        temp = self.tail
        temp.next = node
        node.prev = temp
        node.next = None
        self.tail = node

    def remove_head(self):
        node = self.head.next
        self.head = node
        node.prev = None
    
    def relocate(self,node):
        print("RELOCATE")
        if node == self.tail:
            return
        n = node.next
        if node == self.head:
            if n:
                n.prev = None
                self.head = n
            self.add_last(node)
            return
        p = node.prev
        p.next = node.next
        n.prev = p
        self.add_last(node)
        
#    def changeVal(self,value):
#        self.tail.value = value
    
class LRU:
    def __init__(self,max_cap):
        self.LRU = {} #dictionary with keys mapped to nodes
        self.max_cap = max_cap #max capacity
        self.list = DoublyLinkedList()  #Doubly Linked List of nodes
        self.size = 0

    def get(self,key):
        if key in self.LRU:
            self.list.relocate(self.LRU[key])
            return self.LRU[key]
        else:
            return -1
    
#        update recently used 
        #Gets the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
        
    def put(self,key,value):
        node = Node(key,value)
        if not key in self.LRU:
            if self.size != self.max_cap:
                self.size += 1
                self.LRU[key] = node
                self.list.add_last(node)
             
            else:
                self.LRU[key] = node
                print("YEET")
                self.list.remove_head()
                self.list.add_last(node)
        else:
            self.list.relocate(self.LRU[key])
            self.list.tail.value = value
#            self.list.changeVal(value)
            
        #Insert or replace the value if the given key is not already in the cache. 
        #When the cache reaches its maximum capacity, it should invalidate the least recently used key
#        before inserting a new key.
    
    def sizeL(self):
       return self.size
        #Returns the number of key/value pairs currently stored in the cache
    
    def max_capacity(self):
        return self.max_cap
    
        # Returns the maximum capacity of the cache

    def printList(self):
        a = self.list.head
        while(a):
            print(a.key, a.value)
            a = a.next


class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    def is_empty(self):
        return len(self.tree) == 0

    def parent(self, i):
        if i == 0:
            return -1000#math.inf does not work
        return self.tree[(i - 1) // 2]

    def left_child(self, i):
        c = 2 * i + 1
        if c >= len(self.tree):
            return -1000 #math.inf does not work
        return self.tree[c]

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return -1000 #math.inf does not work
        return self.tree[c]

    def insert(self, item):
        self.tree.append(item)
        self._percolate_up(len(self.tree) - 1)

    def _percolate_up(self, i):
        if i == 0:
            return

        parent_index = (i - 1) // 2

        if self.tree[parent_index] < self.tree[i]:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()

        root = self.tree[0]
        self.tree[0] = self.tree.pop()

        self._percolate_down(0)

        return root

    def _percolate_down(self, i):

        if self.tree[i] >= max(self.left_child(i), self.right_child(i)):
            return

        max_child_index = 2 * i + 1 if self.left_child(i) > self.right_child(i) else 2 * i + 2

        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)

def heap_sort(list_a):
    heap = MaxHeap()
    for a in list_a:
        heap.insert(a) #put everything in a heap
    i = 0
    while not heap.is_empty():
        list_a[i] = heap.extract_max() #extract greatest value
        i = i+1
    
    
#    Problem B
#
#Given a list of words (strings), print the k most frequent elements in descending order. When you print, you have to print the word and its number of occurrences in the list.
#
#If two words have the same frequency, the word with the lower alphabetical order comes first. 

#Use a heap to receive credit.


def most_freq(arr, k):
   dict = {}
   values = list()
   final = list() #final list of words in order
   same_val = list() #list of words with same value
   for i in range(len(arr)):
       if arr[i] in dict:
           dict[arr[i]] += 1
       else:
           dict[arr[i]] = 1
   for i in dict:
       values.append(dict[i])
   heap_sort(values)  #Heap sorts values of the dictionary
   visited = set()
   print(values)

   i = 0
    
   for j in dict:
       if values[0] == dict[j]:
           same_val.append(j) #start with first word
           visited.add(j)
           i += 1
        
   while i < len(values):
       same_val.sort() #sort all the same value words 
       for m in range(len(same_val)):
           final.append(same_val[m]) #append same value words to final list
       same_val = list()
       for j in dict:
           if values[i] == dict[j] and j not in visited:
               same_val.append(j)
               visited.add(j)
               i += 1

   if len(same_val) != 0:
       same_val.sort()
       for m in range(len(same_val)):
           final.append(same_val[m])
   if k > len(values) or k < 0:
       print("Out of Bounds") #Checks for out of bounds
       return
   print("Top",k, "Most Occuring Values")
   for i in range(k):
        print(final[i])
#   print(final)
        
        
#######################################
#######################################
#######################################
#######################################
#######################################


def main():
    
 lru = LRU(5)
 lru.put("A",8)
 lru.put(6,9)
 lru.put("A",9)
 lru.put("A",8)
 print("yeet")
 lru.put("D",3)
 lru.get("D")
 lru.put("3",3)
 lru.get("A")
 lru.get("")
 lru.put("Q",3)
 lru.printList()
 print("Max Capacity", lru.max_capacity())
 print("Size", lru.sizeL())
 s2 = ["b","b","d","a","a","c","e"]
 strings = ["ba","d","d","d","d","a","a","a","a","a","a","ba","bac","bac","bac","ba","ba"]
 most_freq(s2,3)

main()