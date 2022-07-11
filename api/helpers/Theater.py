import numpy as np
from api.helpers.Movie import Movie


class Theater:
    def __init__(self, current_movie: Movie, ticket_price: float, rows: int = 8, cols: int = 8):
        self.current_movie = current_movie
        self.ticket_price = ticket_price
        self.seats = np.zeros((rows, cols), dtype=bool)

    def get_amount_of_seats(self):
        return self.seats.size

    def get_distribution_of_seats(self):
        return self.seats

    def get_available_seats(self):
        return np.count_nonzero(self.seats == False)
