'''

* 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

* What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
def check(num, lis):
    for i in lis:
        if num%i != 0:
            return False
    return True

div_nums = [1, 5, 7, 9, 11, 13, 16, 17, 19]
val = 1

while True:
    if check(val, div_nums):
        break
    val = val + 1

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is:", val) #232792560 Time Complexcity = O(n^2)