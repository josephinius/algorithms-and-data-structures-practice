"""

Least Recently Used (LRU) cache

- LRUCacheDict: implementation based on dictionary with O(n) time-complexity

- LRUCacheHeap: implementation based on dictionary and min-heap with O(log(n)) time-complexity

- LRUCacheQueue: implementation based on dictionary and queue with O(1) time-complexity

"""


class LRUCacheDict:

    def __init__(self, capacity):
        self.adict = {}  # key: [value, priority]
        self.capacity = capacity

    def get(self, key):
        if key not in self.adict:
            raise KeyError
        val = self.adict[key][0]
        i = self.adict[key][1]
        self.adict[key][1] = self.capacity
        for k in self.adict.keys():
            if k == key:
                continue
            if self.adict[k][1] > i:
                self.adict[k][1] -= 1
        return val

    def __getitem__(self, key):
        return self.get(key)

    def set(self, key, value):
        i = 0
        if key in self.adict:
            i = self.adict[key][1]
        self.adict[key] = [value, self.capacity]
        key_to_remove = None
        for k in self.adict.keys():
            if k == key:
                continue
            if self.adict[k][1] > i:
                self.adict[k][1] -= 1
            if self.adict[k][1] == 0:
                key_to_remove = k
        if key_to_remove is not None:
            del self.adict[key_to_remove]

    def __setitem__(self, key, val):
        self.set(key, val)

    def __contains__(self, key):
        """Checks whether key is in cache without changing its priority."""
        return key in self.adict


class VLItem:

    def __init__(self, value, location):
        self.val = value
        self.loc = location


class HeapElement:

    def __init__(self, key, time_stamp):
        self.key = key
        self.time_stamp = time_stamp

    def __lt__(self, other):
        return self.time_stamp < other.time_stamp


class LRUCacheHeap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.time_step = 0
        self.storage = []  # min heap
        self.vl_dict = {}  # values are VLItem objects

    def parent(self, i):
        if i == 1:
            return None
        return i // 2

    def heapify(self, i):  # min heapify at location i
        size = len(self.storage)
        l = 2 * i
        r = 2 * i + 1
        smallest = i
        if l <= size and self.storage[l - 1] < self.storage[smallest - 1]:
            smallest = l
        if r <= size and self.storage[r - 1] < self.storage[smallest - 1]:
            smallest = r
        if smallest != i:
            self.storage[i - 1], self.storage[smallest - 1] = self.storage[smallest - 1], self.storage[i - 1]
            self.vl_dict[self.storage[i - 1].key].loc = i - 1
            self.vl_dict[self.storage[smallest - 1].key].loc = smallest - 1
            self.heapify(smallest)

    def find_min_key(self):
        return self.storage[0].key

    def replace_min(self, key, val):
        del self.vl_dict[self.find_min_key()]
        self.storage[0] = HeapElement(key, self.time_step)
        self.vl_dict[key] = VLItem(val, 0)
        self.heapify(1)

    def get(self, key):
        if key not in self.vl_dict:
            raise KeyError
        value = self.vl_dict[key].val
        loc = self.vl_dict[key].loc
        self.storage[loc].time_stamp = self.time_step  # update priority of the current element
        self.heapify(loc + 1)
        self.time_step += 1
        return value

    def __getitem__(self, key):
        return self.get(key)

    def set(self, key, val):
        if key in self.vl_dict:
            self.vl_dict[key].val = val
            loc = self.vl_dict[key].loc
            self.storage[loc].time_stamp = self.time_step  # update priority of the current element
            self.heapify(loc + 1)
        else:
            if len(self.storage) == self.capacity:
                self.replace_min(key, val)
            else:
                # newly inserted key has the largest heap key (min-heap property is preserved)
                self.storage.append(HeapElement(key, self.time_step))
                self.vl_dict[key] = VLItem(val, len(self.storage) - 1)
        self.time_step += 1

    def __setitem__(self, key, val):
        self.set(key, val)

    def __contains__(self, key):
        """Checks whether key is in cache without changing its priority."""
        return key in self.vl_dict


class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, node):
        if self.head is None:  # dll is empty
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
        self.tail = node
        self.size += 1

    def popleft(self):
        if self.head is None:
            raise IndexError('popleft from empty list')
        node = self.head
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        node.prev = None
        node.next = None
        self.size -= 1
        return node

    def pop(self):
        if self.head is None:
            raise IndexError('pop from empty list')
        node = self.tail
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        node.prev = None
        node.next = None
        self.size -= 1
        return node

    def delete(self, node):
        if node is None:
            return
        if node is self.head:
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1
        node.next = None
        node.prev = None


class LRUCacheQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.dll = DoublyLinkedList()
        self.adict = {}

    def get(self, key):
        if key not in self.adict:
            raise KeyError
        node = self.adict[key]
        value = node.value[1]
        self.dll.delete(node)
        self.dll.append(node)
        return value

    def __getitem__(self, key):
        return self.get(key)

    def set(self, key, val):
        if key in self.adict:
            node = self.adict[key]
            node.value[1] = val
            self.dll.delete(node)
            self.dll.append(node)
            return
        node = Node([key, val])
        self.adict[key] = node
        if self.dll.size == self.capacity:
            node_to_delete = self.dll.popleft()
            del self.adict[node_to_delete.value[0]]
        self.dll.append(node)

    def __setitem__(self, key, val):
        self.set(key, val)

    def __contains__(self, key):
        """Checks whether key is in cache without changing its priority."""
        return key in self.adict
