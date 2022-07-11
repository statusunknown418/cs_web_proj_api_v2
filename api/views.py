import json

from django.http import HttpRequest
from rest_framework.decorators import api_view


# Ah I don't like Django at all 🤮 (and really prefer good ol' next.js api routes)
@api_view(['GET', 'POST'])
def simulate_random_theater_handler(request: HttpRequest):
    import numpy as np
    from django.http import JsonResponse
    from faker import Faker

    from api.helpers.Movie import Movie
    from api.helpers.Person import Person
    from api.helpers.simulator import main
    from api.helpers.Theater import Theater

    # # Very useful library heavily used in Web Development (my area of expertise with Typescript) to simulate random real data
    fake = Faker()

    body = json.loads(request.body.decode('utf-8')
                      ) if request.body else {"rows": 8,
                                              "columns": 8,
                                              "ticket_price": 50,
                                              "minimum_age": 18,
                                              "simulation_length": 100,
                                              }

    # Simulate a populated theater
    theater = Theater(Movie("The Matrix", "Wachowski", 1999, minimum_age=body['minimum_age']),
                      ticket_price=body['ticket_price'], rows=body['rows'], cols=body['columns'])

    spectators = [Person(name=fake.name(),
                         age=fake.random_int(10, 60),
                         available_cash=fake.random_int(10, 100)) for _ in range(np.random.randint(10, body['simulation_length']))]

    try:
        simulation = main(messages_arr=[], theater=theater,
                          spectators=spectators)

        data = {
            "status": "success" if simulation else "error",
            "data": simulation,
            "body": body
        }

        return JsonResponse(data)

    except Exception as e:
        data = {
            "status": "error",
            "message": str(e)
        }
        return JsonResponse(data)
