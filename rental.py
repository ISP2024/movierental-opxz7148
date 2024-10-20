from pricing import *

class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    # The types of movies (price_code). 
    REGULAR = RegularPrice.__new__()
    NEW_RELEASE = NewReleasePrice.__new__()
    CHILDRENS = ChildrenPrice.__new__()
    
    
    def __init__(self, movie, days_rented, price_code): 
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code
     
    def get_price(self):
        return self.price_code.get_price(self.days_rented)
    
    def rental_points(self):
        return self.price_code.get_point(self.days_rented)

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented
    
    def get_price_code(self):
        # get the price code
        return self.price_code

