"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from abc import ABC, abstractmethod

"""CREATE ABSTRACT EMPLOYEE CLASS   
    WHICH TAKES A NAME AND DEFAULTS EMPLOYEE TO HAVING NO COMMISSION"""

class Employee(ABC):

    def __init__(self, name, commission=None):
        self.name = name
        self.commission = commission
        
     
    def get_pay(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def get_commission_string(self):
        if self.commission != None:
            if self.commission.is_bonus:
                commission_string = f' and receives a bonus commission of {self.commission.get_calc_commission()}'
            else:
                commission_string = f' and receives a commission for {self.commission.get_num_contracts()} contract(s) at {self.commission.get_commission()}/contract'
        else:
            commission_string = ""
        return commission_string

"""CREATE CONCRETE SALARY EMPLOYEE WHICH TAKES IN THEIR MONTHLY SALARY"""

class SalaryContractEmployee(Employee):

    def __init__(self, name, salary, commission = None):
        super().__init__(name, commission)
        self.salary = salary

    def get_pay(self):
       if self.commission != None:
        return self.salary + self.commission.get_calc_commission() 
       else:
           return self.salary
    
    def __str__(self):
        #local variables
        salary = str(self.salary)
        pay = str(self.get_pay())
        commission_string = self.get_commission_string()

        #construct string
        description = f'{self.name} works on a monthly salary of {salary}'
        if commission_string:
            description += commission_string
        description+= f'. Their total pay is {pay}.'

        return description

"""CREATE CONCRETE HOURLY CONTRACT EMPLOYEE
 WHICH TAKES IN THEIR HOURS WORKED AND HOURLY WAGE"""

class HourlyContractEmployee(Employee):

    def __init__(self, name, hours_worked, hourly_wage, commission = None):
        super().__init__(name, commission)
        self.hours_worked = hours_worked
        self.hourly_wage = hourly_wage

    def get_pay(self):
       if self.commission != None:
        return (self.hours_worked * self.hourly_wage) + self.commission.get_calc_commission() 
       else:
        return self.hours_worked * self.hourly_wage

    def __str__(self):
        #local variables 
        hours = self.hours_worked
        hourly_wage = self.hourly_wage
        pay = str(self.get_pay())
        commission_string = self.get_commission_string()

        #construct string
        description = f'{self.name} works on a contract of {hours} hours at {hourly_wage}/hour'
        if commission_string:
            description += commission_string
        description+= f'. Their total pay is {pay}.'

        return description
    
"""CREATE ABSTRACT COMMISSION CLASS TO PASS THROUGH
EMPLOYEE OBJECT WHICH TAKES IN AT MINIMUM A COMMISSION AMOUNT-
PROVIDING DEFAULTS"""

class Commission(ABC):

    def __init__(self, commission, num_contracts = 0, is_bonus = False):
        self.commission = commission
        self.num_contracts = num_contracts
        self.is_bonus = is_bonus

    @abstractmethod
    def get_calc_commission(self):
        pass
    
"""CREATE CONCRETE BONUS COMMISSION CLASS - UPDATES IS_BONUS BOOL TO TRUE"""

class BonusCommission(Commission):

    def __init__(self, commission, num_contracts = 0, is_bonus = True):
        super().__init__(commission, num_contracts, is_bonus)
    
    def get_calc_commission(self):
        return self.commission
    
"""CREATE CONCRETE CONTRACT COMMISSION CLASS"""
    
class ContractCommission(Commission):

    def __init__(self, commission, num_contracts, is_bonus = False):
        super().__init__(commission, num_contracts, is_bonus)
        
    def get_calc_commission(self):
        return self.commission * self.num_contracts    

    def get_num_contracts(self):
        return self.num_contracts

    def get_commission(self):
        return self.commission   

"""END OF CLASSES"""

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryContractEmployee('Billie', 4000)
#print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyContractEmployee('Charlie', 100, 25)
#print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryContractEmployee('Renee', 3000, ContractCommission(200, 4))
#print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyContractEmployee('Jan', 150, 25, ContractCommission(220, 3))
#print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryContractEmployee('Robbie', 2000, BonusCommission(1500))
#print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyContractEmployee('Ariel', 120, 30, BonusCommission(600))
#print(str(ariel))