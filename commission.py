from abc import ABC, abstractmethod

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