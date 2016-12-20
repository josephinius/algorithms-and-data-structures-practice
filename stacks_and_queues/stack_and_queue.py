class UnderflowError(Exception):
    pass

class OverflowError(Exception):
    pass

class Element(object):
    """An element in the linked-list implementation of stack or queue."""
    
    def __init__(self, item, pointer):
        """Creates an element.
        
        Args:
            item: Item stored in the element. 
            pointer: Pointer to the next element.
        """
        self.item = item
        self.pointer = pointer 

class Stack(object):
    """An (linked-list) implementation of a stack.""" 
    
    def __init__(self):
        """Creates an empty stack."""
        self.head = None 
            
    def empty(self):
        """Tests whether the stack is empty."""
        if self.head is None:
            return True
        else: 
            return False 
    
    def push(self, a):
        """Pushes a new element to the stack. 
        
        Args:
            a: Item stored in the new element. 
        """
        pointer = self.head 
        element = Element(a, pointer)
        self.head = element 
        
    def pop(self):
        """Pops an element from the stack.
        
        Returns:
            Item of the popped element. 
        Raises:
            UnderflowError if the stack is empty.
        """
        if self.empty(): 
            raise UnderflowError 
        element = self.head 
        self.head = element.pointer 
        return element.item 
        
class QueueArray(object):
    """Fixed-size array implementation of a queue."""
    
    def __init__(self, size):
        """Creates a queue based on a fixed-size array.
        
        Args: 
            size: Size of the array.
        """
        self.array = [None] * size
        self.size = size
        self.read = 0 
        self.write = 0 
        
    def empty(self):
        """Tests whether the queue is empty."""
        if self.read == self.write:
            return True
        else: 
            return False 
    
    def enqueue(self, key):
        """Inserts a key to the queue.
        
        Args:
            key: Key to be inserted.
        Raises:
            OverflowError if the queue is full. 
        """
        if (self.read - self.write == 1) or (self.write - self.read == self.size - 1):
            raise OverflowError
        self.array[self.write] = key
        if self.write == self.size - 1:
            self.write = 0
        else:
            self.write = self.write + 1 
    
    def dequeue(self):
        """Deletes an element from the queue.
        
        Returns: 
            key: Deleted key.
        Raises:
            UnderflowError if the queue is empty.
        """
        if self.empty(): 
            raise UnderflowError
        key = self.array[self.read]
        if self.read == self.size - 1:
            self.read = 0 
        else: 
            self.read = self.read + 1
        return key
    
class QueueLinkedList(object):
    """Linked list implementation of a queue (using head and tail pointers)."""
    
    def __init__(self):
        """Creates a queue based on linked list."""
        self.head = None
        self.tail = None 
        
    def empty(self):
        """Tests whether the queue is empty."""
        if self.head is None:
            return True
        else:
            return False
    
    def enqueue(self, key):
        """Inserts a key to the queue.
        
        Args:
            key: Key to be inserted.
        """
        element = Element(key, None)
        if self.empty():
            self.head = element
        else:
            self.tail.pointer = element
        self.tail = element
            
    def dequeue(self):
        """Deletes an element from the queue.
        
        Returns: 
            Deleted key.
        Raises:
            UnderflowError if the queue is empty.
        """
        if self.empty(): 
            raise UnderflowError 
        element = self.head
        self.head = element.pointer 
        if self.head is None:
            self.tail = None 
        return element.item 
    