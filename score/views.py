from django.shortcuts import render
from score.models import Score
from score.forms import ScoreForm

def index(request):
    context = {}
    form = ScoreForm()
    scores = Score.objects.all()
    context['scores'] = scores
    context['title'] = 'Home'
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = ScoreForm(request.POST)
            else:
                score = Score.objects.get(id=pk)
                form = ScoreForm(request.POST, instance=score)
            form.save()
            form = ScoreForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            score = Score.objects.get(id=pk)
            score.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            score = Score.objects.get(id=pk)
            form = ScoreForm(instance=score)
    context['form'] = form
    return render(request, 'index.html', context)

def about(request):
    context = {}
    context['title'] = 'About'
    return render(request, 'about.html', context)
