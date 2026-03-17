from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movie_list, name='movie_list'),
    path('schedule/<int:movie_id>/', views.booking_schedule, name='booking_schedule'),
    path('seats/<int:showtime_id>/', views.booking_status, name='booking_status'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('booked/', views.booked_movies, name='booked_movies'),
]
