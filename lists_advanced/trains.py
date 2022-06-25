numbers = int(input())
wagons = [0] * numbers

while True:
    command = input()

    if command == 'End':
        break

    data = command.split(' ')
    current_command = data[0]

    if current_command == 'add':
        people_to_add = int(data[1])
        wagons[-1] += int(people_to_add)
    elif current_command == 'insert':
        index = int(data[1])
        people_to_add = int(data[2])
        wagons[index] += people_to_add
    elif current_command == 'leave':
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] -= number_of_people

print(wagons)