'''Write a program that receives a date in DD/MM/YYYY format and displays it with the month in full:
DD/month in full/YYYY'''

# My signature 
print("=+" * 28, "\n", " " * 20, "ALB System", "\n", "=+" * 28, "\n")

def formatDate(date):
    mm = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = date.split("/")
    months = int(month[1])
    print(f"{months}/{mm[months-1]}/{month[2]}")

date = input("Insert a date: (DD/MM/AAAA): ")
formatDate(date)