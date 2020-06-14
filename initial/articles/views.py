from django.shortcuts import render, redirect, get_object_or_404
from . import views
from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required

# pagination
from django.core.paginator import Paginator

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
    paginator = Paginator(movies, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': movies,
        'page_obj': page_obj,
    }
    return render(request, 'articles/movie_list.html', context)


def last_movie_list(request):
    movies = Movie.objects.order_by('-release_date')
    paginator = Paginator(movies, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': movies,
        'page_obj': page_obj,
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
    form = CommentForm()
    context = {
        'movie': movie,
        'review': review,
        'comments': comments,
        # comment 
        'form': form,
    }
    return render(request, 'articles/review_detail.html', context)


@login_required
def comment_create(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()
        return redirect('articles:review_detail', movie.pk, review.pk)


@login_required
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.user == request.user:
        review.delete()
    return redirect('articles:community', movie_pk)


@login_required
def review_update(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.user == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('articles:review_detail', movie_pk, review_pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('articles:review_detail', movie_pk, review_pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/review_detail.html', context)

@login_required
def comment_delete(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('articles:review_detail', movie_pk, review_pk)

@login_required
def comment_update(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if comment.user == request.user:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('articles:review_detail', movie_pk, review_pk)
        else:
            form = CommentForm(instance=comment)
    else:
        return redirect('articles:review_detail', movie_pk, review_pk)
    context = {
        'form': form,
        'comment': comment,
        'review': review,
    }
    return render(request, 'articles/review_detail.html', context)