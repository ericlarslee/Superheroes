from django.shortcuts import render
from .models import Superhero
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }
    return render(request, 'superheroes/index.html', context)


def detail(request, superhero_id):
    temp_hero = Superhero.objects.get(pk=superhero_id)
    context = {'superhero': temp_hero}
    return render(request, 'superheroes/detail.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_superpower = request.POST.get('primary_superpower')
        secondary_superpower = request.POST.get('secondary_superpower')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_superhero_ability=primary_superpower, secondary_superhero_ability=secondary_superpower, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def update_superhero(request):
    if request.method == 'POST':
        idn = request.POST.get('id')
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_superpower = request.POST.get('primary_superpower')
        secondary_superpower = request.POST.get('secondary_superpower')
        catchphrase = request.POST.get('catchphrase')
        updated_hero = Superhero(id=idn, name=name, alter_ego=alter_ego, primary_superhero_ability=primary_superpower, secondary_superhero_ability=secondary_superpower, catchphrase=catchphrase)
        updated_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
