'''Make a program that takes a sentence and a character and checks whether the character entered is found in the sentence or not, and if it is found, how many times it happens.'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def count_occurrences(text, character):
    char_list = list(text)
    count = 0

    if character in char_list:
        for char in char_list:
            if char == character:
                count += 1

    return count

text_input = input("Enter a text: ").lower()
character_input = input("Enter a character: ").lower()

result = count_occurrences(text_input, character_input)

if result > 0:
    print(f"The character '{character_input}' appears {result} times in the phrase.")
else:
    print(f"The character {character_input} does not appear in the phrase.")
