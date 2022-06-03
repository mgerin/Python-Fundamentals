input_string = input()
output_string = ''

while input_string != 'End':
    for letter in range(len(input_string)):
        output_string += input_string[letter] * 2
    if input_string != 'SoftUni':
        print(output_string)
    output_string = ''
    input_string = input()

