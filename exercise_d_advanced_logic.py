# For the following list of numbers:

from ast import Return


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
for num in numbers:
    if num % 2 == 0:
        print(num)

# 2. Print the difference between the largest and smallest value:
numbers.sort()
smallest = numbers[0]
largest = numbers[-1]
print(largest - smallest)

# 3. Print True if the list contains a 2 next to a 2 somewhere:

# The help of stackoverflow.
numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

for num in range(0, len(numbers) -1):
    if numbers[num] == 2 and (numbers[num+1]) == 2:
        print(True)
    

# 4. Print the sum of the numbers,
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

index_1 = 0
index_2 = 0
for num in numbers:
    if num == 6:
        index_1 = numbers[num]
    else:
        if num == 7:
            index_2 = numbers[num]

no_4_total = 0

for num in numbers:
    if num == 6:
        del(numbers[index_1:index_2])
    else:
        no_4_total += num

print(no_4_total)


# 5. HARD! Print the sum of the numbers.
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.

