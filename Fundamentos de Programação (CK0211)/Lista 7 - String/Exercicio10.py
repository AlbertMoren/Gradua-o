'''Write a program that receives a sentence and a character and checks where in the sentence the character last appears'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def find_last_occurrence(text, character):
    char_list = list(text)
    indices = []
    last_index = -1
    last_space_index = 0

    if " " in char_list:
        for i in range(len(char_list)):
            if char_list[i] == " ":
                indices.append(i)

        last_space_index = indices[-1]

        while last_space_index != len(char_list):
            if char_list[last_space_index] == character:
                last_index = last_space_index
                break
            last_space_index += 1
    else:
        for i in range(len(char_list)):
            if char_list[i] == character:
                last_index = i

    return last_index

# Main
text_input = input("Enter a text: ").lower()
character_input = input("Enter a character: ").lower()

result = find_last_occurrence(text_input, character_input)

if result >= 0:
    print(f"The character '{character_input}' is found at position {result + 1} in the last word of the phrase.")
else:
    print(f"The character {character_input} does not appear in the last word of the phrase.")
