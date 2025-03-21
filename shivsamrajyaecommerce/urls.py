"""
URL configuration for shivsamrajyaecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from shivsamrajyaecommerce import settings, views
from django.conf.urls.static import static # type: ignore
from .views import registration


urlpatterns = [
    path('admin/', admin.site.urls),
    path("contactus/",views.contactus),
    path('login/',views.login),
    path('loginverify/',views.loginverify),
    path('registration/',views.registration),
    path('',views.home),
    path('about/',views.about),
    path('general/',views.general),
    path('cosmetic/',views.cosmetic),
    path('spices/',views.Spices),
    path('general/',views.general),
    path('fooditems/',views.fooditems),
    path('shop/',views.shop),
    path('grocery/',views.grocery),
    path('stationary/',views.stationary),

    path('submit/',views.submit),
    path('slider/',views.slider),
    # path('submit/',views.submit),
   







    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
