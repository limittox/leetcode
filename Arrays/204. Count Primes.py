"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True for _ in range(n)]
        
        primes[0] = primes[1] = False
        
        for i in range(2, n):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        
        return sum(primes)