from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Movie, Showtime, Seat, Booking

def home(request):
    featured_movies = Movie.objects.all()[:4] # show top 4
    return render(request, 'home.html', {'movies': featured_movies})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def booking_schedule(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    showtimes = movie.showtimes.all().order_by('date', 'time')
    return render(request, 'booking_schedule.html', {'movie': movie, 'showtimes': showtimes})

def booking_status(request, showtime_id):
    showtime = get_object_or_404(Showtime, id=showtime_id)
    seats = showtime.seats.all().order_by('seat_number')

    if request.method == 'POST':
        selected_seats = request.POST.getlist('seats')
        user_name = request.POST.get('user_name')

        if not selected_seats:
            messages.error(request, 'Please select at least one seat.')
            return redirect('booking_status', showtime_id=showtime_id)
        
        if not user_name:
            messages.error(request, 'Please provide your name.')
            return redirect('booking_status', showtime_id=showtime_id)

        # check if all selected are available
        seats_to_book = Seat.objects.filter(id__in=selected_seats, showtime=showtime, is_booked=False)
        if seats_to_book.count() != len(selected_seats):
            messages.error(request, 'Some seats were already booked. Please choose other seats.')
            return redirect('booking_status', showtime_id=showtime_id)
        
        # update seats
        for seat in seats_to_book:
            seat.is_booked = True
            seat.save()

        # create booking
        booking = Booking.objects.create(showtime=showtime, user_name=user_name)
        booking.seats_booked.set(seats_to_book)
        booking.save()

        messages.success(request, 'Booking successful!')
        return redirect('booking_confirmation', booking_id=booking.id)

    return render(request, 'booking_status.html', {'showtime': showtime, 'seats': seats})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_confirmation.html', {'booking': booking})

def booked_movies(request):
    bookings = Booking.objects.all().order_by('-booking_time')
    return render(request, 'booked_movies.html', {'bookings': bookings})
