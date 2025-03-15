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

def grocery(request):
    return render(request,'grocery.html')

def Spices(request):
    return render(request,'Spices.html')

def cosmetic(request):
    return render(request,'cosmetic.html')

def fooditems(request):
    return render(request,'fooditems.html')

def shop(request):
    return render(request,'shop.html')

def stationary(request):
    return render(request,'stationary.html')

def submit(request):
    if request.method == "POST":

     fullNameEng = request.POST.get('fullNameEng')
     fullNameMarathi = request.POST.get('fullNameMarathi')
     mobile = request.POST.get('mobile')
     birthDate = request.POST.get('birthDate')
     pinCode = request.POST.get('pinCode')
     email = request.POST.get('email')
     password = request.POST.get('password')
     confirmPassword = request.POST.get('confirmPassword')

    return render(request,'submit.html')
    


