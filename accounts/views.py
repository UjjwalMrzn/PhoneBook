from django.shortcuts import render
from django.http import HttpResponse
from .models import Person





# Create your views here.
from .models import *

def home(request):
    return render(request, 'accounts/home.html')

def add(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        number = request.POST['number']
        address = request.POST['address']
        email = request.POST['email']
        uname = request.POST['uname']
        # media = request.Post['media']

        form,created=Phone.objects.get_or_create(Number=number)
        form2,created2=Email.objects.get_or_create(email=email)
        form3,created2=Address.objects.get_or_create(Address=address)
        form4,created2=SocialMedia.objects.get_or_create(User_Name=uname)

        new_contact = Person(first_name=fname , last_name=lname ,phone=form, email=form2 , address=form3 , media = form4 )
        new_contact.save()
        
    return render(request, 'accounts/add.html', {})

def search(request):
    query = request.GET['query']
    per = Person.objects.filter(first_name__icontains=query)
    # per = Person.objects.filter(last_name__icontains=query)
    
    return render(request, 'accounts/search.html' , {'per' : per})
    

def delete(request):
    return HttpResponse('delete')


# , phone=number , 
#                              address=address , email=emai