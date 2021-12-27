from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect("/accounts/dashboard")
    if request.method == "POST":
        form_username = request.POST['username']
        form_password = request.POST['password']

        user = authenticate(request, username=form_username, password=form_password)
        if user is not None:
            auth_login(request, user)
            if request.GET.get('next'):
                print("redirect")
                return redirect("/accounts/portal")
                # return redirect(request.GET['next'])
            return redirect("/accounts/dashboard")
        else:
            messages.error(request, "Invalid Credentials")
            return render(request, "accounts/login.html")

    return render(request, "accounts/login.html") 

def register(request):
    if request.user.is_authenticated:
        return redirect("/accounts/dashboard")
    if request.method == "POST":
        form_username = request.POST['username']
        form_email = request.POST['email']
        form_password = request.POST['password']
        form_password2 = request.POST['password2']
        form_fname = request.POST['firstname']
        form_lname = request.POST['lastname']

        if form_password != form_password2:
            messages.error(request, "Both passwords should be same")
            return redirect(register)
        
        if User.objects.get(username=form_username).DoesNotExist:
            messages.error(request, "username already taken")
            return redirect(register)

        user = User.objects.create_user(form_username, form_email, form_password)
        user.first_name = form_fname
        user.last_name = form_lname
        user.save()


        auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect("/accounts/dashboard")

    return render(request, "accounts/register.html")

def dashboard(reuqest):
    return render(reuqest, "accounts/dashboard.html")

def logout(request):
    auth_logout(request)
    return redirect("/accounts/login")


@login_required(login_url="/accounts/login")
def portal(request):
    return render(request, "accounts/portal.html")