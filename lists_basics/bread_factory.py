list_of_events = input().split('|')
total_energy = 100
total_coins = 100
is_bakary_open = True

for event in list_of_events:
    event_info = event.split('-')
    event_type = event_info[0]
    number = int(event_info[1])
    if event_type == 'rest':
        temp_energy = total_energy
        total_energy += number
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - temp_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {total_energy}.')
    elif event_type == 'order':
        if total_energy >= 30:
            total_energy -= 30
            total_coins += number
            print(f'You earned {number} coins.')
        else:
            total_energy += 50
            print('You had to rest!')
    else:
        if total_coins >= number:
            total_coins -= number
            print(f'You bought {event_type}.')
        else:
            print(f'Closed! Cannot afford {event_type}.')
            is_bakary_open = False
            break

if is_bakary_open:
    print('Day completed!')
    print(f'Coins: {total_coins}')
    print(f'Energy: {total_energy}')
