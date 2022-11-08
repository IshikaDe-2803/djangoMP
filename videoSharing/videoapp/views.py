from django.shortcuts import render, HttpResponse, redirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

from .models import NewVideo
from django.http import HttpResponseRedirect
from datetime import date

# Create your views here.
def homepage(request):
    # return HttpResponse('Hello')
    videos=NewVideo.objects.all()
    return render(request,'videoapp/homepage.html',{'videos':videos})

def upload(request):
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        thumbnail=request.FILES['thumbnail']
        video=request.FILES['video']

        videoobj=NewVideo(title=title, description=desc, date=date.today(), thumbnail=thumbnail,video=video)
        videoobj.save()
        return redirect('homepage')
    return render(request,'videoapp/upload.html',{})

def video(request,pk):
    video = NewVideo.objects.get(pk=pk)
    print(video)
    if request.method=="POST":
        print(request.POST)
        return redirect('ViewVideo',pk=pk)
    return render(request,'videoapp/videoView.html',{'video':video})

def login(request):
    return render(request,'videoapp/account/login.html',{})

def error404(request, exception):
    return render(request, 'videoapp/404.html')

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("homepage")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'videoapp/register.html', context)

def login(request):
    if request.method == "POST":
	    form = AuthenticationForm(request, data=request.POST)
	    if form.is_valid():
	    	username = form.cleaned_data.get('username')
	    	password = form.cleaned_data.get('password')
	    	user = authenticate(username=username, password=password)
	    	if user is not None:
	    		auth_login(request, user)
	    		messages.info(request, f"You are now logged in as {username}.")
	    		return redirect("homepage")
	    	else:
	    		messages.error(request,"Invalid username or password.")
	    else:
	    	messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "videoapp/login.html", context)

