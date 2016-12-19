
class RepInvariantError(AssertionError):
    pass

class MaxHeap(object):
    """An implementation of a max heap.""" 
    
    def __init__(self, alist):
        """Creates a max heap. 
        
        Args: 
            alist: Alist from which the max heap is build. 
        """
        self.alist = alist
        self.size = len(alist)
        self.build_max_heap() 
        
    def parent(self, i):
        """Returns index of node's parent (one-based indexing).
        
        Args:
            i: Index of the node. 
        Returns: 
            Index of the node's parent. 
        """
        if i == 1:
            return None
        else:
            return i // 2 
    
    def left(self, i):
        """Returns index of node's left child (one-based indexing).
        
        Args: 
            i: Index of the node. 
        Returns: 
            Index of the node's left child. 
        """
        return 2 * i
    
    def right(self, i):
        """Returns index of node's right child (one-based indexing).
        
        Args:
            i: Index of the node.
        Returns: 
            Index of the node's right child. 
        """
        return 2 * i + 1 
    
    def max_heapify(self, i): 
        """Corrects a single violation of the heap property in a subtree rooted at a node of index i.""" 
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l <= self.size and self.alist[l-1] > self.alist[largest-1]: #condition for max heap
        #if l <= self.size and self.alist[l-1] < self.alist[largest-1]: #condition for min heap
            largest = l
        if r <= self.size and self.alist[r-1] > self.alist[largest-1]: #condition for max heap
        #if r <= self.size and self.alist[r-1] < self.alist[largest-1]: #condition for min heap
            largest = r
        if largest != i:
            self.alist[i-1], self.alist[largest-1] = self.alist[largest-1], self.alist[i-1] 
            self.max_heapify(largest)
        return self
        
    def build_max_heap(self):
        """Produces a max heap from an unordered list."""
        for i in range(self.size // 2, 0, -1):
            self.max_heapify(i)
        #self.ri_check()
        return self 
    
    def extract_max(self):
        """Extract and returns the max element of the max heap."""
        self.alist[0], self.alist[-1] = self.alist[-1], self.alist[0]
        heap_max = self.alist.pop()
        self.size = len(self.alist)
        self.max_heapify(1)
        #self.ri_check()
        return heap_max
    
    def insert(self, value):
        """Inserts value into the max heap."""
        self.alist.append(value)
        self.size = len(self.alist)
        up = self.parent(self.size)
        while up is not None: 
            self.max_heapify(up) 
            up = self.parent(up)
        #self.ri_check()
        return self
            
    def ri_check(self): 
        """Checks if representation invariant is preserved."""
        for i in range(self.size // 2, 0, -1): 
            l = self.left(i)
            r = self.right(i)
            largest = i 
            if l <= self.size and self.alist[l-1] > self.alist[largest-1]: #condition for max heap
            #if l <= self.size and self.alist[l-1] < self.alist[largest-1]: #condition for min heap
                largest = l
            if r <= self.size and self.alist[r-1] > self.alist[largest-1]: #condition for max heap
            #if r <= self.size and self.alist[r-1] < self.alist[largest-1]: #condition for min heap
                largest = r
            if largest != i:
                raise RepInvariantError('Representation invariant is not preserved.')
    
def heap_sort(list_to_sort):
    """Sorts a list using max heap. 
    
    Args:
        list_to_sort: List to sort. 
    Returns: 
        Sorted list. 
    """
    aheap = MaxHeap(list_to_sort)
    result = [] 
    while aheap.size > 0: 
        i = aheap.extract_max()
        result.append(i)
    return result 
    
    