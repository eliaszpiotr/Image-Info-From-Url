import json

from django.shortcuts import render, redirect
from .models import Image
from .scripts import get_image_size, save_image, dominantcolor


# Create your views here.

def list(request):
    if request.method == 'GET':
        images = Image.objects.all()
        return render(request, 'app/list.html', {'images': images})


def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        albumId = request.POST.get('albumId')
        url = request.POST.get('url')
        image = Image.objects.create(title=title, albumId=albumId, url=url)
        return redirect('list')
    return render(request, 'app/add.html')


def detail(request, id):
    if request.method == 'GET':
        image = Image.objects.get(id=id)
        url = image.url + '.jpg'
        id = image.id
        albumId = image.albumId
        title = image.title
        width, height = get_image_size(url)
        save_image(url, id)
        color = dominantcolor(id)
        context = {
            'id': id,
            'albumId': albumId,
            'title': title,
            'width': width,
            'height': height,
            'dominantColorHex': color,
            'url': url,
            'image': f'images/img{id}.jpg'
        }
        return render(request, 'app/detail.html', context)


def delete(request, id):
    if request.method == 'GET':
        image = Image.objects.get(id=id)
        image.delete()
        return redirect('list')


def edit(request, id):
    if request.method == 'GET':
        image = Image.objects.get(id=id)
        return render(request, 'app/edit.html', {'image': image})

    if request.method == 'POST':
        title = request.POST.get('title')
        albumId = request.POST.get('albumId')
        url = request.POST.get('url')
        image = Image.objects.get(id=id)
        image.title = title
        image.albumId = albumId
        image.url = url
        image.save()
        return redirect('list')
