money_amount = 1000  # euro
interest = 5  # percent
years = 5  # depositing time
money_prime = money_amount * (1 + interest / 100) ** years
print(money_prime)
