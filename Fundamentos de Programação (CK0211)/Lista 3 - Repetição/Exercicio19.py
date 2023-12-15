'''Create a program that receives the type of action, i.e., a letter to be traded on the stock exchange, the purchase price, and the selling price of each action, and calculates and shows:
■ the profit of each traded action;
■ the number of actions with a profit greater than R$ 1,000.00;
■ the number of actions with a profit less than R$ 200.00;
■ the total profit of the company.
Finish with the action type 'F'.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

counterUp = 0
counterDown = 0
totalProfit = 0

while True:
    share = input("Enter your share: ")
    if share == "F":
        break
    valueBuy = float(input("Enter the purchase amount: "))
    valueSell = float(input("Enter the sale value: "))
    profit = valueSell - valueBuy
    totalProfit += profit
    if profit > 1000:
        counterUp += 1
    if profit < 200:
        counterDown += 1
    print(f"The profit from this action was R${profit:.2f}")

print(f"Number of actions with profit greater than R$ 1,000.00: {counterUp}")
print(f"Number of actions with profit less than R$ 200.00: {counterDown}")
print(f"Total profit of the company: R${totalProfit:.2f}")
