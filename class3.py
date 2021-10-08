import sys
class Customer:
    '''customer bank class operation'''
    Bankname='Bhavanibank'
def __init__(self,name,balance=0.0):
    self.name=name
    self.balance=balance
def deposit(self,amount):
    self.balance=self.balance + amount
def withdraw(self,amount):
    if amount>self.balance:
        print('insufficent balance')
        sys.exit(0)
    self.balance=self.balance-amount
    print('after withdra balance is:',self.balance)
print('welcome to:',Customer.Bankname)
name=input('Enter your Name:')
c=Customer(name)
while True:
    print('d-Deposit \n w-Withdraw  \n e-Exit' )
    option=input('Choose your option').lower()
    if option=='d':
        amount=float(input('Enter amount to deposit:'))
        Customer.deposit(amount)
    elif option=='w':
        amount=float(input('Enter amount to deposit:'))
        Customer.withdraw(amount)
    elif option=='e':
        sys.exit()
    else:
        print('invalid option please choose correct option')




