from curses import curs_set
from datetime import datetime
class Account:
    account_type="Savings"
    def __init__(self,username,accountnumber):
        self.balance=0
        self.username=username
        self.accountnumber=accountnumber
        self.deposits=[]
        self.withdrawals=[]
        self.date=datetime.now()
        self.loan_balance=0
      
    
    def account_deposit(self,amount):
        if amount<=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance+=amount
            self.deposits.append({"date":self.date.strftime("%c"),
                                  "amount":amount,
                                  "naration":"deposit"
                                  })
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
            self.withdrawals.append({"date":self.date.strftime("%c"),                       
                                     "amount":amount,
                                     "narration":"withdraw"
                                     })
            return f"You have withdrawn {amount} this is your new balance {self.balance}"

    
    def deposits_statement(self):
        for x in self.deposits:
            print(f"you have deposited {x}")

    def withdrawals_statement(self):
        for x in self.withdraws:
            print(f"you have withdrawn {x}")
    
    def current_balance(self):
        current_bal=self.balance
        return f"Your current balance is {current_bal}"

    def full_statement(self):
        statements=self.withdrawals+self.deposits
        for statement in statements:
          print(statement)


    def borrow(self,amount):
        sum=0
        for i in self.deposits:
            sum+=i["amount"]
        if (len(self.deposits)) < 10:
            return f"Hello {self.username}.You cannot borrow {amount} you have less than ten deposits"
        elif amount<100:
            return f"Hello {self.username}.You cannot borrow less than 100"
        elif amount > sum//3:
            return f"Hello {self.username}.You have exceeded your loan limit"
        elif self.balance==0:
            return f"Hello {self.username}.You have an insufficient balance qualify for this loan"
        elif self.loan_balance>0:
            return f"Hello {self.username}.You have an outstanding loan of {self.loan_balance}"
        else:
            self.loan_balance+=(amount+(amount*0.03))
            return f"Hello {self.username}.You have borrowed {amount} with an interest of {amount*0.03} so your total loan amount is {self.loan_balance}"
        
    def loan_repayment(self,amount):
        if amount < 0:
            return f"Repayment amount must be more than zero"
        elif amount <=self.loan_balance:
            self.loan_balance-=amount
            return f"Your loan balance is {self.loan_balance}"
        elif amount > self.loan_balance:
            self.balance+=(amount-self.loan_balance)

    
    def transfer(self,receiver,amount):
        self.receiver=receiver
        self.amount=amount
        current_balance=self.balance-amount
        if amount<=0:
            return f"You cannot transfer a non-existant amount"
        elif amount>self.balance:
            return f"Your cannot transfer {amount}.Your current balance is {self.balance}"
        elif amount<self.balance:
            return f"You have transfered {amount} to {self.receiver} your current balance is {current_balance}"

        
        
        
        
       
       
       
       
       
       
       
       
       
       
    
       
    
       
       
       
       
       


    
    

    
    
           
    
    
    
    
         
  

