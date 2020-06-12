from django.shortcuts import render
from . import views

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


def community(request):
    return render(request, 'articles/community.html')