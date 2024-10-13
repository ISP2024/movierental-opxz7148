from abc import ABC, abstractmethod

class Price(ABC):
    
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
    
class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = RegularPrice()
    NEW_RELEASE = NewReleasePrice()
    CHILDRENS = ChildrenPrice()
    
    def __init__(self, title: str, price: Price):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price
        
    def get_price(self, days):
        return self.price_code.get_price(days)
    
    def get_points(self, days):
        return self.price_code.get_point(days)
        
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title
    
    def get_price_code(self):
        # get the price code
        return self.price_code

