from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpRequest
from django.contrib import messages
def log_in(request):
   if request.user.is_authenticated:
        return redirect('home')
   else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or password is incorrect")
        return render(request, 'login.html')        
def log_out(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')

