'''by the user. In encryption, the sentence must be inverted and the consonants must be replaced by #. Example:
Phrase: I'M AT SCHOOL
Output: A#O##E A# UO##E UE'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'w', 'y', 'z')

def encrypt_phrase(text):
    char_list = list(text)
    for i in range(len(char_list)):
        for consonant in consonants:
            if char_list[i] == consonant:
                char_list[i] = '#'
    encrypted_text = "".join(char_list)
    print(encrypted_text[::-1])

# Main
text = input("Enter a phrase: ").lower()
encrypt_phrase(text)
