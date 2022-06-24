# solution 1

# numbers = input().split(' ')
# abs_numbers = []
#
# for num in numbers:
#     abs_numbers.append(abs(float(num)))
#
# print(abs_numbers)

# solution 2 - list comprehension
# numbers = list(map(float, input().split(' ')))
# result = [abs(num) for num in numbers]
# print(result)

# solution 3 - function

def abs_numbers(nums):
    result = [abs(num) for num in nums]
    return result

numbers = list(map(float, input().split(' ')))
print(abs_numbers(numbers))
