from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Person





# Create your views here.
from .models import *

def home(request):
    return render(request, 'accounts/home.html')

def add(request):
   
    if request.method == 'POST':
        print(request.POST)
        fname = request.POST['fname']
        lname = request.POST['lname']
        number = request.POST['number']
        address = request.POST['address']
        email = request.POST['email']
        uname = request.POST['uname']
        ntype = request.POST['ntype']
        atype = request.POST['atype']
        etype = request.POST['etype']
        mtype = request.POST['mtype']

        form,created=Phone.objects.get_or_create(Number=number,Number_type=ntype)
        form2,created2=Email.objects.get_or_create(email=email,email_type=etype)
        form3,created2=Address.objects.get_or_create(Address=address,Address_type=atype)
        form4,created2=SocialMedia.objects.get_or_create(User_Name=uname,Linked_App=mtype)

        #  drop down menu 
       

        new_contact = Person(first_name=fname , last_name=lname ,phone=(form ), email=(form2 ) , address=(form3), media = (form4))
        print(new_contact)                     
        new_contact.save()
        
    return render(request, 'accounts/add.html', {})

def search(request):
    query = request.GET['query']
    per2 = Person.objects.filter(first_name__icontains=query)
    per1 = Person.objects.filter(last_name__icontains=query)
    # per3 = Person.objects.filter(phone__Number__contains=query)
    per=per1 or per2 
    # context ={'per' : per} 
    return render(request, 'accounts/search.html' , {'per' : per} )


def all(request):
    per = Person.objects.all()
    # per = Person.objects.filter(last_name__icontains=query)
    
    return render(request, 'accounts/all.html' , {'per' : per})
    

def edit(request):
    return render(request ,'accounts/edit.html')




def delete(request):
        return render(request, 'accounts/delete.html')





# def delete(request):
#     per = Person.objects.delete()
#     return render(request, 'accounts/delete.html')
