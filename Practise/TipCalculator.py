# This program will calculate the tip amount of 20%
# on the original amount.

Amount = input('Enter your amount')
print('Your amount is: ' + Amount)

Tip = 20 / 100

Total_amount = float(Amount) * Tip

Total = Total_amount + float(Amount)

print('Your total amount is: ' + str(Total))

