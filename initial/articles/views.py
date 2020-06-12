from django.shortcuts import render, get_object_or_404
from . import views
from .models import Movie

# Create your views here.
def index(request):
    # articles = Article.objects.all()
    
    context = {
        #'articles'가 html로 넘어가는 거.
        # 'articles': articles,
        
    }
    return render(request, 'articles/index.html', context)


def home(request):
    context = {

    }
    return render(request, 'articles/home.html', context)


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'articles/movie_list.html', context)


def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'articles/movie_detail.html', context)


def community(request, movie_pk):
    # 해당하는 영화에 대한 reviews 들고오기 
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'articles/community.html', context)