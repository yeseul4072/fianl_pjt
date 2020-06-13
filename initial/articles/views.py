from django.shortcuts import render, redirect, get_object_or_404
from . import views
from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required

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
        'movie': movie,
    }
    return render(request, 'articles/community.html', context)

@login_required
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('articles:community', movie_pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)


def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.review = review
                comment.user = request.user
                comment.save()
                return redirect('articles:review_detail', movie_pk, review_pk)
        else:
            form = CommentForm()
    context = {
        'movie': movie,
        'review': review,
        'comments': comments,
        # comment 
        'form': form,
    }
    return render(request, 'articles/review_detail.html', context)
