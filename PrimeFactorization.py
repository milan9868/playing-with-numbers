from typing import List
from ListOfPrimes import list_of_primes


def factorize_to_primes(n:int) -> List[int]:
    factors = []
    for i in list_of_primes():
        if n % i == 0:
            factors.append(i)
            n = n / i
            if n == 1:
                break

    return factors