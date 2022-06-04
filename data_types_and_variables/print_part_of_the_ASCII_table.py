first_index = int(input())
last_index = int(input())
final_string = ''

for symbol in range(first_index, last_index + 1):
    final_string += chr(symbol) + chr(32)

print(final_string[0:-1])