def orders_func(product: str, quantity: int):
    price = 0
    if product == 'coffee':
        price = 1.50
    elif product == 'coke':
        price = 1.40
    elif product == 'water':
        price = 1.00
    elif product == 'snacks':
        price = 2.00

    return f'{price * quantity:.2f}'


product = input()
quantity = int(input())
print(orders_func(product, quantity))
