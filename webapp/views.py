from django.shortcuts import *
from .models import *
from django.http import *
from django.contrib import auth
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    category=Categories.objects.all()
    return render(request,'home.html',{'category':category})
def products(request):
    category=Categories.objects.all()
    default_category='vogue'
    item_pic=Category_pics.objects.filter(cat__slug=default_category)
    all_products=Final_products.objects.filter(category__slug = default_category)
    return render(request,'product.html',{'cat':category,'pro':all_products,'d':default_category,'item_pic':item_pic})
def single_category(request,slug):
    category=Categories.objects.all()
    default_category=slug
    item_pic=Category_pics.objects.filter(cat__slug=default_category)
    all_products=Final_products.objects.filter(category__slug=default_category)
    return render(request,'product1.html',{'cat':category,'pro':all_products,'d':default_category,'item_pic':item_pic})
def aboutus(request):
    return render(request,'about.html')
def client(request):
    return render(request,'client.html')
@login_required(login_url="login")
def blog(request):
    return render(request,'blog.html')
def blog_detail(request):
    return render(request,'blog-detail.html')
def product_details(request,d):
    details=Final_products.objects.get(id=d)
    return render(request,'product-detail.html',{'details':details})
def contactus(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def logout(request):
     auth.logout(request)
     return HttpResponseRedirect('/')
def auth_view(request):
    #print request.POST,type(request)
    username=request.POST['username']
    password=request.POST['password']
    #match username & password
    #if not match,authenticate() will return None
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('blog')
    else:
        return HttpResponseRedirect('/invalid/')
def signup(request):
    if request.method=="POST":
        form=Reg_form(request.POST,request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            u= User.objects.create_user(username=cd['username'],email=cd['email'],password=cd['password'])
            p=Profile(user=u,pic=form.cleaned_data['pic'])
            p.save()
            return redirect('login')
    else:
        form=Reg_form()
    return render(request,"signup.html",{'form':form})
