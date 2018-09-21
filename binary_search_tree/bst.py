class RepInvariantError(AssertionError):
    pass 


class BSTNode(object):
    """An implementation of a node in Binary Search Tree (BST). 

    Attributes:
        key: Key associated with node. 
        parent: Reference to parent node; None if node is root
        left: Reference to the left child (key >= left.key); None if no left child
        right: Reference to the right child (key <= right.key); None if no right child
    """

    def __init__(self, key):
        """Inits BSTNode with key."""
        self.key = key 
        self.parent = None 
        self.left = None 
        self.right = None 

    def __str__(self):
        """Returns a string representation of the subtree rooted at this node."""
        l = self.left.__str__() if self.left else None 
        r = self.right.__str__() if self.right else None 
        if l is None and r is None: 
            return str(self.key)
        else: 
            return str(self.key) + "(" + str(l) + "," + str(r) + ")"

    def insert(self, node):
        """Inserts node into the subtree rooted at this node."""
        if self.key > node.key: 
            if self.left is None: 
                self.left = node 
                node.parent = self 
            else: 
                self.left.insert(node) 
        else:
            if self.right is None: 
                self.right = node 
                node.parent = self 
            else: 
                self.right.insert(node)

    def find_min(self):
        """Returns a node with the smallest key in the subtree rooted at this node."""
        current = self 
        while current.left is not None:
            current = current.left 
        return current

    def next_larger(self):
        """Returns a node with the smallest key larger than the key of this node."""
        if self.right is not None:
            return self.right.find_min() 
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent 
        return current.parent

    def find(self, key):
        """Returns node with the specified key from the subtree rooted at this node."""
        if self.key == key:
            return self
        elif self.key > key:
            if self.left is None:
                return None 
            else:
                return self.left.find(key)
        else:
            if self.right is None:
                return None 
            else:
                return self.right.find(key)

    def delete(self):
        """Removes this node from the BST; returns nothing"""
        if self.left is None or self.right is None: 
            if self.parent is not None:
                if self.parent.left is self: 
                    self.parent.left = self.left or self.right 
                else: 
                    self.parent.right = self.left or self.right 
            if self.left is not None: 
                self.left.parent = self.parent
            if self.right is not None:
                self.right.parent = self.parent 
        else: 
            node = self.right.find_min()
            self.key, node.key = node.key, self.key 
            node.delete()

    def check_ri_left_helper(self, key):
        """Subroutine in check_ri(). Checks if the keys of all children are not bigger than key."""
        if self.key > key:
            raise RepInvariantError('Key of a left child bigger than key of an ancestor.')
        if self.left is not None:
            self.left.check_ri_left_helper(key)
        if self.right is not None:
            self.right.check_ri_left_helper(key)

    def check_ri_right_helper(self, key):
        """Subroutine in check_ri(). Checks if the keys of all children are not smaller than key."""
        if self.key < key:
            raise RepInvariantError('Key of a right child smaller than key of an ancestor.')
        if self.left is not None:
            self.left.check_ri_right_helper(key)
        if self.right is not None:
            self.right.check_ri_right_helper(key)

    def check_ri(self):
        """Checks the representation invariant of BST."""
        if self.left is not None:
            if self.left.parent is not self:
                raise RepInvariantError('Incorrect parent pointer of left child.')
            self.left.check_ri_left_helper(self.key)
            self.left.check_ri()
        if self.right is not None:
            if self.right.parent is not self:
                raise RepInvariantError('Incorrect parent pointer of right child.')
            self.right.check_ri_right_helper(self.key)
            self.right.check_ri()
