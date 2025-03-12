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
def general(request):
    return render(request,'general.html')

def Spices(request):
    return render(request,'Spices.html')

def cosmetic(request):
    return render(request,'cosmetic.html')

def fooditems(request):
    return render(request,'fooditems.html')
    


