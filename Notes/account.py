import random
from abc import *

class Account(ABC):
    def __init__(self,account_holder):
        self.name=account_holder
        self.balance=0
        self.__id= self.__createID()

    @abstractmethod
    def greeting(self):
        raise NotImplementedError

    def setID(self,new_id):
        self.__id=new_id
    
    @property
    def getID(self):
        return self.__id

    def __createID(self):
        return random.randint(100,900)


    def __str__(self):
        return 'Account Balance: ${}'.format(self.balance)

    def __repr__(self):
        return '${}'.format(self.balance)
        
    def deposit(self, amount):
        if isinstance(amount,int) or isinstance(amount,float):
            self.balance+=amount
            return self.balance
        elif isinstance(amount,Check):
            if amount.cashed:
                return 'Invalid check'
            elif amount.pay_to==self.name and amount.check_amount>0:
                self.balance+=amount.check_amount
                amount.check_amount=0
                amount.cashed=True
                return self.balance
            else:
                return 'Invalid operation'
        else:
            return 'Invalid operation'

    def withdraw(self,amount):
        if self.balance<amount:
            return 'Insufficient funds'

        self.balance-=amount
        return self.balance

class CheckingAccount(Account):

    withdraw_fee=1
    interest=0.01

    def __init__(self, name,amount=0):
        super().__init__(name)
        self.balance=amount
        print(self.greeting())
    def greeting(self):
        return 'Welcome to your checking account'

    def withdraw(self,amount):
        return Account.withdraw(self,amount+CheckingAccount.withdraw_fee)

class SavingsAccount(Account):

    __INTEREST=0.03
    __MIN_BALANCE=500
    __DEPOSIT_FEE=1
    __WITHDRAW_FEE=2
    __GIFT=10
    __OPEN_WITH=1000

    def __new__(cls,name,amount):
        if amount<SavingsAccount.__OPEN_WITH:
            raise ValueError('You need ${} to open account'.format(SavingsAccount.__OPEN_WITH))
        obj=super(SavingsAccount,cls).__new__(cls)
        return obj

    def __init__(self, name, amount):
        super().__init__(name)
        self.first_time=True
        self.balance=amount+SavingsAccount.__GIFT

    def deposit(self, amount):
        return Account.deposit(self,amount-SavingsAccount.__DEPOSIT_FEE)

    def withdraw(self,amount):
        if self.balance-(amount+SavingsAccount.__WITHDRAW_FEE)<SavingsAccount.__MIN_BALANCE:
            return "Invalid operation"
        return Account.withdraw(self, amount+SavingsAccount.__WITHDRAW_FEE)


class Check:

    def __init__(self, pay_to, amount):
        self.pay_to=pay_to
        self.check_amount=amount
        self.cashed=False

class Bank:
    def __init(self):
        self.accounts=[]

    def openAccount(self, name, amount=0, account_type=CheckingAccount):
        customer = account_type(name, amount)
        self.accounts.append(customer)
        return customer

    def payInterest(self):
        for customers in self.accounts:
            if isinstance(customers, CheckingAccount):
                customers.deposit(customers.balance*customers._CheckingAccount__INTEREST)
            elif isinstance(customers, SavingsAccount):
                customers.deposit(customers.balance*customers._SavingsAccount__INTEREST)


