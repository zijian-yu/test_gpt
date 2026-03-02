from django.shortcuts import render

from .models import Post


def home(request):
    posts = Post.objects.all()[:10]
    return render(request, 'web/home.html', {'posts': posts})


def about(request):
    return render(request, 'web/about.html')
