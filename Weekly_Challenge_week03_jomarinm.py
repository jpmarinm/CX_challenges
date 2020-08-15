import time
from colorama import Fore, Back, Style

print('{:#^50}'.format('Expense Report Calculator'))
month_income = float(input('Enter the amount of monthly income: '))
total_purchases = int(input('Enter the numnber of purchases made in the month: '))
print('')
purchases_count = 1
purchase_items = []
purchase_amounts = []
total_expenses = 0

while purchases_count <=total_purchases:
    item = input(f'Enter name of the purchase number {purchases_count}: ')
    amount = float(input(f'Enter the amount of the purchase number {purchases_count}: '))
    purchase_items.append(item)
    purchase_amounts.append(amount)
    total_expenses+=amount
    purchases_count+=1
#print(purchase_amounts)
#print(purchase_items)
#print(total_expenses)
print('')
print('Creating expense report... plase wait')
for t in range(5):
    print('.',end=' ')
    time.sleep(1)
print('\n')
print('{:#^50}'.format('Expense Report Calculator'))
print('')
for i in range(len(purchase_items)):
    print('{:.<25}{:.>25}'.format(purchase_items[i],purchase_amounts[i]))
    #print(purchase_items[i], end=' ')
    #print(purchase_amounts[i])
print('{:-^50}'.format(''))
restante = month_income - total_expenses
print('{:.<25}{:.>25}'.format('Balance',restante))

if restante<0:
    print(Fore.YELLOW+'WARNING: You have expended more than your income')


