'''Write a program that takes a sentence and shows how many different letters it contains'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def count_unique_characters(text):
    char_list = list(text)
    unique_chars = []

    for char in char_list:
        if char not in unique_chars:
            if char != " ":
                unique_chars.append(char)

    return len(unique_chars)

text_input = input("Enter a text: ").lower()
print(f"This phrase has {count_unique_characters(text_input)} different characters")
