money_left = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
loaf_cost = flour_price + eggs_price + milk_price
baking_bread_cost = milk_price
current_bread_count = 0
number_of_loaves = 0
colored_eggs = 0

while money_left - loaf_cost > 0:
    money_left -= loaf_cost
    number_of_loaves += 1
    colored_eggs += 3
    if money_left - baking_bread_cost > 0:
        current_bread_count += 1
    if number_of_loaves % 3 == 0:
        colored_eggs -= current_bread_count - 2


print(f'You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')
