from django.shortcuts import render, HttpResponse, redirect
from django.template import RequestContext

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

def login(request):
    return render(request,'videoapp/account/login.html',{})

def error404(request, exception):
    return render(request, 'videoapp/404.html')
