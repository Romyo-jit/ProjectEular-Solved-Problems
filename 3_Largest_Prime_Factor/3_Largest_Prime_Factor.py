# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

num = 600851475143
limit = int(num**(1/2))
fctors = []

for i in range(2, limit+1):
    if num%i == 0:
        fctors.append(i)

pfac = []
for i in fctors:
    run = True
    for j in range(2, int(i**(1/2)) + 1):
        if i%j == 0:
            run = False
            break
    if run:
        pfac.append(i)

print("The largest prime factor of the numbe: ", max(pfac))