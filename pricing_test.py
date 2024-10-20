from re import S
from unittest import TestCase
from movie import Movie
from rental import Rental

class PricingTest(TestCase):
    
    def setUp(self):
        self.new_movie = Movie("Mulan", 2024, ['Live action'])
        self.regular_movie = Movie("CitizenFour", 2014, ['Documentary'])
        self.childrens_movie = Movie("Frozen", 2014, ['Animation', 'Children'])
        self.new_children_movie = Movie("Movie", 2024, ['Children'])
        
    
    def test_regular_movie(self):
        
        r = Rental(self.regular_movie, 1)
        self.assertEqual(id(r.price_code), id(Rental.REGULAR))
        
    def test_new_movie(self):
        
        r = Rental(self.new_movie, 1)
        self.assertEqual(id(r.price_code), id(Rental.NEW_RELEASE))
        
    def test_children_movie(self):
        
        r = Rental(self.childrens_movie, 1)
        self.assertEqual(id(r.price_code), id(Rental.CHILDRENS))
        
    def test_new_children_movie(self):
        
        r = Rental(self.new_children_movie, 1)
        self.assertEqual(id(r.price_code), id(Rental.NEW_RELEASE))
        
        
        