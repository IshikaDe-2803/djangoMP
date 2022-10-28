from django.shortcuts import render, HttpResponse
from django.template import RequestContext

# Create your views here.
def homepage(request):
    # return HttpResponse('Hello')
    return render(request,'videoapp/homepage.html')

def upload(request):
    return render(request,'videoapp/upload.html',{})

def login(request):
    return render(request,'videoapp/account/login.html',{})

def error404(request, exception):
    return render(request, 'videoapp/404.html')
