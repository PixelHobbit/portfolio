from django.shortcuts import render
from gallerys.models import Gallery
from django.shortcuts import render,get_object_or_404

def home(request):
    gallerys = Gallery.objects
    return render(request, 'home.html',{'gallerys':gallerys})

def gallery_text(request, gallerys_id):
    gallery = get_object_or_404(Gallery, pk=gallerys_id)
    return render(request,'gallery_text.html',{'gallery':gallery})
