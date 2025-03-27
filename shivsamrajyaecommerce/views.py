

from django.shortcuts import render # type: ignore

from customer.models import Customer
from state.models import State
from franchise.models import Franchise
from district.models import District
from taluka.models import Taluka
from village.models import Village
from slider.models import Slider
from category.models import Category
from brands.models import Brands
from contactus.models import Contactus
from product.models import Product
from wishlist.models import Wishlist
from cart.models import Cart


from django.shortcuts import redirect # type: ignore




def product(requset):
    productdata=Product.objects.all()
    data={
       
        "plist":productdata
        
   }
    print(data)

    return render(requset,'home.html',data)


def contactus(request):
    if 'user_email' not in request.session:
        return redirect("/login/")
    categorydata= Category.objects.all()
    branddata=Brands.objects.all()
    user_name = request.session.get('user_name', None)
   
    data={
       
        "category":categorydata,
        "brand":branddata,
        "user_name": user_name,
        
   }
    return render(request,'contactus.html',data)
    
  
def sub(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        enquiry = request.POST.get("enquiry", "")

     
        insert = Contactus(
            contact_name=name,
            contact_email=email,
            contact_enquiry=enquiry
        )
        insert.save( )
        
    
    return render(request, "contactus.html") 




def about(request):
    if 'user_email' not in request.session:
        return redirect("/login/")
    categorydata= Category.objects.all()
    branddata=Brands.objects.all()
    user_name = request.session.get('user_name', None)
   
    data={
       
        "category":categorydata,
        "brand":branddata,
        "user_name": user_name,
        
   }
    return render(request,'about.html',data)
    
def home(request):
   sliderdata= Slider.objects.all()
   categorydata= Category.objects.all()
   branddata=Brands.objects.all()

   user_name = request.session.get('user_name', None)

   productdata=Product.objects.all()[:4]  
   product=Product.objects.all()[86:92]  
    

   data={
        "list":sliderdata,
        "category":categorydata,
        "brand":branddata,

        
        "user_name": user_name,  # Pass the user name to the template

        "plist":productdata,
        "product":product
        
   }
   return render(request,'home.html',data)

def logout(request):
    request.session.flush()  # Clear session data
    return redirect("/")  # Redirect to home page
 


def registration(request):
    if request.method == "POST":
        full_name_eng = request.POST.get("fullNameEng")
        full_name_marathi = request.POST.get("fullNameMarathi")
        mobile = request.POST.get("mobile")
        birth_date = request.POST.get("birthDate")
        state_id = request.POST.get("state")
        franchise_id = request.POST.get("franchise")
        district_id = request.POST.get("district")
        taluka_id = request.POST.get("taluka")
        village_id = request.POST.get("village")
        pin_code = request.POST.get("pinCode")
        email = request.POST.get("email")
        password = request.POST.get("password")

        state = State.objects.get(state_id=state_id)
        franchise = Franchise.objects.get(franchise_id=franchise_id)
        district = District.objects.get(district_id=district_id) 
        taluka = Taluka.objects.get(taluka_id=taluka_id) 
        village = Village.objects.get(village_id=village_id)

        customer = Customer(
            c_fullNameEng=full_name_eng,
            c_fullNameMarathi=full_name_marathi,
            c_mobile=mobile,
            c_birthDate=birth_date,
            state=state,
            franchise=franchise,
            District=district,
            taluka=taluka,
            village=village,
            c_pinCode=pin_code,
            c_email=email,
            c_password=password
        )
        customer.save()
        return redirect("/login/")

    states = State.objects.all()
    franchises=Franchise.objects.all()
    districts = District.objects.all()
    talukas = Taluka.objects.all()
    villages = Village.objects.all()
    return render(request, "registration.html", {
        "states": states,
        "districts": districts,
        "talukas": talukas,
        "villages": villages,
        "franchises":franchises
    })
    categorydata= Category.objects.all()
    branddata=Brands.objects.all()
   
    data={
       


        "category":categorydata,
        "brand":branddata,

        "category":categorydata,
        "brand":branddata

        
   }
    return render(request,'general.html',data) 


def login(request):
    error_message = ""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
         
        try:
            customer = Customer.objects.get(c_email=email, c_password=password)


            request.session['user_email'] = email
            request.session['user_name'] = customer.c_fullNameEng  

            request.session['user_id'] = str(customer.c_id)
            print(f"DEBUG: Customer ID from session: {request.session.get('user_id')}")
  

            return redirect("/")  
        except Customer.DoesNotExist:
            error_message = "Invalid email or password. Please try again."
    
    return render(request, 'login.html', {"error": error_message})
    categorydata= Category.objects.all()
    branddata=Brands.objects.all()
   
    data={
       
    "category":categorydata,
    "brand":branddata
        
   }
    return render(request,'login.html',data)
     
def general(request):
    #  if 'username' not in request.session:
        # return redirect("/login/")
     categorydata= Category.objects.all()
     branddata=Brands.objects.all()
   
     data={
       
        "category":categorydata,
        "brand":branddata
        
   }
     return render(request,'general.html',data) 
     

def grocery(request):
    # if 'username' not in request.session:
        # return redirect("/login/")
    categorydata= Category.objects.all()
    branddata=Brands.objects.all()
   
    data={
       
        "category":categorydata,
        "brand":branddata
        
   }
    return render(request,'grocery.html',data)
    


def Spices(request):
    # if 'username' not in request.session:
        # return redirect("/login/")
    categorydata= Category.objects.all()
    branddata=Brands.objects.all()
   
    data={
       
        "category":categorydata,
        "brand":branddata
        
   }
    return render(request,'Spices.html',data)
    
    

def cosmetic(request):
    # if 'username' not in request.session:
        # return redirect("/login/")
    categorydata= Category.objects.all()
    branddata=Brands.objects.all()
   
    data={
       
        "category":categorydata,
        "brand":branddata
        
   }
    return render(request,'cosmetic.html',data)
    

def fooditems(request):
    # if 'username' not in request.session:
        # return redirect("/login/")
    categorydata= Category.objects.all() 
    branddata=Brands.objects.all()
   
    data={
       
        "category":categorydata,
        "brand":branddata
        
   }
    return render(request,'fooditems.html',data)
    
def shop(request):
    # if 'username' not in request.session:
        # return redirect("/login/")
    categorydata= Category.objects.all()
    branddata=Brands.objects.all()
    productdata=Product.objects.all() 
    user_name = request.session.get('user_name', None)
     
    data={
       
        "category":categorydata,
        "brand":branddata,
        "plist":productdata,
        "user_name": user_name, 
        
   }
    return render(request,'shop.html',data)
    

def stationary(request):
    # if 'username' not in request.session:
        # return redirect("/login/")
    categorydata= Category.objects.all()
    branddata=Brands.objects.all()
   
    data={
       
        "category":categorydata,
        "brand":branddata
        
   }
    return render(request,'stationary.html',data)
    

   
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
     
def cart_submit(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        c_id = request.session.get('user_id')
        cart_quantity=request.POST.get("cart_quantity")
        cart_price=request.POST.get("cart_price")  
        if not c_id:
            return redirect("/")  
        
        try:
            customer = Customer.objects.get(c_id=int(c_id))  
        except Customer.DoesNotExist:
            return redirect("/") 

     
        insert =Cart(
        product_id= Product.objects.get(product_id=product_id),
        c_id=customer,
        cart_quantity=cart_quantity,
        cart_price=cart_price
            
        )
        
   
    insert.save()
    return redirect("/")

def wishlist(request):
    wishlist = Wishlist.objects.all()  
    data = {
        "wishlist": wishlist
    }
    return render(request, "wishlist.html", data)

def wishlistdelete(request, id):
    wishlist= Wishlist.objects.get(wish_id=id)
    wishlist.delete()
    return redirect("/wishlist/")


def wishlist_add(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        c_id = request.session.get('user_id')

        if not c_id:
            return redirect("/") 

        try:
            customer = Customer.objects.get(c_id=int(c_id)) 
        except Customer.DoesNotExist:
            return redirect("/") 

        
        if Wishlist.objects.filter(c_id=customer, product_id=product_id).exists():
            return redirect("/") 

       
        insert = Wishlist(
            product_id=Product.objects.get(product_id=product_id),
            c_id=customer
        )
        insert.save()
        
    return redirect("/")


def slider(request):
    sliderdata= slider.objects.all()
    data={
        "list":sliderdata
    }
    return render(request,'home.html',data)








     





     


