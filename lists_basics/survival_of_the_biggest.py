nums_as_string = input().split()
count_to_remove = int(input())
nums_as_digits = []

for index in range(len(nums_as_string)):
    nums_as_digits.append(int(nums_as_string[index]))

for _ in range(count_to_remove):
    nums_as_digits.remove(min(nums_as_digits))

print(*nums_as_digits, sep=', ')
