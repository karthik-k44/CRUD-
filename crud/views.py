from django.shortcuts import render,redirect
from django.views.generic import View
from crud.forms import MobileForm,Register,Signin
from crud.models import Mobiles
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator


# Create your views here.
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
            messages.error(request,"login first")
        else:
            return fn(request, *args,**kwargs)
    return wrapper
    
@method_decorator(signin_required, name="dispatch")
class Mobilesview(View):
    def get(self, request,*args, **kwargs):
        form= MobileForm()
        return render(request, 'mobiles.html',{'form':form})
     
    def post(self, request,*args, **kwargs):
        form = MobileForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            print("created")
            return render(request, 'mobiles.html', {'form': form})

        else:
            return render(request, 'mobiles.html', {'form': form})

@method_decorator(signin_required, name="dispatch")
class Mobilelist(View):
    def get(self, request,*args,**kwargs):
        form=Mobiles.objects.all()
        print(request.GET)
        if "Company" in request.GET:
            Company=request.GET.get("Company")
            form=form.filter(Company__iexact=Company)
        return render(request,"list.html",{"form":form})
    def post(self,request,*args, **kwargs):
        Name = request.POST.get("box")
        Price = request.POST.get("box")
        Company = request.POST.get("box")
        form=form.objects.filter(Name=Name,Price=Price,Company=Company)
        return render(request,"list.html",{"form":form})
        

class Mobiledelete(View):
    def get(self,request,*args, **kwargs):
        id = kwargs.get("id")
        Mobiles.objects.get(id=id).delete()
        return redirect('mobile-al')
    
class Mobiledetails(View):
    def get(self,request,*args, **kwargs):
        id = kwargs.get("id")
        data=Mobiles.objects.get(id=id)
        return render(request, "details.html",{'data':data})
    
class Mobileupdate(View):
    def get(self,request,*args, **kwargs):
        id = kwargs.get("id")
        data=Mobiles.objects.get(id=id)
        form=MobileForm(instance=data)
        return render(request,"mobiles.html",{'form':form})
    
    def post(self, request, *args, **kwargs):
        id =kwargs.get("id")
        data=Mobiles.objects.get(id=id)
        form=MobileForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        else:
            print("...")
        return redirect('mobile-al')
    
class Signup(View):
    def get(self,request,*args, **kwargs):
        form=Register()
        return render (request,"reg.html",{"form":form})
    
    def post(self, request, *args, **kwargs):
       form=Register(request.POST)
       if form.is_valid():
           User.objects.create_user(**form.cleaned_data)
           messages.success(request,"added successfully")
           
        #    form.save()
       else:
            messages.error(request,"error occured")
       return render(request,"reg.html",{"form":form})
   

class Login(View):
    
    def get(self, request, *args, **kwargs):
       form=Signin()
       return render(request,"login.html",{"form":form})
   
    def post(self, request, *args, **kwargs):
        form=Signin(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(u_name,pwd)
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                print("valid credentials")
                login(request,user_obj)
                return redirect("mobile-al")
            else:
                print("invalid credentials")
        else:
            print("get out")
        return render(request,"login.html",{"form":form})
    
class Logout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
        
   
    