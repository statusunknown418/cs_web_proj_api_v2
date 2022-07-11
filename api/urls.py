from django.urls import path

from . import views

urlpatterns = [
    path('', views.simulate_random_theater_handler, name='index'),
]
