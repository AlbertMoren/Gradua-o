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

# Initialize variables
votes_candidate_1 = 0
votes_candidate_2 = 0
votes_candidate_3 = 0
votes_candidate_4 = 0
null_votes = 0
blank_votes = 0
total_votes = 0

# Voting process
while True:
    vote = int(input("Enter your vote (1, 2, 3, 4, 5, 6), or enter 0 to finish: "))
    
    if vote == 0:
        break
    
    if vote >= 1 and vote <= 4:
        if vote == 1:
            votes_candidate_1 += 1
        elif vote == 2:
            votes_candidate_2 += 1
        elif vote == 3:
            votes_candidate_3 += 1
        elif vote == 4:
            votes_candidate_4 += 1
    elif vote == 5:
        null_votes += 1
    elif vote == 6:
        blank_votes += 1
    else:
        print("Invalid vote. Please enter a valid code.")

    total_votes += 1

# Display results
print(f"\nTotal votes for Candidate 1: {votes_candidate_1}")
print(f"Total votes for Candidate 2: {votes_candidate_2}")
print(f"Total votes for Candidate 3: {votes_candidate_3}")
print(f"Total votes for Candidate 4: {votes_candidate_4}")
print(f"Total null votes: {null_votes}")
print(f"Total blank votes: {blank_votes}")
print(f"Percentage of null votes: {(null_votes / total_votes) * 100:.2f}%")
print(f"Percentage of blank votes: {(blank_votes / total_votes) * 100:.2f}%")
