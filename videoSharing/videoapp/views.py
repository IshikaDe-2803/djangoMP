from django.shortcuts import render, HttpResponse, redirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q, Max
from .models import NewVideo, User, Comment
from django.http import HttpResponseRedirect
from datetime import date

def homepage(request):
    if request.method =='GET' and 'search_query' in request.GET:
        query = request.GET.get('search_query')
        videos = NewVideo.objects.filter(Q(title__icontains=query))
    else:
        videos = NewVideo.objects.all()
    return render(request, 'videoapp/homepage.html', {'videos':videos})

@login_required
def upload(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        thumbnail = request.FILES['thumbnail']
        video = request.FILES['video']
        videoobj = NewVideo(user=request.user, title=title, description=desc, date=date.today(), thumbnail=thumbnail, video=video)
        videoobj.save()
        return redirect('homepage')
    return render(request, 'videoapp/upload.html', {})

def video(request, videoID):
    video = NewVideo.objects.get(pk=videoID)
    comments = Comment.objects.filter(video=video)
    count = Comment.objects.filter(video=video).count()
    video.visits = video.visits + 1
    if request.method == "POST":
        if 'Addcomment' in request.POST:
            comment_text = request.POST['Addcomment']
            user = User.objects.first()
            comment = Comment.objects.create(
                user = user,
                comment_text = comment_text,
                video = video
            )
        elif 'Like' in request.POST:
            video.likes = video.likes + 1
            video.save()
        elif 'Dislike' in request.POST:
            video.dislikes = video.dislikes + 1
            video.save()
        return redirect('ViewVideo', videoID=videoID)
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'videoapp/videoView.html', {'video':video, 'comments':comments, 'count':count, 'num_visits': num_visits})

def trending(request):
    max_visits = NewVideo.objects.aggregate(Max('visits'))["visits__max"] # Returns the highest number.
    trending= NewVideo.objects.filter(visits=max_visits) 
    return render(request, 'videoapp/trending.html', {'trending':trending})

def login(request):
    return render(request, 'videoapp/account/login.html', {})

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
                return redirect('homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "videoapp/login.html", context)

