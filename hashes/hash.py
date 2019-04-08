
"""
class TableFullError(Exception):
    pass
"""

class Deleted(object):
    """Deleted item."""
    pass 
        
class HashTable(object):
    """An implementation of a hash table. Open addressing with linear probing is used  
    for the resolution of collisions. Table doubling is used for the table resizing."""
        
    def __init__(self):
        """Creates a hash table of size one."""
        self.size = 1
        self.number_of_items = 0 
        self.number_of_deleted = 0 
        self.data = [None] * self.size
            
    def insert(self, key, value):
        """Adds a key-value pair into the table (overwrites any existing key).
        
        Args: 
            key: Key to be inserted (has to be a string). 
            value: Value to be inserted. 
        """
        deleted_index = None 
        for i in range(self.size):
            idx = self._linear_probing(key, i)
            if self.data[idx] is None:  # End of probing sequence 
                if deleted_index is not None:  # Deleted item has been encountered somewhere in probing sequence 
                    break
                self.data[idx] = (key, value)
                self.number_of_items += 1
                return
            elif self.data[idx] is Deleted:
                if deleted_index is None: 
                    deleted_index = idx
            elif self.data[idx][0] == key:  # Overwriting existing key 
                self.data[idx] = (key, value)
                return 
        if deleted_index is not None: 
            self.data[deleted_index] = (key, value)
            self.number_of_deleted -= 1 
            return
        #raise TableFullError # table resizing instead
        self._table_enlarging()
        self.insert(key, value)            
            
    def search(self, key):
        """Returns item with key if it exists. 
        
        Args: 
            key: Key for search. 
        Returns: 
            Item with key if it exists, otherwise None. 
        """
        for i in range(self.size):
            idx = self._linear_probing(key, i)
            if self.data[idx] is None:
                return None
            elif self.data[idx] is Deleted: 
                continue 
            elif self.data[idx][0] == key:
                return self.data[idx]
        return None 
    
    def delete(self, key):
        """Removes item with a key from the table.
        
        Args: 
            key: Key of an item to be removed. 
        Raises:
            KeyError if the key does not exist. 
        """
        for i in range(self.size):
            idx = self._linear_probing(key, i)
            if self.data[idx] is None:
                raise KeyError('Deleting non-existent element.')
            elif self.data[idx] is not Deleted and self.data[idx][0] == key:
                self.data[idx] = Deleted 
                self.number_of_deleted += 1 
                if self.number_of_items - self.number_of_deleted < self.size // 4:
                    self._table_reduction()
                return
        raise KeyError('Deleting non-existent element.')

    def __getitem__(self, key):
        """Square bracket [] accessor for getting the item with key."""
        return self.search(key)

    def __setitem__(self, key, value):
        """Square bracket [] accessor for setting the key-value item."""
        self.insert(key, value)
    
    def _string_hash(self, astring): 
        """Computes a hash of a string.
        
        Args:
            astring: A string. 
        Returns: 
            Hash value. 
        """
        base = 31 # 257 can be used for longer strings
        ahash = 0 
        for c in astring:
            ahash += ahash * base + ord(c) 
        return ahash % self.size 
    
    def _linear_probing(self, key, i):
        """Computes a hash for a key and a trial count i. 
        
        Args: 
            key: A string. 
            i: A trial count. 
        Returns:
            Hash value. 
        """
        return (self._string_hash(key) + i) % self.size
    
    def _quadratic_probing(self, key, i):
        """Computes a hash for a key and a trial count i. 
        Quadratic probing is usually very inefficient. 
        
        Args: 
            key: A string. 
            i: A trial count. 
        Returns:
            Hash value. 
        """
        return (self._string_hash(key) + i + i ** i) % self.size 
    
    def _table_enlarging(self, factor=2):
        """Increases the size of the table by the factor. 
        The old table is re-hashed. 
        
        Args:
            factor: Factor of increase. 
        """
        self.size = self.size * factor 
        self.number_of_items = self.number_of_items - self.number_of_deleted
        self.number_of_deleted = 0 
        self._copy_data()
        
    def _table_reduction(self, factor=2):
        """Reduces the size of the table by a factor. 
        The old table is re-hashed. 
        
        Args:
            factor: Factor of reduction. 
        """
        self.size = self.size // factor 
        self.number_of_items = self.number_of_items - self.number_of_deleted
        self.number_of_deleted = 0 
        self._copy_data()
        
    def _copy_data(self):
        """Re-builds the hash table from scratch."""
        data_new = [None] * self.size
        for item in self.data: 
            if item is None or item is Deleted:
                continue
            else: 
                key, value = item
                for i in range(self.size):
                    idx = self._linear_probing(key, i)
                    if data_new[idx] is None: 
                        data_new[idx] = (key, value)
                        break
        self.data = data_new 
