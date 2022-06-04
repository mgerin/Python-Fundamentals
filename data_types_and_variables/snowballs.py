number_of_snowballs = int(input())
max_snowball_value = 0

for current_snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        max_snowball_weight = snowball_weight
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality

print(f'{max_snowball_weight} : {max_snowball_time} = {int(max_snowball_value)} ({max_snowball_quality})')