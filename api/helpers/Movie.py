class Movie:
    def __init__(self, title, director, duration: int, minimum_age: int):
        self.title = title
        self.director = director
        self.year = int(duration)
        self.minimum_age = minimum_age

    def __str__(self):
        return f"{self.title} ({self.year}) - directed by {self.director} for {self.minimum_age}+"
