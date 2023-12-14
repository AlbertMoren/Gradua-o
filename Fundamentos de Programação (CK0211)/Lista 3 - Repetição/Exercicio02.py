'''A theater company wishes to stage a series of shows. The management calculates that with a ticket price of $5.00, 120 tickets will be sold, and the expenses will be $200.00. By decreasing the ticket price by $0.50, it is expected that sales will increase by 26 tickets. Create a program that writes a table of expected profits based on the ticket price, varying the price from $5.00 to $1.00 in increments of $0.50. Also, for each new ticket price, write the maximum expected profit, the ticket price, and the quantity of tickets sold to achieve that profit.'''

# My signature
print("=+"*28, "\n", " "*20, "ALB System", "\n", "=+"*28, "\n")

ticket_price = 5.00
tickets_sold = 120.00
expenses = 200.00

for i in range(9):
    earnings = ticket_price * tickets_sold
    profit = earnings - expenses
    print(f"Price  | Tickets | Earnings | Expenses | Profit")
    print(f"${ticket_price:.2f} | {tickets_sold:.2f}   | ${earnings:.2f} | ${expenses:.2f} | ${profit:.2f}")
    ticket_price -= 0.50
    tickets_sold += 26
