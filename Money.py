def Convert(currency, budget):
    if currency == 1:
       money = budget/21.7
       answer(money)
    elif currency == 2:
        money = budget/6.7
        answer(money)
    elif currency == 3: 
        money = budget/1.3
        answer(money)
    else:
        print("Choose a supported currency")

def answer(money):
    print("You are converting your money into " + str(money) + " dollars")

message = """Choose your currency
1. Peso mexicano
2. Yuan
3. Dolar canadian
"""

currency = int(input(message))
budget = int(input("Type the amount of money you are converting to dollars"))

Convert(currency,budget)

