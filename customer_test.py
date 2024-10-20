import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie
from pricing import *


class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:
    
        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", 2020, ['Live action'])
        self.regular_movie = Movie("CitizenFour", 2014, [])
        self.childrens_movie = Movie("Frozen", 2014, ['Animation'])
        
    @unittest.skip("No convenient way to test")
    def test_billing():
        # no convenient way to test billing since its buried in the statement() method.
        pass
    
    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4, Rental.NEW_RELEASE)) # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
        
    def test_total_charge(self):
        
        r1 = Rental(self.regular_movie, 3, Rental.REGULAR)
        r2 = Rental(self.new_movie, 4, Rental.NEW_RELEASE)
        r3 = Rental(self.childrens_movie, 2, Rental.CHILDRENS)

        self.c.add_rental(r1)
        self.c.add_rental(r2)
        self.c.add_rental(r3)
        
        self.assertEqual(self.c.get_total_price(), sum([r1.get_price(), r2.get_price(), r3.get_price()]))
        
    def test_total_points(self):
        
        r1 = Rental(self.regular_movie, 3, Rental.REGULAR)
        r2 = Rental(self.new_movie, 4, Rental.NEW_RELEASE)
        r3 = Rental(self.childrens_movie, 2, Rental.CHILDRENS)

        self.c.add_rental(r1)
        self.c.add_rental(r2)
        self.c.add_rental(r3)
        
        self.assertEqual(self.c.get_total_points(), sum([r1.rental_points(), r2.rental_points(), r3.rental_points()]))

