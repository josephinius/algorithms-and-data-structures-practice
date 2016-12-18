
class SLLNode(object):
    """A node in the singly linked list."""
    
    def __init__(self, value):
        """Creates a node.
        
        Args:
            value: Value at the node.
        """
        self.value = value
        self.next_node = None 
        
class SinglyLinkedList(object):
    """An implementation of a singly linked list.""" 
    
    def __init__(self, data=None):
        """Creates a singly linked list. 
        
        Args: 
            data: A list of values to initialise the singly linked list (optional). 
        """
        self.head = None 
        if data is not None:
            for value in data:
                self.append(value)
                
    def __str__(self):
        """Returns a string representation of the singly linked list."""
        result = [] 
        node = self.head
        while node is not None:
            result.append(str(node.value))
            node = node.next_node 
        return '[' + ', '.join(result) + ']'
        
    def append(self, value):
        """Appends a node with the value to the singly linked list.
        
        Args: 
            value: Value to be appended. 
        """
        node = SLLNode(value)
        if self.head is None: 
            self.head = node 
        else: 
            tail_node = self.head
            while tail_node.next_node is not None: 
                tail_node = tail_node.next_node
            tail_node.next_node = node 
        
    def remove_value(self, value):
        """Removes and returns first node with its value being equal to value. 
        
        Args: 
            value: Value to be removed. 
        Returns:
            The first node of given value, if such node exists. 
        Raises: 
            ValueError() if no such value exists in the list. 
        """
        if self.head is None: 
            raise ValueError('Deleting from empty list.')
        node = self.head 
        if node.value == value: 
            self.head = self.head.next_node 
            return node 
        while node.next_node is not None:
            current = node.next_node 
            if current.value == value:
                node.next_node = current.next_node 
                return current 
            node = current
        raise ValueError('Deleting non-existing value.')
        
    def size(self):
        """Returns the size of a linked list."""
        size = 0 
        node = self.head 
        while node is not None:
            size += 1 
            node = node.next_node 
        return size

    def _kth_to_last_recursive(self, head, k):
        """Subroutine used in kth_to_last_recursive. 
        
        Args:
            head: A node in the singly linked list. 
            k: The index to the last node. 
            
        Returns:
            node: k-th node to the last. 
            index: The index of the current node (i.e. head).  
        """
        if head is None:
            return None, 0 
        node, index = self._kth_to_last_recursive(head.next_node, k) 
        index += 1 
        if index == k:
            return head, index
        return node, index 
        
    def kth_to_last_recursive(self, k):
        """Returns the value of the k-th node to the last node in the singly linked list. 
        Indexing starts by k=1 (i.e. the last element is indexed as k=1).
        (Method is implemented recursively.)
        
        Args: 
            k: The index to the last node. 
            
        Returns: 
             Value of the k-th node to the last. 
        """
        node, _ = self._kth_to_last_recursive(self.head, k)
        if node is None:
            raise IndexError('List index out of range')
        else:
            return node.value
    
    def _kth_to_last_recursive_1(self, head, k, idx):
        """Subroutine used in kth_to_last_recursive_1. 
        
        Args:
            head: A node in the singly linked list. 
            k: The index to the last node. 
            idx: Index class object representing the index of the current node (i.e. head).
            
        Returns:
            node: k-th node to the last. 
        """
        if head is None:
            return None
        node = self._kth_to_last_recursive_1(head.next_node, k, idx) 
        idx.index += 1 
        if idx.index == k:
            return head
        return node 
        
    def kth_to_last_recursive_1(self, k):
        """Returns the value of the k-th node to the last node in the singly linked list. 
        Indexing starts by k=1 (i.e. the last element is indexed as k=1).
        (Method is implemented recursively, using the custom Index class.)
        
        Args: 
            k: The index to the last node. 
            
        Returns: 
             Value of the k-th node to the last. 
        """
        class Index(object):
            def __init__(self):
                self.index = 0
        idx = Index()
        node = self._kth_to_last_recursive_1(self.head, k, idx)
        if node is None:
            raise IndexError('List index out of range')
        else:
            return node.value
    
    def _kth_to_last_iterative(self, head, k): #
        """Subroutine used in kth_to_last_iterative. 
        
        Args:
            head: A node in the singly linked list. 
            k: The index to the last node. 
            
        Returns:
            node2: k-th node to the last. 
        """
        node1 = head
        node2 = None 
        flag = False 
        i = 0 
        while node1 is not None:
            i += 1 
            node1 = node1.next_node 
            if flag: 
                node2 = node2.next_node 
            if i == k:
                flag = True 
                node2 = head 
        return node2 
    
    def kth_to_last_iterative(self, k): 
        """Returns the value of the k-th node to the last node in the singly linked list. 
        Indexing starts by k=1 (i.e. the last element is indexed as k=1).
        (Method is implemented iteratively using the "runner" technique.)
        
        Args: 
            k: The index to the last node. 
            
        Returns: 
             Value of the k-th node to the last. 
        """
        node = self._kth_to_last_iterative(self.head, k)
        if node is None:
            raise IndexError('List index out of range')
        else:
            return node.value
        
    def _get_node_at(self, index): 
        """Returns node in the position given by index. 
        Zero-based indexing is employed. 
        Negative indexing as in Python list.
        
        Args: 
            index: Index of the node.
            
        Returns:
            Node in the position given by index. 
        """
        assert isinstance(index, int)        
        if index >= 0: 
            steps = index 
        else:
            steps = self.size() + index
            if steps < 0:
                return None 
        node = self.head
        while steps > 0 and node is not None:
            node = node.next_node
            steps -= 1 
        return node 
    
    def _value_at(self, index):
        """Returns value of the node in the position given by index.
        
        Args: 
            index: Index of the node. 
            
        Returns: 
            Value of the node in the position given by index. 
        """
        node = self._get_node_at(index)
        if node is None:
            raise IndexError('List index out of range.')
        return node.value 
    
    def __getitem__(self, index): 
        """Returns value of the node in the position given by index.
        
        Args: 
            index: Index of the node. 
            
        Returns: 
            Value of the node in the position given by index. 
        """
        return self._value_at(index)

    def reverse(self): 
        """Reverses the singly linked list."""
        current = self.head
        previous = None 
        while current is not None:
            next_node = current.next_node 
            current.next_node = previous
            current, previous = next_node, current 
        self.head = previous  
    
class DLLNode(object):
    """A node in the doubly linked list."""
    
    def __init__(self, value):
        """Creates a node.
        
        Args:
            value: Value at the node.
        """
        self.value = value
        self.prev_node = None
        self.next_node = None 
        
class DoublyLinkedList(object):
    """An implementation of a doubly linked list.""" 

    def __init__(self, data=None): 
        """Creates a doubly linked list. 
        
        Args: 
            data: A list of values to initialise the doubly linked list (optional). 
        """
        self.head = None
        self.tail = None
        if data is not None:
            for value in data:
                self.append(value)
        
    def __str__(self):
        """Creates a string representation of the linked list."""
        result = [] 
        node = self.head
        while node is not None:
            result.append(str(node.value))
            node = node.next_node 
        return '[' + ', '.join(result) + ']'
        
    def append(self, value):
        """Appends a node with the value to the doubly linked list.
        
        Args: 
            value: Value to be appended. 
        """
        node = DLLNode(value)
        if self.head is None: 
            self.head = node 
            self.tail = node 
        else: 
            self.tail.next_node = node 
            node.prev_node = self.tail 
            self.tail = node
            
    def remove_value(self, value): 
        """Removes and returns first node with its value being equal to value. 
        
        Args: 
            value: Value to be removed. 
        Returns:
            The first node of given value, if such node exists. 
        Raises: 
            ValueError() if no such value exists in the list. 
        """
        if self.head is None: 
            raise ValueError('Deleting from empty list.')
        node = self.head 
        if node.value == value: 
            self.head = self.head.next_node 
            if self.head is None: 
                self.tail = None
            else:
                self.head.prev_node = None 
            return node 
        while node.next_node is not None:
            node = node.next_node 
            if node.value == value:
                node.prev_node.next_node = node.next_node 
                if node.next_node is None: 
                    self.tail = node.prev_node                                 
                else:
                    node.next_node.prev_node = node.prev_node
                return node
        raise ValueError('Deleting non-existing value.')
            
    def size(self):
        """Returns the size of a linked list."""
        size = 0 
        node = self.head 
        while node is not None:
            size += 1 
            node = node.next_node 
        return size

    def _get_node_at(self, index):
        """Returns node in the position given by index. 
        Zero-based indexing is employed. 
        Negative indexing as in Python list.
        
        Args: 
            index: Index of the node.
            
        Returns:
            Node in the position given by index. 
        """
        assert isinstance(index, int)
        from_head = True if index >= 0 else False 
        if from_head: 
            node = self.head
            steps = index 
        else:
            node = self.tail 
            steps = abs(index) -1         
        while steps > 0 and node is not None:
            node = node.next_node if from_head else node.prev_node 
            steps -= 1 
        return node 
    
    def _value_at(self, index):
        """Returns value of the node in the position given by index.
        
        Args: 
            index: Index of the node. 
            
        Returns: 
            Value of the node in the position given by index. 
        """
        node = self._get_node_at(index)
        if node is None:
            raise IndexError('List index out of range.')
        return node.value 
    
    def __getitem__(self, index):
        """Returns value of the node in the position given by index.
        
        Args: 
            index: Index of the node. 
            
        Returns: 
            Value of the node in the position given by index. 
        """
        return self._value_at(index)
    
    def push_front(self, value): 
        """Inserts node at the beginning. 
        
        Args: 
            value: Value of node to be inserted. 
        """
        node = DLLNode(value)
        if self.head is None:
            self.tail = node 
        else: 
            self.head.prev_node = node 
            node.next_node = self.head
        self.head = node 
        
    def pop_front(self):
        """Extract node at the beginning.
        
        Returns: 
            Value of the node at the beginning. 
            
        Raises: 
            IndexError if list is empty. 
        """
        if self.head is None:
            raise IndexError('pop_front from empty list')
        node = self.head 
        if node.next_node is None:
            self.tail = None 
        else: 
            node.next_node.prev_node = None 
        self.head = node.next_node
        return node.value 
    
    def pop_back(self):
        """Extract node at the end.
        
        Returns: 
            Value of the node at the end. 
            
        Raises: 
            IndexError if list is empty. 
        """
        if self.head is None:
            raise IndexError('pop_back to empty list')
        node = self.tail 
        if node.prev_node is None:
            self.head = None
        else:
            node.prev_node.next_node = None
        self.tail = node.prev_node
        return node.value
    
    def _update_value_at(self, index, value):
        """Updates value of the node in the position given by index.
        
        Args: 
            index: Index of the node. 
            value: New value to be set.             
        """
        node = self._get_node_at(index)
        if node is None:
            raise IndexError('List index out of range.')
        node.value = value 
    
    def __setitem__(self, index, value):
        """Updates value of the node in the position given by index.
        
        Args: 
            index: Index of the node. 
            value: New value to be set.             
        """
        self._update_value_at(index, value)
    
    def insert(self, index, value):
        """Inserts node with the value at the position given by index. 
        
        Args: 
            index: Position of node to be inserted. 
            value: Value of node to be inserted. 
        """
        if self.head is None:
            self.append(value)
            return
        
        from_head = True if index >= 0 else False 
        if from_head: 
            node = self.head
            steps = index 
        else:
            node = self.tail 
            steps = abs(index) -1         
        while steps > 0 and node is not None:
            node = node.next_node if from_head else node.prev_node 
            steps -= 1 
            
        if node is None:
            if from_head: 
                self.append(value)
                return
            else:
                self.push_front(value)
                return
        if node is self.head:
            self.push_front(value)
            return
        else:
            new_node = DLLNode(value)
            new_node.next_node = node
            new_node.prev_node = node.prev_node
            node.prev_node.next_node = new_node
            node.prev_node = new_node 
            return
            
    def erase(self, index):
        """Erases a node at the position given by index. 
        
        Args:
            index: Position of node to be erased. 
            
        Returns: 
            Value of the erased node. 
            
        Raises: 
            IndexError if the index is out of range. 
        """
        node = self._get_node_at(index)        
        if node is None:
            raise IndexError('List index out of range.') 
        if node == self.head: 
            if node.next_node is None:
                self.tail = None 
            else: 
                node.next_node.prev_node = None 
            self.head = node.next_node
        elif node == self.tail: 
                node.prev_node.next_node = None 
                self.tail = node.prev_node
        else: 
            node.prev_node.next_node = node.next_node
            node.next_node.prev_node = node.prev_node
        return node.value 
    
    def reverse(self): 
        """Reverses the doubly linked list."""
        node = self.head
        while node is not None:
            next_node = node.next_node 
            node.next_node, node.prev_node = node.prev_node, node.next_node 
            node = next_node
        self.head, self.tail = self.tail, self.head
