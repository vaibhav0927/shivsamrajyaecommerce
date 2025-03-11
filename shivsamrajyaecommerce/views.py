from django.shortcuts import render # type: ignore


def base(request):
    return render(request,'base.html')
def contactus(request):
    return render(request,'contactus.html')

def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,'home.html')

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')


