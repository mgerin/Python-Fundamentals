input_string = input()
numbers = input_string.split()
opposite_numbers = []

for num in numbers:
    opposite_numbers.append(-int(num))
print(opposite_numbers)
