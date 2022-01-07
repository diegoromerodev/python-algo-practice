class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1
        return self
    
    def pop(self):
        if self.head is None: return None
    
        tmp = self.head
        prev = tmp
        while tmp is not None:
            prev = tmp
            tmp = tmp.next
            
        self.tail = prev
        prev.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        
        return prev
    
    def shift(self):
        if self.length <= 0: return None
        tmp = self.head
        self.head = tmp.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return tmp

    def unshift(self, value):
        node = Node(value)
        if self.tail is None:
            self.tail = node
        else:
            node.next = self.head

        self.head = node
        self.length += 1
        return self
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        current_index = 0

        while current_index < index:
            current_node = current_node.next
            current_index += 1

        return current_node
    
    def set(self, index, value):
        node = self.get(index)
        if node is None: return False
        
        node.value = value
        return True
    
    def insert(self, index, value):
        node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0: self.unshift(node)
        elif index == self.length: self.push(node)
        else:
            prev = self.get(index - 1)
            next = prev.next
            prev.next = node
            node.next = next
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index > self.length: return False
        elif index == 0: return self.shift()
        elif index == self.length: return self.pop()
        else:
            prev = self.get(index - 1)
            tmp = prev.next
            prev.next = prev.next.next
            self.length -= 1
            return tmp
    def reverse(self):
        if self.head is None or self.tail is None: return False
        curr = self.tail
        tmp = curr.next
        self.tail = self.head
        while tmp is not None:
            saved = tmp.next
            tmp.next = curr
            curr = tmp
            tmp = saved
        return self.tail

sll = SinglyLinkedList()
print(sll.head, sll.tail)
sll.push("Diego")
print(sll.head.value, sll.tail.value)
sll.push("Jose")
print(sll.head.value, sll.tail.value)
sll.push("Arturo")
print(sll.head.value, sll.tail.value)
sll.pop()
print(sll.head.value, sll.tail.value)
sll.unshift("Magaly")
print(sll.head.value, sll.tail.value)
print(sll.get(2).value)
print(sll.set(2, "Jose Romero"))
print(sll.get(2).value)
print(sll.reverse().value, sll.head.value)