number_of_electrons = int(input())
distributed_electrons = []
current_shell_index = 1

while number_of_electrons > 0:
    max_electron = 2 * (current_shell_index ** 2)
    if max_electron <= number_of_electrons:
        distributed_electrons.append(max_electron)
        number_of_electrons -= max_electron
        current_shell_index += 1
    else:
        distributed_electrons.append(number_of_electrons)
        break

print(distributed_electrons)
