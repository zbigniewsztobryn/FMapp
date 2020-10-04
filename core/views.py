from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'home.html', {'var': 'content'})

def count(request):
    fulltext = request.GET['fulltext']
    #print (fulltext)
    return render (request, 'count.html', {'fulltext': fulltext})

def about(request):
    return render(request, 'about.html')