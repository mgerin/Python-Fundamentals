number_of_fills = int(input())
capacity = 255
liters_in_tank = 0

for fills in range(number_of_fills):
    liters = int(input())
    if capacity - liters < 0:
        print('Insufficient capacity!')
        continue
    capacity -= liters
    liters_in_tank += liters
print(liters_in_tank)