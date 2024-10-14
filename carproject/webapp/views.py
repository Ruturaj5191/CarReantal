from django.http import HttpResponse
from django.shortcuts import redirect, render
from adminapp.models import Basic_info,HomePage,Carinfo,Aboutinfo,TestInfo,BlogInfo
from webapp.models import Pickup_form,Contact,Customer

# Create your views here.
def Home(request):
    data=Basic_info.objects.get(id=1)
    home=HomePage.objects.get(id=1)
    cari=Carinfo.objects.all()
    abou=Aboutinfo.objects.get(id=1)
    test=TestInfo.objects.all()
    cust=Customer.objects.all()
    obj={'data':data,'home':home,'cari':cari,'abou':abou,'test':test,'cust':cust}
    return render(request,'user/index.html',obj)

def about(request):
    data=Basic_info.objects.get(id=1)
    home=HomePage.objects.get(id=1)
    abou=Aboutinfo.objects.get(id=1)
    test=TestInfo.objects.all()
    obj={'data':data,'home':home,'abou':abou,'test':test}
    return render(request,'user/about.html',obj)

def blog(request):
    data=Basic_info.objects.get(id=1)
    home=HomePage.objects.get(id=1)
    blo=BlogInfo.objects.all()
    obj={'data':data,'home':home,'blo':blo}
    return render(request,'user/blog.html',obj)

def car(request):
    data=Basic_info.objects.get(id=1)
    home=HomePage.objects.get(id=1)
    cari=Carinfo.objects.all()
    obj={'data':data,'home':home,'cari':cari}
    return render(request,'user/car.html',obj)

def contact(request):
    data=Basic_info.objects.get(id=1)
    home=HomePage.objects.get(id=1)
    obj={'data':data,'home':home}
    return render(request,'user/contact.html',obj)

def services(request):
    data=Basic_info.objects.get(id=1)
    home=HomePage.objects.get(id=1)
    obj={'data':data,'home':home}
    return render(request,'user/services.html',obj)

def save_pickupform(request):
    Pickup_form.objects.create(
        pickup=request.POST['pickup'],
        dropoff=request.POST['dropoff'],
        pickupdate=request.POST['pickupdate'],
        dropoffdate=request.POST['dropoffdate'],
        pickuptime=request.POST['pickuptime'],
    )
    return redirect("/")

def save_contact(request):
    print(request.POST)
    Contact.objects.create(
        cname=request.POST['cname'],
        cemail=request.POST['cemail'],
        csubject=request.POST['csubject'],
        cmessage=request.POST['cmessage'],
        ctext=request.POST['ctext'],
    )
    return redirect("/contact")

def signup(request):
    return render(request,'user/signup.html')

def create_account(request):
	customer = Customer(
		customer_name=request.POST['customer_name'],
		customer_mobile=request.POST['customer_mobile'],
		customer_email=request.POST['customer_email'],
		customer_password=request.POST['customer_password']
	)
	customer.save()
	return redirect("/login")

def login(request):
    return render(request,'user/login.html')

def login_process(req):
	customer = Customer.objects.filter(customer_mobile= req.POST['customer_mobile'],customer_password=req.POST['customer_password']).values()
	customer =list(customer)
	
	if len(customer)==0:
		return render(req,"login_Failed.html")
	else:
		req.session['customer_id'] = customer[0]['id']
		return redirect("/")
