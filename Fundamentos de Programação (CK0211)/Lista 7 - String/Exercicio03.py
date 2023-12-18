'''Write a program that receives a sentence and generates a new one, removing excess spaces at the beginning and end of the sentence and between its words.'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def sub_routine(text):
    char_list = list(text)
    new_list = []
    for i in range(len(char_list)):
        if char_list[i] != " ":
            new_list.append(char_list[i])
    new_text = "".join(new_list)
    print(new_text)

# Main
text = input("Enter a text: ").lower()
sub_routine(text)
