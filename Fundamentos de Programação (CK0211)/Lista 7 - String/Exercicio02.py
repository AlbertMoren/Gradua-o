'''Write a program that takes a sentence and displays each word in it on a separate line. Example:
Quote: COMPUTERS ARE POWERFUL MACHINES
Exit:
COMPUTERS
THEY ARE
MACHINES
POWERFULS'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def sub_routine(text):
    for i in range(len(text)):
        if text[i] != ' ':
            print(text[i], end="")
        else:
            print("")

# Main
text = input("Enter a text: ").lower()
sub_routine(text)
