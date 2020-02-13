from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from . forms import UserForm




def log_out(request):
    logout(request)
    return redirect(('home'))
def log_in(request):

        if request.method=="POST":
            print(request.POST)
            u=request.POST.get("username")
            p=request.POST.get("password")
            user=authenticate(request,username=u,password=p)
           # print("\n" +user +"\n")
            if user is not None:
                if user.is_active :
                    print("yoyo")
                    print( user.is_active) 
                    login(request,user)
                else:
                    messages.info(request, 'your account is under verification')
                
                return redirect("home")
        return render(request,"accounts/login.html")
        

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username=username, password=raw_password,is_active=False)
            messages.info(request, 'your account is under verification')
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    user = get_object_or_404(User, username=request.user)
    return render(request, 'profile.html', {'profile_user': user})

def update(request):
    form=UserForm()
    return render(request,"update.html",{"form":form})