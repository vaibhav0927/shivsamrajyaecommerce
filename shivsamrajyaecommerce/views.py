from django.shortcuts import render # type: ignore

def home(request):
    return render(request,'home.html')

def registration(request):
    return render(request,'registration.html')

def reg(request):
     name = request.POST.get("name", "")
     email = request.POST.get("email", "")
     password = request.POST.get("password","")
     data = {
         "name":name,
         "email":email,
         "password":password
     }
     return render(request,"regisration.html",data)

def login(request):
    return render(request,'login.html')

def log(request):
    email = request.POST.get("email","")
    password = request.POST.get("password","")
    data = {
        "email":email,
        "password":password
    }
    return render(request,"login.html",data)