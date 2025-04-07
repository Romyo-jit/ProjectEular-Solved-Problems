'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

'''
num_to_10 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

mult_of_10 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

mult_of_100 = [i + "hundred" for i in num_to_10[:9]]

one_and_two_dig = [i for i in num_to_10] ## Final Name For 1 and 2 DIGITS
one_and_two_dig.append("twenty")

for i in mult_of_10:
    for j in num_to_10[:-10]:
        one_and_two_dig.append(i+j)
        if j == "nine":
            try:
                one_and_two_dig.append(mult_of_10[mult_of_10.index(i) + 1])
            except:
                pass

len_to_99 = sum(len(i) for i in one_and_two_dig)

sum_100 = sum(len(i) for i in mult_of_100)

count = 0

for i in mult_of_100:
    for j in one_and_two_dig:
        count += len(i + "and" + j)

for i in "onethousand":
    count += 1

print("If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, total letters would be used is:", count + len_to_99 + sum_100)
