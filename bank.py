# class Account:
    # account_type="Savings"
    # def __init__(self,username,pin,accountnumber):
        # self.balance=0
        # self.username=username
        # self.pin=pin
        # self.accountnumber=accountnumber
    # 
    # def account_deposit(self,amount):
        # self.balance+=amount
        # return f"You have deposited {self.balance}"
    # 
    # def withdraw(self):
        # withdrawal=initial_balance-new_balance
        # return withdraw
    # 
    # def greet(self):
        # return f"Hello {self.username} your pin is {self.pin} and your account number is {self.accountnumber}"
# 
# 

from curses import curs_set


class Account:
    account_type="Savings"
    def __init__(self,username,accountnumber):
        self.balance=0
        self.username=username
        self.accountnumber=accountnumber
        self.deposits=[]
        self.withdrawals=[]
        
    
    def account_deposit(self,amount):
        if amount<=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance+=amount
            self.deposits.append(amount)
            return f"You have deposited {amount} this is your new balance {self.balance}"
    
    
    def withdraw(self,amount):
        transaction_fee=100
        if amount + transaction_fee > self.balance:
            return f"You have insufficient balance"
        elif amount <=0:
            return f"Withdraw amount should be more than zero"
        else:
            self.balance-=amount
            self.balance-=transaction_fee
            self.withdrawals.append(amount)
            return f"You have withdrawn {amount} this is your new balance {self.balance}"

    
    def deposits_statement(self):
        for x in self.deposit:
            print(f"you have deposited {x}")

    def withdrawals_statement(self):
        for x in self.withdraws:
            print(f"you have withdrawn {x}")
    
    def current_balance(self):
        current_bal=self.balance
        return f"Your current balance is {current_bal}"

    current_balance()


    
    

    
    
           
    
    
    
    
         
  

