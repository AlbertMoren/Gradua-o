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
    candidate