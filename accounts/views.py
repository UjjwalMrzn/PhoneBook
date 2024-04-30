from django.shortcuts import render
from django.http import HttpResponse





# Create your views here.
from .models import *

def home(request):
    return render(request, 'accounts/home.html')

def add(request):
    return render(request, 'accounts/add.html')

def search(request):
    query = request.GET['query']
    per = Person.objects.filter(first_name__icontains=query)
    # per = Person.objects.filter(last_name__icontains=query)
    
    return render(request, 'accounts/search.html' , {'per' : per})
    

def delete(request):
    return HttpResponse('delete')


