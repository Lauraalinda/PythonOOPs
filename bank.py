class Account:
    account_type="Savings"
    def __init__(self,username,pin,accountnumber):
        self.username=username
        self.pin=pin
        self.accountnumber=accountnumber
    
    def account_deposit(self):
        deposit=new_balance-initial_balance
        return deposit
    
    def withdraw(self):
        withdrawal=initial_balance-new_balance
        return withdraw
    
    def greet(self):
        return f"Hello {self.username} your pin is {self.pin} and your account number is {self.accountnumber}"