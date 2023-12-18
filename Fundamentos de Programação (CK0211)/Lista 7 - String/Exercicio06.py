'''Write a program that receives a sentence and generates a new sentence, duplicating each character of the entered sentence. Example:
Phrase: PROGRAMMING IS GOOD
Output: PPRROOGGRRAAMMMMIINNGG IISS GGOOOODD'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

def edit_subroutine(text):
    list_text = list(text)
    edited_list = []

    for character in list_text:
        if character == " ":
            edited_list.append(character)
        else:
            for _ in range(2):
                edited_list.append(character)

    edited_text = "".join(edited_list)
    return edited_text

# Main
text_input = input("Enter a text: ").lower()
edited_text = edit_subroutine(text_input)
print(edited_text)
