from django.shortcuts import render
from score.models import Score

def index(request):
    context = {}
    scores = Score.objects.all()
    context['scores'] = scores
    context['title'] = 'Home'
    return render(request, 'index.html', context)

def about(request):
    context = {}
    context['title'] = 'About'
    return render(request, 'about.html', context)
