'''Write a program that receives two strings of characters and checks if the first string entered is a permutation of the second string, that is, if all characters from the first string are present in the second string, even if in different positions. Example:
“abccde” is a permutation of “cbadce”, but is neither “abcdef” nor “abcde”'''

# My signature
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def compare_subroutine(text1, text2):
    list1 = list(text1)
    list2 = list(text2)
    for i in range(len(list1)):
        if list1[i] in list2:
            if i + 1 == len(list1):
                print(f"{text1} is a permutation of {text2}")
            continue
        else:
            print("No")
            break

# Main
text1 = input("Enter a word: ").lower()
text2 = input("Enter another word: ").lower()
compare_subroutine(text1, text2)
