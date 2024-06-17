from typing import Generator
from ListOfPrimes import list_of_primes,is_prime
from PrimeFactorization import factorize_to_primes




tmp_product = 1
primes = []
for prime in list_of_primes():
    tmp_product = tmp_product * prime
    primes.append(prime)
    if not is_prime(tmp_product + 1):
        print(tmp_product + 1)
        print(primes)
        print(factorize_to_primes(tmp_product + 1))
        break

