from django.shortcuts import render # type: ignore

def base(request):
    return render(request,'base.html')

