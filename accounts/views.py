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
            #print( user.is_active)
            print("\n" +str(user) +"\n")
            
            if user is None:
                messages.info(request, 'your account is under verification  or accont does not exist')
            if user is not None:
                login(request,user)
                    
                
                return redirect("home")
        return render(request,"accounts/login.html")
        

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # user=User.objects.create_user(username=username, password=raw_password,is_active=False)
            # user
            user = authenticate(username=username, password=raw_password,is_active=False)
            user.is_active=False
            user.save()
            messages.info(request, 'your account is under verification')
            
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    user = get_object_or_404(User, username=request.user)
    return render(request, 'profile.html', {'profile_user': user})
@login_required
def update(request):
    form=UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            
            request.user.username = form.cleaned_data.get('username')
            request.user.first_name = form.cleaned_data.get('first_name')
            request.user.last_name = form.cleaned_data.get('last_name')
            request.user.email = form.cleaned_data.get('email')
            request.user.save()
            messages.info(request, 'your account is updated')
            
            return redirect('home')
    else:
        form =UserForm()
    return render(request,"update.html",{"form":form})
    
    