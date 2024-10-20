from gettext import Catalog
from re import S
import unittest
from customer import Customer
from rental import Rental
from movie import Movie
from moviefactory import MovieCatalog


class RentalTest(unittest.TestCase):

    def setUp(self):
        
        self.catalog = MovieCatalog()
        self.new_movie = self.catalog.get_movie("Civil War")
        self.regular_movie = self.catalog.get_movie("Arrival")
        self.childrens_movie = self.catalog.get_movie("Weathering With You")

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        self.assertEqual("Arrival(2016)", str(self.regular_movie))

    def test_rental_price(self):

        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        rental = Rental(self.childrens_movie, 3)
        print(rental.movie.genre)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_price(), 3.0)
        
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 4)
        self.assertEqual(rental.get_price(), 5.0)
        
    def test_rental_points(self):
        
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.new_movie, 3)
        self.assertEqual(rental.rental_points(), 3)
                
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.rental_points(), 1)
        
        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.rental_points(), 1)