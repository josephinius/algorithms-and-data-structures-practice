
class TrieNode(object):
    """A node in the Trie.""" 
    
    def __init__(self, parent, is_word):
        """Creates a node.
        
        Args:
            parent: The node's parent.
            is_word: Is is a complete word or not. 
            children: Pointers to children nodes. 
        """
        self.parent = parent
        self.is_word = is_word 
        self.children = {}
        
    def find(self, word, stem=False):
        """Finds and returns the node with word word from the subtrie rooted at this 
        node. Stem search finds and returns a node with the corresponding stem. 
        
        Args:
            word: The word/stem of the node we want to find.
            stem: Specifies if searching a word (False) or a stem (True). 
        
        Returns:
            The node with word word, or the node with the corresponding stem (when stem is True).
        """
        current = self
        level = 0
        while level < len(word):
            c = word[level]
            if c in current.children:
                current = current.children[c]
            else:
                return 
            level += 1 
        if not stem: 
            if current.is_word: return current 
        else: 
            return current 
        
    def insert(self, node):    
        """Inserts a node into the subtrie rooted at this node.
        
        Args:
            node: The node to be inserted.
        """
        current = self
        level = 0
        while level < len(node.text) - 1: 
            c = node.text[level] 
            if c in current.children:
                current = current.children[c] 
            else: 
                blank_node = TrieNode(current, False)
                current.children[c] = blank_node 
                current = blank_node
            level += 1
        c = node.text[level]
        if c in current.children:
            if current.children[c].is_word:
                return
            else: 
                current.children[c].is_word = True 
                current.children[c].text = node.text 
        else: 
            current.children[c] = node 
            node.parent = current 
                
    def level_order_traversal(self):
        """Returns the list of words from shortest to longest in the subtrie rooted at this node."""
        level_order = []
        if self.is_word: level_order.append(self.text)
        frontier = [self]
        #level = { self: 0 }
        i = 1
        while frontier: 
            new = [] 
            for u in frontier: 
                for c in u.children:
                    v = u.children[c]
                    #if v not in level: # this is always TRUE
                    #level[v] = i
                    if v.is_word:
                        level_order.append(v.text)
                    new.append(v)
            frontier = new 
            i += 1 
        return level_order 
        
class Trie(object):
    """An implementation of a trie.""" 
    
    def __init__(self):
        """Creates an empty trie."""
        self.root = None 
        
    def find(self, word):
        """Finds and returns the node with word word from this trie.
        
        Args:
            word: The word of the node we want to find.
        
        Returns:
            The node with word word or None is the trie is empty.
        """
        return self.root and self.root.find(word)
    
    def find_stem(self, word):
        """Finds and returns the node of stem corresponding to word from this trie.
        
        Args:
            word: The stem corresponding to the node we want to find.
        
        Returns:
            The node of stem corresponding to word or None is the trie is empty.
        """
        return self.root and self.root.find(word, True)
    
    def insert(self, word):
        """Inserts a node with word word into this trie. 
        
        Args:
            word: The word of the node to be inserted.
        """
        assert isinstance(word, str)
        assert len(word) > 0 
        node = TrieNode(None, True)
        node.text = word
        if self.root is None:
            self.root = TrieNode(None, False)
        self.root.insert(node)
            
    # atrie.autocomplete('') will return all words in a trie 
    def autocomplete(self, word):
        """Finds the node of stem matching word in this trie and returns the result of level order traversal 
        started at the node that was found.
        
        Args:
            word: The word to be completed. 
        """
        assert isinstance(word, str)
        node = self.find_stem(word)
        return node and node.level_order_traversal() 
        