

# Ah I don't like Django at all 🤮 (and really prefer good ol' next.js api routes)
def simulate_random_theater_handler(_request):
    import numpy as np
    from django.http import JsonResponse
    from faker import Faker

    from api.helpers.Movie import Movie
    from api.helpers.Person import Person
    from api.helpers.simulator import main
    from api.helpers.Theater import Theater

    # # Very useful library heavily used in Web Development (my area of expertise with Typescript) to simulate random real data
    fake = Faker()

    # Simulate a populated theater
    theater = Theater(Movie("The Matrix", "Wachowski", 1999, 18), 10)

    spectators = [Person(name=fake.name(),
                         age=fake.random_int(18, 60),
                         available_cash=fake.random_int(100, 1000)) for _ in range(np.random.randint(10, 100))]

    try:
        simulation = main(messages_arr=[], theater=theater,
                          spectators=spectators)

        data = {
            "status": "success" if simulation else "error",
            "data": simulation,
        }

        return JsonResponse(data)

    except Exception as e:
        data = {
            "status": "error",
            "message": str(e)
        }
        return JsonResponse(data)
