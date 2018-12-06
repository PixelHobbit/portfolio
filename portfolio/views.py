from django.shortcuts import render
from gallerys.models import Gallery

def home(request):
    gallerys = Gallery.objects
    return render(request, 'home.html',{'gallerys':gallerys})
