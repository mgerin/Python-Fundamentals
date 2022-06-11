list_of_gifts = input().split()
inputted_command = ''

while inputted_command != 'No Money':
    inputted_command = input()
    commands = inputted_command.split()
    if commands[0] == 'OutOfStock':
        for index in range(len(list_of_gifts)):
            if list_of_gifts[index] == commands[1]:
                list_of_gifts[index] = 'None'
    elif commands[0] == 'Required':
        if int(commands[2]) in range(len(list_of_gifts)):
            list_of_gifts[int(commands[2])] = commands[1]
    elif commands[0] == 'JustInCase':
        list_of_gifts[len(list_of_gifts) - 1] = commands[1]

while 'None' in list_of_gifts:
    list_of_gifts.remove('None')
print(*list_of_gifts)
