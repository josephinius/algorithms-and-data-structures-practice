import gmpy

class RollingHash(object):
    """An implementation of a rolling hash for strings."""
    
    def __init__(self): 
        """Creates an empty rolling hash."""
        self.base = 257 # let's use prime base of 257 
        self.p = 1000000007 
        self.curhash = 0
        self.ibase = int(gmpy.invert(self.base, self.p)) # multiplicative inverse of the base 
        self.base_to_size_minus_one = self.ibase 
        
    def current_hash(self):
        """Returns the current hash value."""
        return self.curhash 
        
    def append(self, c):
        """Adds letter c to end of string.
        
        Args:
            c: Letter to be added. 
        """
        self.curhash = (self.curhash * self.base + ord(c)) % self.p 
        self.base_to_size_minus_one = (self.base_to_size_minus_one * self.base) % self.p
    
    def skip(self, c):
        """Removes the front letter from string, assuming it is c.
        
        Args:
            c: Letter to be removed. 
        """
        self.curhash = (self.curhash - ord(c) * self.base_to_size_minus_one + self.base * self.p) % self.p 
        # The term (base * p) in curhash is there to guarantee the positivity of the result. 
        self.base_to_size_minus_one = (self.base_to_size_minus_one * self.ibase) % self.p
        
def string_to_hash(s):
    """Converts a string into a RollingHash instance. 
    
    Args:
        s: String to be converted. 
    Returns: 
        rs: Rolling hash. 
    """
    rs = RollingHash()
    for c in s:
        rs.append(c)
    return rs 