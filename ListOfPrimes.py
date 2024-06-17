from typing import Generator


def is_prime(n: int) -> bool :
    if n == 2:
        return True
    i = 2
    if n % i == 0 :
        return False
    i = 3
    while i*i <= n :
        if n % i == 0 :
            return False
        i = i + 2

    return True

def list_of_primes() -> Generator[int, None, None]:
    for i in range(2, 100000):
        if is_prime(i):
            yield i