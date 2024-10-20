from pricing import *

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

