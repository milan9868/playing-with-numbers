from typing import Generator
from PrimeNumberChecker import is_prime


def list_of_primes() -> Generator[int, None, None]:
    for i in range(2, 100000):
        if is_prime(i):
            yield i


tmp_product = 1
primes = []
for prime in list_of_primes():
    tmp_product = tmp_product * prime
    primes.append(prime)
    if not is_prime(tmp_product + 1):
        print(tmp_product + 1)
        print(primes)
        break

