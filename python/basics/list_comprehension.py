# list numbers from 0 to 9
print("numbers from 0 to 9", [i for i in range(10)])
# list primes to 100
print("primes from 0 to 100", [
    n
    for n in range(100)
    if len([
        i
        for i in range(1,n+1)
        if n % i == 0
        ]) == 2
    ])
"""
[i for i in range(1,n+1) if n % i == 0] creates the list of divisors for outer loop variable n
by definition a prime has exactly 2 divisors which is the filter condition in outer loop [n for n in range(100) if condition]
"""
