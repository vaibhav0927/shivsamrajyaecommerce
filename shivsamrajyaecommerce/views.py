

from http.client import HTTPResponse
from django.http import JsonResponse # type: ignore


from django.http import JsonResponse # type: ignore





from django.shortcuts import render # type: ignore
from customer.models import Customer
from state.models import State
from district.models import District
from taluka.models import Taluka
from village.models import Village
from slider.models import Slider
from category.models import Category
from brands.models import Brands
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
          Customer.objects.get(c_email=email,c_pass=password)
        except:
        
           return render(request,'login.html')
        else:
             request.session['username']='admin'
             return redirect('/')

def about(request):
      categorydata= Category.objects.all()
      branddata=Brands.objects.all()
      data={
          "category":categorydata,
          "brand":branddata
      }
      return render(request,'about.html',data)
      
      if 'username' in request.session:
        return render(request,'about.html')
      else:
        return redirect("/login/")
     


def home(request):
   sliderdata= Slider.objects.all()
   categorydata= Category.objects.all()
   branddata=Brands.objects.all()
   
   data={
        "list":sliderdata,
        "category":categorydata,
        "brand":branddata
        
   }
   return render(request,'home.html',data)

   





   
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

        customer = Customer(
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
     
    categorydata= Category.objects.all()
    branddata=Brands.objects.all()
   
    data={
       
        "category":categorydata,  
        "brand":branddata
        
        }
    return render(request,'registration.html',data)
   

    states = State.objects.all()
    districts = District.objects.all()
    talukas = Taluka.objects.all()
    villages = Village.objects.all()
    return render(request, "registration.html", {
        "states": states,
        "districts": districts,
        "talukas": talukas,
        "villages": villages
    })



def login(request):
   categorydata= Category.objects.all()
   branddata=Brands.objects.all()
   
   data={
       
        "category":categorydata,  
        "brand":branddata
        
        }
   return render(request,'login.html',data)
    
def general(request):
   categorydata= Category.objects.all()
   branddata=Brands.objects.all()
   
   data={
       
        "category":categorydata,  
        "brand":branddata
        
        }
   return render(request,'general.html',data)
   if 'username' in request.session:
      return render(request,'general.html')
   else:
      return redirect("/login/")

def grocery(request):
   categorydata= Category.objects.all()
   branddata=Brands.objects.all()
   
   data={
       
        "category":categorydata,  
        "brand":branddata
        
        }
   return render(request,'grocery.html',data)
   if 'username' in request.session:
        return render(request,'grocery.html')
   else:
        return redirect("/login/")
def Spices(request):
   categorydata= Category.objects.all()
   branddata=Brands.objects.all()
   
   data={
       
        "category":categorydata,  
        "brand":branddata
        
        }
   return render(request,'Spices.html',data)
   if 'username' in request.session:
        return render(request,'Spices.html')
   else:
        return redirect("/login/")
def cosmetic(request):
   categorydata= Category.objects.all()
   branddata=Brands.objects.all()
   
   data={
       
        "category":categorydata,  
        "brand":branddata
        
        }
   return render(request,'cosmetic.html',data)
   if 'username' in request.session:
        return render(request,'cosmetic.html')
   else:
        return redirect("/login/")

def fooditems(request):
   categorydata= Category.objects.all()
   branddata=Brands.objects.all()
   
   data={
       
        "category":categorydata,  
        "brand":branddata
        
        }
   return render(request,'fooditems.html',data)
   if 'username' in request.session:
        return render(request,'fooditems.html')
   else:
        return redirect("/login/")

def shop(request):
   categorydata= Category.objects.all()
   branddata=Brands.objects.all()
   
   data={
       
        "category":categorydata,  
        "brand":branddata
        
        }
   return render(request,'shop.html',data)
   if 'username' in request.session:
        return render(request,'shop.html')
   else:
        return redirect("/login/")

def stationary(request):

   categorydata= Category.objects.all()
   branddata=Brands.objects.all()
   
   data={
       
        "category":categorydata,  
        "brand":branddata
        
        }
   return render(request,'stationary.html',data)
   if 'username' in request.session: 
         render(request,'stationary.html')
   else:
       return redirect("/login/")



<<<<<<< HEAD
insertquery=Customer(
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

=======

       



       
>>>>>>> 46221ebb5d22eab44c62cc89bf7dd03da6e7b98d
def submit(request):
     if request.method == "POST":


<<<<<<< HEAD
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


      insertquery=Customer(

           fullNameEng = request.POST.get('fullNameEng'),
           fullNameMarathi = request.POST.get('fullNameMarathi'),
           mobile = request.POST.get('mobile'),
           birthDate = request.POST.get('birthDate'),
           pinCode = request.POST.get('pinCode'),
           email = request.POST.get('email'),
           password = request.POST.get('password'),
           confirmPassword = request.POST.get('confirmPassword'),
           state = request.POST.get('state'),
           district = request.POST.get('district'),
           taluka = request.POST.get('taluka'),
           village = request.POST.get('village'),
=======

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
>>>>>>> 46221ebb5d22eab44c62cc89bf7dd03da6e7b98d
           franchise = request.POST.get('franchise')
      )

     insertquery=Customer(
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







     





     


