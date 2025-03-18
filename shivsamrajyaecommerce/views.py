from django.http import JsonResponse # type: ignore
from django.shortcuts import render # type: ignore
from django.shortcuts import redirect # type: ignore



    
def contactus(request):
     if 'username' in request.session:
        return render(request,'contactus.html')
     else:
        return redirect("/login/")

def loginverify(request):
    if request.method=="POST":
        email= request.POST.get('email')
        password=request.POST.get("password")
        try:
          Customers.objects.get(c_email=email,c_pass=password)
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
from customer.models import Customers
from state.models import State
from district.models import District
from taluka.models import Taluka
from village.models import Village

    



def registration(request):
    if request.method == "POST":
        full_name_eng = request.POST.get("fullNameEng")
        full_name_marathi = request.POST.get("fullNameMarathi")
        mobile = request.POST.get("mobile")
        birth_date = request.POST.get("birthDate")
        state_id = request.POST.get("state")
        district_id = request.POST.get("district")
        taluka_id = request.POST.get("taluka")
        village_id = request.POST.get("village")
        pin_code = request.POST.get("pinCode")
        email = request.POST.get("email")
        password = request.POST.get("password")

        state = State.objects.get(id=state_id) if state_id else None
        district = District.objects.get(id=district_id) if district_id else None
        taluka = Taluka.objects.get(id=taluka_id) if taluka_id else None
        village = Village.objects.get(id=village_id) if village_id else None

        customer = Customers(
            full_name_eng=full_name_eng,
            full_name_marathi=full_name_marathi,
            mobile=mobile,
            birth_date=birth_date,
            state=state,
            district=district,
            taluka=taluka,
            village=village,
            pin_code=pin_code,
            email=email,
            password=password  
        )
        
        customer.save()
        return redirect("registration")




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
     state = request.POST.get('state')
     district = request.POST.get('district')
     taluka = request.POST.get('taluka')
     village = request.POST.get('village')
     franchise = request.POST.get('franchise')


     insertquery=Customers(
         fullNameEng=fullNameEng,
         fullNameMarathi=fullNameMarathi,
         mobile=mobile,
         birthDate=birthDate,
         pinCode=pinCode,
         email=email,
         password=password,
         confirmPassword=confirmPassword,
         state=state,
         district=district,
         taluka=taluka,
         village=village,
         franchise=franchise,

     )
     insertquery.save()
     return redirect("/login/")
    else:
         
         return render(request,'registration.html')
    
def slider(request):
    sliderdata= slider.objects.all()
    data={
        "list":sliderdata
    }
    return render(request,'home.html',data)



   



     


