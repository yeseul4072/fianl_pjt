from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
 path('', views.index, name='index'),   
 path('home/', views.home, name='home' ),
 path('movie_list/', views.movie_list, name='movie_list'),
 path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
 path('<int:movie_pk>/community', views.community, name='community'),
 path('<int:movie_pk>/review_create', views.review_create, name='review_create'),
 path('<int:movie_pk>/<int:review_pk>/review_detail', views.review_detail, name='review_detail'),

]