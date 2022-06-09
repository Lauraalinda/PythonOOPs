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

class Account:
    account_type="Savings"
    def __init__(self,username,accountnumber):
        self.balance=0
        self.username=username
        self.accountnumber=accountnumber
        self.deposit=[]
        self.withdraws=[]
        
    
    def account_deposit(self,amount):
        if amount<=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance+=amount
            self.deposit.append(amount)
            return f"You have deposited {amount} this is your new balance {self.balance} and {self.deposit}"
    
    
    def withdraw(self,amount):
        if amount > self.balance:
            return f"Your balance insufficient balance"
        elif amount<=0:
            return f"Withdraw amount should be more than zero"
        else:
            self.balance-=amount
            self.withdraws.append(amount)
            return f"You have withdrawn {amount} this is your new balance {self.balance}"


    def deposits_statement(self):
        for x in self.deposit:
            print(f"you have deposited {x}")

    
    

    
    
           
    
    
    
    
         
  

