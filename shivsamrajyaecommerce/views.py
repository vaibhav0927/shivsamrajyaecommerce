from django.shortcuts import render # type: ignore

def base(request):
    return render(request,'base.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')