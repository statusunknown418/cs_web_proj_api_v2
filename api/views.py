from django.http import JsonResponse

from api.helpers.simulator import main


# Ah I don't like Django at all 🤮 (and really prefer good ol' next.js api routes)
def simulate_random_theater_handler(_request):
    try:
        simulation = main()

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
