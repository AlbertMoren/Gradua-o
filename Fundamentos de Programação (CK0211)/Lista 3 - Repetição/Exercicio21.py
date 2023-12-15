# In a presidential election, there are four candidates. Votes are entered using the following codes:
# 1, 2, 3, 4 Votes for the respective candidates
# 5 Null vote
# 6 Blank vote
# Create a program that calculates and displays:
# - The total votes for each candidate
# - The total null votes
# - The total blank votes
# - The percentage of null votes over the total votes
# - The percentage of blank votes over the total votes
# To finish the set of votes, the value is zero. For invalid codes, the program should display a message.

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

contNull = 0
contWhite = 0
contOne = 0
contTwo = 0
contThree = 0
contFour = 0


while True:
    candidate = int(input("Choice your candidade: "))
    if candidate == 0:
        break
    elif candidate == 1 or candidate == 2 or candidate==3 or candidate==4:
        if candidate == 1:
            contOne+=1
        elif candidate == 2:
            contTwo+=1
        elif candidate == 3:
            contThree+=1
        else:
            contFour
    elif candidate == 5:
        contNull+=1
    elif candidate == 6:
        contWhite +=1

print(f"candidade 1 had {contOne}\ncandidade 2 had {contTwo}\ncandidade 3 had {contThree}\ncandidade 4 had {contFour}\nNull votes were {contNull}\nWhite votes were {contWhite}")
