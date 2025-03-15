from django.shortcuts import render # type: ignore
from django.shortcuts import redirect # type: ignore
from customer.models import Customer


    
def contactus(request):
     if 'username' in request.session:
        return render(request,'contactus.html')
     else:
        return redirect("/login/")

def loginverify(request):
    if request.method=="POST":
        email= request.POST.get('username')
        password=request.POST.get("password")
        try:
          Customer.objects.get(c_email=email,c_pass=password)
        except:
        
           return render(request,'login.html')
        else:
             request.session['username']='admin'
             return redirect('/')

def about(request):
      if 'username' in request.session:
        return render(request,'about.html')
      else:
        return redirect("/login/")
def home(request):
     
        return render(request,'home.html')
    

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')
def general(request):
     if 'username' in request.session:
        return render(request,'general.html')
     else:
        return redirect("/login/")

def grocery(request):
     if 'username' in request.session:
        return render(request,'grocery.html')
     else:
        return redirect("/login/")
def Spices(request):
     if 'username' in request.session:
        return render(request,'Spices.html')
     else:
        return redirect("/login/")
def cosmetic(request):
     if 'username' in request.session:
        return render(request,'cosmetic.html')
     else:
        return redirect("/login/")

def fooditems(request):
     if 'username' in request.session:
        return render(request,'fooditems.html')
     else:
        return redirect("/login/")

def shop(request):
     if 'username' in request.session:
        return render(request,'shop.html')
     else:
        return redirect("/login/")

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


    if 'username' in request.session:
        return render(request,'stationary.html')
    else:
        return redirect("/login/") 





     


