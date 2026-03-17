from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration_minutes = models.IntegerField()
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)

    def __str__(self):
        return f"{self.movie.title} - {self.date} {self.time}"

class Seat(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10) # e.g. A1, A2, B1
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('showtime', 'seat_number')

    def __str__(self):
        return f"{self.showtime} - Seat {self.seat_number} - {'Booked' if self.is_booked else 'Available'}"

class Booking(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seats_booked = models.ManyToManyField(Seat)
    user_name = models.CharField(max_length=100)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user_name} for {self.showtime}"
