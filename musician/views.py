from django.shortcuts import render, redirect
from musician.forms import MusicianForm

from musician.models import Musician
# Create your views here.
def musician(request):
    form = Musician.objects.all()
    return render(request,'musician.html', {'form': form})

def create_musician(request):
    form = MusicianForm()
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('musician')
    return render(request, 'create_musician.html', {'form': form})

def edit_musician(request, id):
    musician = Musician.objects.get(pk = id)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        form.save()
        redirect('home')
    form = MusicianForm(instance=musician)
    return render(request, 'edit_musician.html', {'form': form, 'musician_id': musician.id})

def delete_musician(request, id):
    musician = Musician.objects.get(pk = id).delete()
    return redirect('home')
        