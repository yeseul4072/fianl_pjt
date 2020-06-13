from django.core.validators import validate_comma_separated_integer_list
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class Genre(models.Model):
    genre = models.IntegerField()


# Create your models here.
class Movie(models.Model):
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    poster_path = models.CharField(max_length=200)
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=200)
    original_language = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    vote_average = models.FloatField()
    overview = models.TextField()
    release_date = models.DateField()
    color = models.CharField(validators=[validate_comma_separated_integer_list], max_length=30, blank=True, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    

class Review(models.Model):
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)