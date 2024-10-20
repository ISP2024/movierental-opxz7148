import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2023, ['Scifi', 'Adventure'])
        self.regular_movie = Movie("Air", 2023, ['Documentary', 'Sport'])
        self.childrens_movie = Movie("Frozen", 2014, ['Animation'])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2023, ['Documentary', 'Sport'])
        self.assertEqual("Air(2023)", str(m))

    def test_rental_price(self):

        rental = Rental(self.new_movie, 1, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_price(), 15.0)

        rental = Rental(self.childrens_movie, 3, Rental.CHILDRENS)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 4, Rental.CHILDRENS)
        self.assertEqual(rental.get_price(), 3.0)
        
        rental = Rental(self.regular_movie, 2, Rental.REGULAR)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 4, Rental.REGULAR)
        self.assertEqual(rental.get_price(), 5.0)
        
    def test_rental_points(self):
        
        rental = Rental(self.new_movie, 1, Rental.NEW_RELEASE)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.new_movie, 3, Rental.NEW_RELEASE)
        self.assertEqual(rental.rental_points(), 3)
                
        rental = Rental(self.regular_movie, 1, Rental.REGULAR)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.regular_movie, 3, Rental.REGULAR)
        self.assertEqual(rental.rental_points(), 1)
        
        rental = Rental(self.childrens_movie, 1, Rental.CHILDRENS)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(self.childrens_movie, 3, Rental.CHILDRENS)
        self.assertEqual(rental.rental_points(), 1)