from django.shortcuts import render, HttpResponse, redirect
from django.template import RequestContext
from .models import NewVideo
from django.http import HttpResponseRedirect
from datetime import date

def homepage(request):
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
