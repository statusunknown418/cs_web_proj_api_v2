import numpy as np
from api.helpers.Movie import Movie
from api.helpers.Person import Person
from api.helpers.Theater import Theater
from faker import Faker

# Very useful library heavily used in Web Development (my area of expertise with Typescript) to simulate random real data
fake = Faker()

# Simulate a populated theater
theater = Theater(Movie("The Matrix", "Wachowski", 1999, 18), 10)

spectators = [Person(name=fake.name(),
                     age=fake.random_int(18, 60),
                     available_cash=fake.random_int(100, 1000)) for _ in range(np.random.randint(10, 100))]

messages = []


def simulate_spectator_arriving(theater: Theater, spectator: Person):
    if theater.current_movie.minimum_age > spectator.age:
        messages.append(
            f"{spectator.name} is too young to watch {theater.current_movie}")
        return

    if theater.get_available_seats() == 0:
        messages.append(f"{theater.current_movie} is sold out")
        return

    if spectator.available_cash < theater.ticket_price:
        messages.append(
            f"{spectator.name} can't afford {theater.current_movie}")
        return


def simulate_spectator_taking_random_seat(theater: Theater, spectator: Person):
    # Get a random seat
    row = theater.seats.shape[0]
    col = theater.seats.shape[1]
    seat = (fake.random_int(0, row - 1), fake.random_int(0, col - 1))

    # Check if seat is available
    if theater.seats[seat] == True:
        messages.append(
            f"Another spectator is already here ({seat}), looking for another seat")

        simulate_spectator_arriving(theater, spectator)
        return

    theater.seats[seat] = True
    spectator.available_cash -= theater.ticket_price
    messages.append(f"{spectator.name} has bought a seat at {seat}")


def main():
    for spectator in spectators:
        simulate_spectator_arriving(theater, spectator)
        simulate_spectator_taking_random_seat(theater, spectator)

    return {
        "simulation": theater.get_distribution_of_seats().tolist(),
        "log": messages}
