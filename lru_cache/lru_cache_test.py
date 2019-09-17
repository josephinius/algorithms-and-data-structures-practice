import unittest
import lru_cache
import memo


class SimpleCasesFibonacci(unittest.TestCase):

    def test_capacity_1(self):
        """Tests LRUCache with capacity of 1 item"""
        capacity = 1
        lru_list = lru_cache.LRUCacheDict(capacity)
        lru_heap = lru_cache.LRUCacheHeap(capacity)
        lru_queue = lru_cache.LRUCacheQueue(capacity)
        tuple_of_lrus = (lru_list, lru_heap, lru_queue)
        for lru in tuple_of_lrus:
            self.assertRaises(KeyError, lambda x: lru[x], 0)
            lru[1] = 100
            self.assertEqual(lru[1], 100)
            lru[2] = 200
            self.assertRaises(KeyError, lambda x: lru[x], 1)
            self.assertEqual(lru[2], 200)
            lru[2] = 20
            self.assertEqual(lru[2], 20)

    def test_capacity_2(self):
        """Tests LRUCache with capacity of 2 item"""
        capacity = 2
        lru_list = lru_cache.LRUCacheDict(capacity)
        lru_heap = lru_cache.LRUCacheHeap(capacity)
        lru_queue = lru_cache.LRUCacheQueue(capacity)
        tuple_of_lrus = (lru_list, lru_heap, lru_queue)
        for lru in tuple_of_lrus:
            lru[1] = 100
            lru[2] = 200
            self.assertEqual(lru[2], 200)
            self.assertEqual(lru[1], 100)
            lru[3] = 300
            self.assertRaises(KeyError, lambda x: lru[x], 2)
            self.assertTrue(1 in lru)
            self.assertFalse(2 in lru)
            self.assertTrue(3 in lru)
            self.assertEqual(lru[1], 100)
            self.assertEqual(lru[3], 300)
            lru[1] = 10  # updating value for key = 1
            lru[4] = 400  # inserting new key, value pair
            self.assertRaises(KeyError, lambda x: lru[x], 3)
            self.assertEqual(lru[1], 10)
            self.assertEqual(lru[4], 400)

    def test_capacity_3(self):
        """Tests LRUCache with capacity of 3 item"""
        capacity = 3
        lru_list = lru_cache.LRUCacheDict(capacity)
        lru_heap = lru_cache.LRUCacheHeap(capacity)
        lru_queue = lru_cache.LRUCacheQueue(capacity)
        tuple_of_lrus = (lru_list, lru_heap, lru_queue)
        for lru in tuple_of_lrus:
            lru[1] = 100
            lru[2] = 200
            lru[3] = 300
            lru[4] = 400
            self.assertRaises(KeyError, lambda x: lru[x], 1)
            lru[2] = 20  # updating value for key = 2
            lru[5] = 500  # inserting new key, value par
            self.assertRaises(KeyError, lambda x: lru[x], 3)
            self.assertTrue(2 in lru)
            self.assertEqual(lru[4], 400)
            self.assertEqual(lru[2], 20)
            self.assertEqual(lru[5], 500)
            lru[6] = 600
            self.assertFalse(4 in lru)
            self.assertTrue(2 in lru)
            self.assertTrue(5 in lru)
            self.assertTrue(6 in lru)
            lru[2] = 2000  # updating value for key = 2
            lru[7] = 700
            lru[8] = 800
            self.assertTrue(2 in lru)
            self.assertFalse(5 in lru)
            self.assertFalse(6 in lru)
            self.assertEqual(lru[8], 800)
            self.assertEqual(lru[2], 2000)
            self.assertEqual(lru[7], 700)

    def test_fibonacci(self):
        """Tests LRUCacheQueue for recursive function calls (Fibonacci)"""
        f1 = lambda n: 1 if n < 2 else f1(n - 1) + f1(n - 2)
        f1 = memo.memo(f1)
        f2 = lambda n: 1 if n < 2 else f2(n - 1) + f2(n - 2)
        f2 = memo.lru(10)(f2)
        self.assertEqual(f1(42), f2(42))
        for n in range(100):
            self.assertEqual(f1(n), f2(n))

    def test_factorial(self):
        """Tests LRUCacheQueue for recursive function calls (factorial)"""
        f1 = lambda n: 1 if n < 2 else n * f1(n - 1)
        f1 = memo.memo(f1)
        f2 = lambda n: 1 if n < 2 else n * f2(n - 1)
        f2 = memo.lru(10)(f2)
        self.assertEqual(f1(42), f2(42))
        for n in range(100):
            self.assertEqual(f1(n), f2(n))


if __name__ == '__main__':
    unittest.main()
