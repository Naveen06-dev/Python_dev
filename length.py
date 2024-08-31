def count_letters(s):
    return sum(1 for char in s if char.isalpha())

input_string = input("Enter a string : ")
letter_count = count_letters(input_string)
print(f"Number of letters: {letter_count}")
