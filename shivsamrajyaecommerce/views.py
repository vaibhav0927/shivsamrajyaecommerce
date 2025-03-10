from django.shortcuts import render # type: ignore

def base(request):
    return render(request,'base.html')

def contactus(request):
    return render(request,'contactus.html')