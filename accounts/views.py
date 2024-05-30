from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Person

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


# Create your views here.
from .models import *
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only

def navbar(request):
    return render(request, 'accounts/navbar.html')
def about(request):
    return render(request, 'accounts/aboutus.html')
def contact(request):
    return render(request, 'accounts/contactus.html')


def front(request):
    return render(request , 'accounts/front.html')

@login_required(login_url='login')
@admin_only
def home(request):
    return render(request, 'accounts/home.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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

 
@login_required(login_url='login')
def search(request):
    query = request.GET['query']
    per2 = Person.objects.filter(first_name__icontains=query)
    per1 = Person.objects.filter(last_name__icontains=query)
    per3 = Person.objects.filter(phone__Number__contains=query)
    per4 = Person.objects.filter(address__Address__contains=query)
    per5 = Person.objects.filter(email__email__contains=query)
    per6 = Person.objects.filter(media__User_Name__contains=query)
    per=per1 or per2 or per3 or per4 or per5 or per6
    # context ={'per' : per} 
    return render(request, 'accounts/search.html' , {'per' : per} )



@login_required(login_url='login')
def all(request):
    per = Person.objects.all()
    # per = Person.objects.filter(last_name__icontains=query)
    
    return render(request, 'accounts/all.html' , {'per' : per})
    


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def edit(request,pk):

    detail=Person.objects.get(id=pk)
 
    if request.method=='POST':
        
        detail.first_name=request.POST.get("fname")
        detail.last_name=request.POST.get("lname")
        detail.phone.Number=request.POST.get("number")
        detail.phone.Number_type=request.POST.get("ntype")
        detail.address.Address=request.POST.get("address")
        detail.address.Address_type=request.POST.get("atype")
        detail.email.email=request.POST.get("email")
        detail.email.email_type=request.POST.get("etype")
        detail.media.User_Name=request.POST.get("uname")
        detail.media.Linked_App=request.POST.get("mtype")
    
        detail.save()
        detail.phone.save()
        detail.address.save()
        detail.email.save()
        detail.media.save()
        return redirect('/all')


    return render(request,'accounts/edit.html',{'detail': detail})


    # return render(request ,'accounts/edit.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def delete(request,pk):
    detail=Person.objects.get(id=pk)
    if request.method=='POST':
        detail.delete()
        return redirect('/all')
    return render (request,'accounts/delete.html',{'detail':detail})
       
       
       
        # details=Person.objects.get(id=pk)
        
        # return render(request, 'accounts/delete.html' ,{'details':details})





# def delete(request):
#     per = Person.objects.delete()
#     return render(request, 'accounts/delete.html')



# user log in and registration

@unauthenticated_user
def register(request):

        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='users')
                user.groups.add(group)
                messages.success(request, 'An account was created for ' + username)

                return redirect('login')

        context = {'form':form}
        return render(request , 'accounts/register.html' , context)


@unauthenticated_user
def loginpage(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request , username=username , password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, '"Username or Password is incorrect"')

        context = {}
        return render(request, 'accounts/loginpage.html' , context)


def logoutuser(request):
    logout(request)
    return redirect('login') 



# UserPage
@login_required(login_url='login')

def user(request):
    return render(request, 'accounts/user.html')