'''A survey was conducted on the TV channel audience in various houses in a city on a particular day. For each surveyed house, the channel number (4, 5, 7, 12) and the number of people watching that channel were provided. If the television was off, nothing was recorded, meaning that house was not included in the survey. Create a program that:
■ reads an indefinite number of data (channel number and the number of people watching);
■ calculates and shows the percentage of audience for each channel. To end data entry, enter the channel number ZERO.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

counter = 0
counterFour = 0
counterFive = 0
counterSeven = 0
counterTwelve = 0

while True:
    channel = int(input("Which channel do you watch [4/5/7/12]? "))
    if channel == 0:
        break
    amount = int(input("How many people are watching? "))
    counter += 1
    if channel == 4:
        counterFour += amount
    elif channel == 5:
        counterFive += amount
    elif channel == 7:
        counterSeven += amount
    elif channel == 12:
        counterTwelve += amount

print(f"The percentage of people who watch channel 4 is {counterFour/counter:.2%}")
print(f"The percentage of people who watch channel 5 is {counterFive/counter:.2%}")
print(f"The percentage of people who watch channel 7 is {counterSeven/counter:.2%}")
print(f"The percentage of people who watch channel 12 is {counterTwelve/counter:.2%}")
