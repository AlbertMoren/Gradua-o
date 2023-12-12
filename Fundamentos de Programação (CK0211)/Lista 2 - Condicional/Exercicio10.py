'''The consumer price of a new car is the sum of the factory cost with the distributor and taxes percentages, both applied to the factory cost. The percentages are in the following table. Create a program that receives the factory cost of a car and displays the consumer price.
FACTORY COST (R$)  DISTRIBUTOR (%) TAXES (%)
Up to R$12,000.00       5               Exempt
Between R$12,000.00 and R$25,000.00    10              15
Above R$25,000.00       15              20
'''

# My signature 
print("=+"*28,"\n"," "*20, "ALB System","\n","=+"*28,"\n")

# Receive the factory cost
factory_cost = float(input("Enter the car's factory cost: R$"))

# Check the factory cost range and calculate the consumer price accordingly
if factory_cost <= 12000:
    consumer_price = factory_cost + (factory_cost * 0.05)
elif 12000 < factory_cost <= 25000:
    consumer_price = factory_cost + (factory_cost * 0.1) + (factory_cost * 0.15)
else:
    consumer_price = factory_cost + (factory_cost * 0.15) + (factory_cost * 0.2)

# Display the result
print(f"The consumer price of the car is R${consumer_price:.2f}")
