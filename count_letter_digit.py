name = input("Enter the string :: ")

letter_count = 0
digit_count = 0

for char in name:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1


print("The number of letter :: ",letter_count)
print("The number of digit :: ",digit_count)
