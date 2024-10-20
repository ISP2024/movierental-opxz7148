from abc import ABC, abstractmethod

class Price(ABC):
    
    _instance = None

    @classmethod
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Price, cls).__new__(cls)
        return cls._instance
    
    @abstractmethod
    def get_price(self, days: int) -> float:
        pass
    
    def get_point(self, days: int) -> int:
        return 1
    

class RegularPrice(Price):
    
    def get_price(self, days: int) -> float:
        # Two days for $2, additional days 1.50 per day.
        amount = 2.0
        if days > 2:
            amount += 1.5*(days-2)
        return amount
            
            
class ChildrenPrice(Price):

    def get_price(self, days: int) -> float:
        # Three days for $1.50, additional days 1.50 per day.
        amount = 1.5
        if days > 3:
            amount += 1.5*(days-3)
        return amount
            
            
class NewReleasePrice(Price):
    
    def get_price(self, days: int) -> float:
        # Straight $3 per day charge
        return 3*days

    def get_point(self, days: int) -> int:
        # New release movie get 1 point per day
        return days
    