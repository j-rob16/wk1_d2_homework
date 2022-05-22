# For the following list of numbers:

from ast import Return


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
def fet_evens(list):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

# 2. Print the difference between the largest and smallest value:
def sort_nums(list):
    

    list.sort()
    smallest = list[0]
    largest = list[-1]
    return largest - smallest

# 3. Print True if the list contains a 2 next to a 2 somewhere:

def check_doubles(list):
    result = False
    for index, number in enumerate(list):
        if (number == 2 and list[index - 1] == 2 and index != 0):
            result = True
    return result

print(check_doubles(numbers))

# 4. Print the sum of the numbers,
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

total = 0
found_6 = False
for num in numbers:
    if num == 6:
        found_6 = True
    elif num == 7:
        found_6 = False
    else:
        total += num

print(total)


# 5. HARD! Print the sum of the numbers.
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.

total = 0
for index, number in enumerate(numbers):
    if (number == 13) or (numbers[index - 1] == 13 and index != 0):
        pass
    else: 
        total += number
        