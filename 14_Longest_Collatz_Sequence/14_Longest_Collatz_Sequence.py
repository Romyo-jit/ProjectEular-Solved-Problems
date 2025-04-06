'''

The following iterative sequence is defined for the set of positive integers:

            n --> n/2 (n is even)
            n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

        13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

import time, functools

@functools.lru_cache(maxsize=None)
def collaz_conjec(num):
    if num == 1:
        return 1
    if num%2 == 0:
        num = num//2
    else:
        num = num*3 + 1
    return 1 + collaz_conjec(num)

long_chain = 0
ans = 0

st_tim = time.perf_counter()

for i in range(1, 10**6-1):
   chain = collaz_conjec(i)
   if chain > long_chain:
       long_chain = chain
       ans = i

end_tim = time.perf_counter()

print("Longest Chain under 1 million is:", ans)
print('Time:', end_tim - st_tim, 'Seconds')