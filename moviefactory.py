from typing import List
from movie import Movie
import logging

class MovieCatalog:
    
    def __init__(self, filename: str = 'movie.csv') -> None:
        self.file_name = filename
        self.catalog: List[Movie] = []
        self.read_csv()
    
    def read_csv(self):
        
        with open(self.file_name) as movies:
            
            for n, m in enumerate(movies):
                
                # Ignore blank line
                if m == "":
                    continue
                # Ignore comment
                if m[0] == '#':
                    continue
                
                movie_data = m.split(',')
                # Data validation
                if len(movie_data) != 4:
                    logger = logging.getLogger()
                    logger.warning(f'Line {n}: Unrecognized format {m}')
                    continue
                
                # Remove movie ID
                movie_data = movie_data[1:]
                
                # Turn genre to list
                movie_data[-1] = movie_data[-1].split('|')
                
                # Convert year to int
                try: 
                    movie_data[1] = int(movie_data[1])
                except ValueError:
                    logger = logging.getLogger()
                    logger.warning(f'Line {n}: Unrecognized format {m}')
                    continue
                
                self.catalog.append(Movie(*movie_data))
                    
    def get_movie(self, title: str, year: int = None):
        
        year_filter = lambda m, y: m.year == y if y else True
        
        result = filter(
                lambda m: m.title == title and year_filter(m, year), 
                self.catalog
            )
            
        try:
            return next(result)
        except StopIteration:
            return None 
                
                
if __name__ == '__main__':
    m = MovieCatalog()
    print(m.catalog)