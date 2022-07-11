import numpy as np
from api.helpers.Person import Person
from api.helpers.Theater import Theater


def simulate_spectator_arriving(theater: Theater, spectator: Person, messages: list):
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


def simulate_spectator_taking_random_seat(theater: Theater, spectator: Person, messages: list):
    # Get a random seat
    row = theater.seats.shape[0]
    col = theater.seats.shape[1]
    seat = (np.random.randint(0, row - 1), np.random.randint(0, col - 1))

    # Check if seat is available
    if theater.seats[seat] == True:
        messages.append(
            f"Another spectator is already here ({seat}), looking for another seat")

        simulate_spectator_arriving(theater, spectator, messages)
        return

    theater.seats[seat] = True
    spectator.available_cash -= theater.ticket_price
    messages.append(f"{spectator.name} has bought a seat at {seat}")


def main(spectators, theater, messages_arr):
    for person in spectators:
        simulate_spectator_arriving(
            spectator=person, theater=theater, messages=messages_arr)
        simulate_spectator_taking_random_seat(
            theater, person, messages=messages_arr)

    return {
        "simulation": theater.get_distribution_of_seats().tolist(),
        "log": messages_arr}
