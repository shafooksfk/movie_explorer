from django.db import models

# Create your models here.

class Rating(models.Model):
    source = models.CharField(max_length=40)
    rating = models.CharField(max_length=5)
    
    def __str__(self):
        return self.source
    
class Movie(models.Model):
    Title = models.CharField(max_length=200)
    Year = models.CharField(max_length=25,blank=True)
    Rated = models.CharField(max_length=10,blank=True)
    Released = models.CharField(max_length=25,blank=True)
    Runtime = models.CharField(max_length=25,blank=True)
    Genre = models.CharField(max_length=200,blank=True)
    Director = models.CharField(max_length=100,blank=True)
    Writer = models.CharField(max_length=300,blank=True)
    Actors = models.CharField(max_length=300,blank=True)
    Plot = models.CharField(max_length=1000,blank=True)
    Language = models.CharField(max_length=200,blank=True)
    Country = models.CharField(max_length=300,blank=True)
    Awards = models.CharField(max_length=300,blank=True)
    Poster = models.ImageField(upload_to='movies',blank=True)
    Poster_url = models.URLField(blank=True)
    Ratings = models.ManyToManyField(Rating,blank=True)
    Metascore = models.CharField(max_length=5,blank=True)
    imdbRating = models.CharField(max_length=5,blank=True)
    imdbVotes = models.CharField(max_length=100,blank=True)
    imdbID = models.CharField(max_length=100,blank=True)
    Type = models.CharField(max_length=20,blank=True)
    BoxOffice = models.CharField(max_length=25,blank=True)
    
    def __str__(self):
        return self.Title 
    
    
    # def save(self, *args, **kwargs):
        