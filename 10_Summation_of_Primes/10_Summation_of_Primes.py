'''
The sum of the primes below 10 is,

                2 + 3 + 5 + 7 = 17

Find the sum of the primes below two million.

'''

import time

sm = 0

def SieveOfEratos(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p*p <= n):
        if (prime[p]):
            for i in range(p*p, n+1, p):
                prime[i] = False
        p = p + 1
    return prime

st_tim = time.perf_counter()

prime = SieveOfEratos(2*10**6)

for i in range(2, 2*10**6 + 1):
    if prime[i]:
        sm = sm + i

end_tim = time.perf_counter()

print("The sum of the primes below two million is:", sm) # Time Complexity = O(n*log(log(n)))
print('Time:', end_tim - st_tim, 'Seconds')