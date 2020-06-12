from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
 path('', views.index, name='index'),   
 path('home/', views.home, name='home' ),
 path('community/', views.community, name='community'),
]