from django.shortcuts import render, redirect
from album.forms import AlbumForm
from album.models import Album
# Create your views here.
def album(request):
    albums = Album.objects.all()
    return render(request, 'album.html', {'albums': albums})

def create_album(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('album')
    return render(request, 'create_album.html', {'form': form})

def edit_album(request, id):
    album = Album.objects.get(pk = id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance = album)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = AlbumForm(instance = album)
    return render(request, 'edit_album.html', {'form': form})

def delete_album(request, id):
    album = Album.objects.get(pk = id).delete()
    return redirect('home')