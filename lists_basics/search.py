num_of_inputs = int(input())
key_word = input()
list_of_strings = []
filtered_string = []

for _ in range(num_of_inputs):
    current_string = input()
    list_of_strings.append(current_string)
    if key_word in current_string:
        filtered_string.append(current_string)

print(list_of_strings)
print(filtered_string)
