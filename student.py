# Add these methods to class student - full_name, year_of_birth, 
# initials. Create two instances and verify the work as expected

class Student:
    school="Akirachix"
    def __init__(self,first_name,last_name,age,country):
        self.first_name = first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        
    def full_name(self):
        fullname=f"{self.first_name} {self.last_name}"
        return fullname
        
    def initials(self):
        initial= f"{self.first_name[0]} {self.last_name[0]}"
        return initial
    
    def year_of_birth(self):
        x=int(input("Enter current year \n"))
        yearofbirth=x-self.age
        return yearofbirth
        
    
    def greet(self):
        return  f"Hello {self.first_name}{self.last_name} you are from {self.country} ,you were born in {self.age} and your initials are {self.last_name[0]}{self.first_name[0]} welcome to {self.school}"















