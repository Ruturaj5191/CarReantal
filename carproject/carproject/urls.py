"""
URL configuration for carproject project.

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
from django.contrib import admin
from django.urls import path
from webapp.views import Home,about,blog,car,contact,services,save_pickupform,save_contact,signup,create_account,login,login_process
from adminapp.views import basicinfo,save_basicinfo,pickupdata,delete_pickup,contactdata,delete_contact,homeimg,save_homeimg,carinfo,save_carinfo,save_about,aboutinfo,testinfo,save_testinfo,delete_testinfo,bloginfo,save_bloginfo,edit_blog,update_blog,edit_test,update_test,edit_car,update_car,home,login
urlpatterns = [
    path('',Home),
    path('about/',about),
    path('blog/',blog),
    path('car/',car),
    path('contact/',contact),
    path('services/',services),
    path('save_pickupform/',save_pickupform),
    path('save_contact/',save_contact),
    path('signup/',signup),
    path('create_account/',create_account),
    path('login/',login),
    path('login_process/',login_process),
    
    
    # path('admin/', admin.site.urls),

    path('admin/',login),
    path('home/',home),
    path('basicinfo/',basicinfo),
    path('save_basicinfo/',save_basicinfo),
    path('pickupdata/',pickupdata),
    path('delete_pickup/',delete_pickup),
    path('contactdata/',contactdata),
    path('delete_contact/',delete_contact),
    path('homeimg/',homeimg),
    path('save_homeimg/',save_homeimg),
    path('carinfo/',carinfo),
    path('save_carinfo/',save_carinfo),
    path('aboutinfo/',aboutinfo),
    path('save_about/',save_about),
    path('testinfo/',testinfo),
    path('save_testinfo/',save_testinfo),
    path('delete_testinfo/',delete_testinfo),
    path('bloginfo/',bloginfo),
    path('save_bloginfo/',save_bloginfo),
    path('edit_blog/',edit_blog),
    path('update_blog/',update_blog),
    path('edit_test/',edit_test),
    path('update_test/',update_test),
    path('edit_car/',edit_car),
    path('update_car/',update_car),

]
