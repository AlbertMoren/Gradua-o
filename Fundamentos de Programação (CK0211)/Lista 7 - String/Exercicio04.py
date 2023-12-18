'''Write a program that receives a sentence, calculates and displays the number of words in the entered sentence. Before counting the number of words in the sentence, it must undergo the following corrections:
a) Elimination of spaces at the beginning of the sentence.
b) Elimination of spaces at the end of the sentence.
c) Elimination of duplicate spaces between words.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def edit_subroutine(text):
    char_list = list(text)
    new_list = []
    last = char_list[-1]
    for i in range(len(char_list)):
        if char_list[i] != ' ' or last != ' ':
            new_list.append(char_list[i])
            last = char_list[i]
    text = "".join(new_list)
    return text

def count_subroutine(text):
    char_list = list(text)
    count = 0
    for i in range(len(char_list)):
        if char_list[i] == " ":
            count += 1
    return count + 1

# Main
text = input("Enter a text: ").lower()
text = edit_subroutine(text)
print(f"This phrase contains {count_subroutine(text)} words")
