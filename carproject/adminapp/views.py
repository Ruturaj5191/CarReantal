from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Basic_info,HomePage,Carinfo,Aboutinfo,TestInfo,BlogInfo
from webapp.models import Customer, Pickup_form,Contact

# Create your views here.

def home(request):
    return render(request,'admin/home.html')

def login(request):
    return render(request,'admin/login.html')

def save_login(req):
	customer = Customer.objects.filter(customer_mobile= req.POST['customer_mobile'],customer_password=req.POST['customer_password']).values()
	customer =list(customer)
	
	if len(customer)==0:
		return render(req,"login_Failed.html")
	else:
		req.session['customer_id'] = customer[0]['id']
		return redirect("/home")

def basicinfo(request):
    data=Basic_info.objects.all()
    obj={'data':data}
    return render(request,'admin/basicinfo.html',obj)

def save_basicinfo(request):
    print(request.POST)
    ba=Basic_info.objects.get(id=1)
    ba.office_address=request.POST['office_address']
    ba.office_email=request.POST['office_email']
    ba.office_mobile=request.POST['office_mobile']
    ba.office_facebook=request.POST['office_facebook']
    ba.office_instagram=request.POST['office_instagram']
    ba.office_linkedin=request.POST['office_linkedin']
    ba.save()
    return redirect("/basicinfo")

def pickupdata(request):
    pick=Pickup_form.objects.all()
    obj={'pick':pick}
    return render(request,'admin/pickupdata.html',obj)

def delete_pickup(request):
    id=request.GET['id']
    Pickup_form.objects.filter(id=id).delete()
    return redirect("/pickupdata")

def contactdata(request):
    cont=Contact.objects.all()
    obj={'cont':cont}
    return render(request,'admin/contactdata.html',obj)

def delete_contact(request):
    id=request.GET['id']
    Contact.objects.filter(id=id).delete()
    return redirect('/contactdata')

def homeimg(request):
    home=HomePage.objects.all()
    obj={'home':home}
    return render(request,'admin/homeimg.html',obj)

def save_homeimg(request):
    hao=HomePage.objects.get(id=1)
    if 'himg' in request.FILES:
        hao.himg=request.FILES['himg']
    hao.hheading=request.POST['hheading']
    hao.hparag=request.POST['hparag']
    if 'aimg' in request.FILES:
        hao.aimg=request.FILES['aimg']
    hao.save()
    return redirect("/homeimg")

def carinfo(request):
    cari=Carinfo.objects.all()
    obj={'cari':cari}
    return render(request,'admin/carinfo.html',obj)

def save_carinfo(request):
    Carinfo.objects.create(
        cname=request.POST['cname'],
        cprice=request.POST['cprice'],
        cimg=request.FILES['cimg'],

    )
    return redirect("/carinfo")

def delete_car(request):
    id=request.GET['id']
    Carinfo.objects.filter(id=id).delete()
    return redirect('/carinfo')

def edit_car(request):
    cari=Carinfo.objects.get(id=request.GET['id'])
    obj={'cari':cari}
    return render(request,'admin/edit_car.html',obj)

def update_car(request):
    upc=Carinfo.objects.get(id=request.POST['id'])
    upc.cname=request.POST['cname']
    upc.cprice=request.POST['cprice']
    if 'cimg' in request.FILES:
        upc.cimg=request.FILES['cimg']
    upc.save()
    return redirect('/edit_car')

def aboutinfo(request):
    abou=Aboutinfo.objects.all()
    obj={'abou':abou}
    return render(request,'admin/aboutinfo.html',obj)

def save_about(request):
    abo=Aboutinfo.objects.get(id=1)
    abo.abheading=request.POST['abheading']
    abo.abtext=request.POST['abtext']
    abo.save()
    return redirect("/aboutinfo")

def testinfo(request):
    test=TestInfo.objects.all()
    obj={'test':test}
    return render(request,'admin/testinfo.html',obj)

def save_testinfo(request):
    TestInfo.objects.create(
        timg=request.FILES['timg'],
        tinfo=request.POST['tinfo'],
        tname=request.POST['tname'],
        tpos=request.POST['tpos'],
    )
    return redirect("/testinfo")

def delete_testinfo(request):
    id=request.GET['id']
    TestInfo.objects.filter(id=id).delete()
    return redirect('/testinfo')

def edit_test(request):
    test=TestInfo.objects.get(id=request.GET['id'])
    obj={'test':test}
    return render(request,'admin/edit_test.html',obj)

def update_test(request):
    upt=TestInfo.objects.get(id=request.POST['id'])
    if 'timg' in request.FILES:
        upt.timg=request.FILES['timg']
    upt.tinfo=request.POST['tinfo']
    upt.tname=request.POST['tname']
    upt.tpos=request.POST['tpos']
    upt.save()
    return redirect("/testinfo")


def bloginfo(request):
    blo=BlogInfo.objects.all()
    obj={'blo':blo}
    return render(request,'admin/bloginfo.html',obj)

def save_bloginfo(request):
    BlogInfo.objects.create(
        blimg=request.FILES['blimg'],
        bldate=request.POST['bldate'],
        blhead=request.POST['blhead'],
        bltext=request.POST['bltext'],
    )
    return redirect("/bloginfo")

def delete_bloginfo(request):
    id=request.GET['id']
    BlogInfo.objects.filter(id=id).delete()
    return redirect('/bloginfo')

def edit_blog(request):
    blo=BlogInfo.objects.get(id=request.GET['id'])
    obj={'blo':blo}
    return render(request,'admin/edit_blog.html',obj)

def update_blog(request):
    upb=BlogInfo.objects.get(id=request.POST['id'])
    if 'blimg' in request.FILES:
        upb.blimg=request.FILES['blimg']
    upb.bldate=request.POST['bldate']
    upb.blhead=request.POST['blhead']
    upb.bltext=request.POST['bltext']
    upb.save()
    return redirect("/bloginfo")

