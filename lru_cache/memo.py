from lru_cache import LRUCacheQueue as LRUCache


def memo(f):
    dp = {}

    def wrapper(*args, **kwargs):
        if (*args, frozenset(kwargs.items())) in dp:
            return dp[(*args, frozenset(kwargs.items()))]
        rv = f(*args, **kwargs)
        dp[(*args, frozenset(kwargs.items()))] = rv
        return rv

    return wrapper


def lru(capacity=512):
    def outer(f):
        cache = LRUCache(capacity)

        def inner(*args, **kwargs):
            if (*args, frozenset(kwargs.items())) in cache:
                return cache[(*args, frozenset(kwargs.items()))]
            rv = f(*args, **kwargs)
            cache[(*args, frozenset(kwargs.items()))] = rv
            return rv
        return inner

    return outer


# @memo
# @lru(10)
def fibonacci(n):
    """Returns n-th number in Fibonacci sequence"""
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# @memo
def factorial(n):
    """Returns n factorial"""
    if n < 2:
        return 1
    return n * factorial(n - 1)
