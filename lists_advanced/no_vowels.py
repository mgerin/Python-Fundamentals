vowels = ['a', 'o', 'u', 'e', 'i']
some_string = input()
no_vowels_str = [ch for ch in some_string if ch.lower() not in vowels]

print(''.join(no_vowels_str))
