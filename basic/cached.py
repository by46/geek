# -:- coding:utf8 -:-
import time
from functools import wraps


def cached(expiration):
    """
    用于缓存计算结果的装饰器

    :param expiration: :class:`int`, 缓存的过期时间，单元秒
    """

    def decorator(func):
        cache = {}
        missing = object()

        @wraps(func)
        def decorated_function(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            result = missing
            if key in cache:
                (cache_hit, expiry) = cache[key]
                if time.time() - expiry < expiration:
                    result = cache_hit

            if result is missing:
                result = func(*args, **kwargs)

            cache[key] = (result, time.time())
            return result

        return decorated_function

    return decorator

if __name__ == '__main__':
    @cached(100)
    def fib(n):
        """
        Fibonacci function
        :param n:
        :return:
        """
        if n == 1 or n == 0:
            return 1
        return fib(n - 1) + fib(n - 2)

    def fib2(n):
        if n == 1 or n == 0:
            return 1
        return fib2(n - 1) + fib2(n - 2)
    fib(50)
    print fib.__doc__
