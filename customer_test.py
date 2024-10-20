import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie
from pricing import *
from moviefactory import MovieCatalog


class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:
    
        c = a customer
        movies = list of some movies
        """
        
        catalog = MovieCatalog()
        
        self.c = Customer("Movie Mogul")
        self.new_movie = catalog.get_movie("Dune: Part Two")
        self.regular_movie = catalog.get_movie("Everything Everywhere All at Once")
        self.childrens_movie = catalog.get_movie("Mulan")
        
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
        self.c.add_rental(Rental(self.new_movie, 4)) # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
        
    def test_total_charge(self):
        
        r1 = Rental(self.regular_movie, 3)
        r2 = Rental(self.new_movie, 4)
        r3 = Rental(self.childrens_movie, 2)

        self.c.add_rental(r1)
        self.c.add_rental(r2)
        self.c.add_rental(r3)
        
        self.assertEqual(self.c.get_total_price(), sum([r1.get_price(), r2.get_price(), r3.get_price()]))
        
    def test_total_points(self):
        
        r1 = Rental(self.regular_movie, 3)
        r2 = Rental(self.new_movie, 4)
        r3 = Rental(self.childrens_movie, 2)

        self.c.add_rental(r1)
        self.c.add_rental(r2)
        self.c.add_rental(r3)
        
        self.assertEqual(self.c.get_total_points(), sum([r1.rental_points(), r2.rental_points(), r3.rental_points()]))

