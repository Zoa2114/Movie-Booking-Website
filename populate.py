from datetime import date, time, timedelta
from movies.models import Movie, Showtime, Seat

# Add Movies
m1 = Movie.objects.create(
    title="Inception",
    description="A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
    duration_minutes=148,
    poster_url="https://images.unsplash.com/photo-1626814026160-2237a95fc5a0?q=80&w=2070&auto=format&fit=crop",
    release_date=date(2010, 7, 16)
)

m2 = Movie.objects.create(
    title="The Dark Knight",
    description="When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
    duration_minutes=152,
    poster_url="https://images.unsplash.com/photo-1531259683007-016a7b628fc3?q=80&w=2146&auto=format&fit=crop",
    release_date=date(2008, 7, 18)
)

m3 = Movie.objects.create(
    title="Interstellar",
    description="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
    duration_minutes=169,
    poster_url="https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072&auto=format&fit=crop",
    release_date=date(2014, 11, 7)
)

m4 = Movie.objects.create(
    title="Avatar",
    description="A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
    duration_minutes=162,
    poster_url="https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1980&auto=format&fit=crop",
    release_date=date(2009, 12, 18)
)

# Add Showtimes and Seats
today = date.today()
tomorrow = today + timedelta(days=1)

movies = [m1, m2, m3, m4]
times = [time(10, 0), time(14, 0), time(18, 0), time(21, 30)]

seat_rows = ['A', 'B', 'C', 'D', 'E']

for m in movies:
    for d in [today, tomorrow]:
        for t in times:
            st = Showtime.objects.create(movie=m, date=d, time=t, price=12.50)
            
            # create seats
            for row in seat_rows:
                for num in range(1, 11): # 10 seats per row -> 50 seats total
                    Seat.objects.create(showtime=st, seat_number=f"{row}{num}")
                    
print("Database successfully populated with movies, showtimes and seats!")
