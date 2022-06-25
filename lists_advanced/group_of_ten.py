numbers = list(map(int, input().split(', ')))
group_boundary = 10

while len(numbers) > 0:
    filtered_numbers = [number for number in numbers if number <= group_boundary]
    numbers = [number for number in numbers if number > group_boundary]
    print(f"Group of {group_boundary}'s: {filtered_numbers}")
    group_boundary += 10
