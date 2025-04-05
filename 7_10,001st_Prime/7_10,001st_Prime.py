'''

* By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the th prime is 13.

* What is the 10,001st prime number?

'''

def is_prime(num):
    for i in range(2, int(num**1/2)):
        if num%i == 0:
            return False
    return True

n = 3
count = 0

while True:
    if is_prime(n):
        count = count + 1
    if count == 10001:
        print("The 10,001st prime number is:", n)
        break
    n = n + 1