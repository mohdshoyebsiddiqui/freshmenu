from django.shortcuts import render,redirect
from .models import Category,Product,Order,Wishlist,Comments,Follow,Profile
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password
from .forms import ProductForm,CateForm,UserCreate
from django.db.models import Count,Sum
from django.contrib.sessions import base_session
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime,timedelta
from django.contrib import sessions
from django.views.decorators.cache import cache_page
# from .signals import notification
from django.dispatch import receiver,Signal




# Create your views here.




def home(request):
        # Signal.notification.send(sender=None, request=request, user=['india'])
        data=Product.objects.all()
        total2=''
        cart=[]
        totalcart=''
        if request.user.is_authenticated:
            usern=request.user
            cart=Order.objects.filter(user=usern,order_status='cart')
            totalcart=Order.objects.filter(user=usern,order_status='cart').count()
            total=cart.annotate(total_sum=Sum('price'))
            total2=0
            request.session['django']=3.5
            request.session['name']='india'
            for i in total:
                total2+=i.price
                response = HttpResponse("Cookie set")
                response.set_cookie('ffgfgdfg', "india", max_age=3600)

        else:
            cart=[]
            response = HttpResponse("Cookie set")
            response.set_cookie('namewe', "tuesday", expires= datetime.utcnow()+timedelta(days=365))
            cookie_value = request.COOKIES.get('csrftoken')
            print(cookie_value)
            response.delete_cookie('name')
        return render(request,'index.html',{'data':data, 'cart':cart,'total':total2,'totalcart':totalcart}) 





def search(request):
    if request.method=='POST':
        search=request.POST.get('search')
        data=[]
        data=Product.objects.filter(name__icontains=search)
        return render(request,'search.html',{'search':search,'data':data})
    else:
     return render(request,'search.html')




def userlist(request):
 if request.user.is_authenticated:
    user=request.user
    listuser=Follow.objects.filter(user=request.user)
    alluser=[]
    alluser=User.objects.all()
   
    for i in listuser:
        userdata=User.objects.get(username=i.followers)
        if userdata in alluser:
                alluser = alluser.exclude(pk=userdata.pk)


    return render(request,'userlist.html',{'data':alluser})

    
 else:
    return redirect('signin')


@login_required
def userprofile(request,id):
    user=User.objects.get(id=id)
    profiledata=Profile.objects.get(userid=id)

    follower=len(Follow.objects.filter(user=user.username))
    following=len(Follow.objects.filter(followers=user.username))


    return render(request,'userprofile.html',{'user':user,'follower':follower,'following':following,'profiledata':profiledata})

@cache_page(60)
def follow(request):
 if request.user.is_authenticated:
   if request.method=='POST':
       user=request.user
       followers=request.POST.get("followers")

       if Follow.objects.filter(user=user,followers=followers).first():
            unfollow=Follow.objects.filter(user=user,followers=followers)
            unfollow.delete()
            return redirect('userlist')  
       else:
            saved=Follow(user=user,followers=followers)
            saved.save()
            return redirect('friend')
   else:
        return redirect('home')
 else:
    return redirect('signin')

@cache_page(60)
def friend(request):
 if request.user.is_authenticated:
   listuser=Follow.objects.filter(user=request.user)
   data=[]
   for i in listuser:
       userdata=User.objects.get(username=i.followers)
       data.append(userdata)
   return render(request,'friend.html',{'data':data})
 else:
    return redirect('signin')
 
 # user - follower

def product(request,id):
    data=Product.objects.get(id=id)
    commentdata=Comments.objects.filter( product=data.id)

    if request.method=='POST':
         if request.user.is_authenticated:
            user=request.user
            comment = request.POST.get('comment')
            comments=Comments(user=user,product=data.id, name=comment)
            comments.save()
            return render(request,'product.html',{'data':data,'commentdata':commentdata})
         else:
            return redirect('signin')

    return render(request,'product.html',{'data':data,'commentdata':commentdata})

def cart(request,id):
    if request.user.is_authenticated:
         data=Product.objects.get(id=id)
         usern=request.user

         alldata=Order.objects.filter(user=usern,order_status='cart')
         for i in alldata:
            if data.name==i.name:
             print(i.quantity)
             print(i.price)
             i.quantity+=1
             i.price=(data.price*i.quantity)
             i.save()
             return redirect('home')
         
         Order.objects.create(name=data.name, price=data.price, user=usern )
         return redirect('home')
            

         
    else:
        return redirect('signin')
    
def cartplus(request,id):
    if request.user.is_authenticated:
        data=Order.objects.get(id=id)
        pro=Product.objects.filter(name=data.name).first()
        data.quantity+=1
        data.price=(pro.price*data.quantity)
        data.save()
        return redirect('home')
    

def cartminus(request,id):
    if request.user.is_authenticated:
        data=Order.objects.get(id=id)
        pro=Product.objects.filter(name=data.name).first()
        data.quantity-=1
        data.price=(pro.price*data.quantity)
        if data.quantity==0:
         data.delete()
        else:
            data.save()
        return redirect('home')
   
def checkout(request):
    return render(request,'checkout.html')


def wishlist(request):
  if request.user.is_authenticated:
    user=request.user
    data=[]
    wish=Wishlist.objects.filter(user=user)
    for i in wish:
        data.append(Product.objects.get(id=i.product))
    
    return render(request,'wishlist.html',{'data':data})
  else:
       return redirect('signin')



def addwish(request,id):
 if request.user.is_authenticated:
    product=id
    user=request.user
    data=Wishlist.objects.filter(user=user)
    for i in data:
        if product==i.id:
            i.delete()
            return redirect('home')
    Wishlist.objects.create(product=product,user=user)
    return redirect('home')
 else:
       return redirect('signin')
         

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        request.session['username']=username
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Profile details correct.") 
            messages.error(request, "Profile update failed.")
            return render(request,'signin.html')
        else:
            messages.error(request, "Profile update failed.")
            return render(request,'signin.html')
    else:
        messages.info(request, "username and password details to login.") 
        return render(request,'signin.html')



def signup(request):
    if request.method=='POST':
        fm=UserCreate(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            first=fm.cleaned_data['first_name']
            last=fm.cleaned_data['last_name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password2']
            password=make_password(password)
            data=User(username=username,first_name=first,last_name=last,email=email,password=password)
            data.save()
            login(request,data)

            profile=User.objects.get(username=username)
            profilecreate=Profile.objects.create(user=profile,userid=profile.id)
            profilecreate.save()

            return redirect('profile')
        
    else:
        fm=UserCreate()
        return render(request,'signup.html',{'fm':fm})

def logouts(request):
    logout(request)
    return redirect('signin')


@login_required
def profile(request):
        id=request.user
        se=request.session.get('name', default='guest')
        request.session.setdefault('surname','bharat')
        allkey= request.session.items()
        request.session.modified=True
        # if 'name' in request.session:
        #     del request.session['name']
        # request.session.set_expiry(10)
        cookie_age =request.session.get_session_cookie_age() 
        cookie_date =request.session.get_expiry_date()  
        cookie_expiry =request.session.get_expiry_age()  
        cookie_browser =request.session.get_expire_at_browser_close() 
        
        user=User.objects.get(username=id)
        profiledata=Profile.objects.get(userid=user.id)

        return render(request,'profile.html',{'user':user,'profiledata':profiledata,'sessiondata':cookie_date,'allkey':allkey})

@login_required
def profileedit(request,id):
    data=Profile.objects.get(userid=id)
    if request.method=='POST':
        if request.FILES.get('image')==None:
            image=data.profilepic
            bio=request.POST.get('bio')
            address=request.POST.get('address')
            data.profilepic=image
            data.bio=bio
            data.address=address
            data.save()
            return redirect('profile')
        if request.FILES.get('image')!=None:
            image=request.FILES.get('image')
            bio=request.POST.get('bio')
            address=request.POST.get('address')
            data.profilepic=image
            data.bio=bio
            data.address=address
            data.save()
            return redirect('profile')

    else:
     return render(request,'profileedit.html',{'data':data})


@login_required
def order(request):
         return render(request,'order.html')



def orderplaced(request):
        if request.user.is_authenticated:
            usern=request.user
            cart=Order.objects.filter(user=usern,order_status='cart')
            cart.update(order_status='placed')
            
        else:
            cart=[]
        return  redirect('home')
    


# dashboard 
def dashboard(request):
    if request.user.is_authenticated:
     if request.user.is_superuser:
      return render(request, 'dashboard/dashboard.html')
     
        
    
    return redirect('signindash')

def productcreate(request):
    if request.user.is_authenticated:
     if request.user.is_superuser:
        if request.method=='POST':
            fm=ProductForm(request.POST,request.FILES)
            if fm.is_valid():
                name=fm.cleaned_data['name']
                price=fm.cleaned_data['price']
                des=fm.cleaned_data['des']
                ingredient=fm.cleaned_data['ingredient']
                category=fm.cleaned_data['category']
                image=fm.cleaned_data['image']
                data=Product(name=name,price=price,des=des,ingredient=ingredient,category=category,image=image)
                data.save()
                return redirect('product')
        else:
            fm=ProductForm()
        return render(request, 'dashboard/product-create.html',{'fm':fm})
     return redirect('signindash')

def productedit(request,id):
    if request.user.is_authenticated:
     if request.user.is_superuser:
        data=Product.objects.get(id=id)
        if request.method=='POST':

            fm=ProductForm(request.POST,request.FILES,instance=data)
            fm.save()
            return redirect('product')
        else:
            fm=ProductForm(instance=data)
        return render(request, 'dashboard/product-edit.html',{'fm':fm})
    return redirect('signindash')



def productview(request):
    if request.user.is_authenticated:
     if request.user.is_superuser:
        data=Product.objects.all()
        return render(request, 'dashboard/product.html',{'data':data})
    return redirect('signindash')

def productdelete(request,id):
    if request.user.is_authenticated:
     if request.user.is_superuser:
        data=Product.objects.get(id=id)
        data.delete()
        return redirect('product')
    return redirect('signindash')


def categorycreate(request):
    if request.user.is_authenticated:
     if request.user.is_superuser:
        if request.method=='POST':
            fm=CateForm(request.POST)
            if fm.is_valid():
                name=fm.cleaned_data['name']
                data=Category(name=name)
                data.save()
                return redirect('category')
        else:
        
            fm=CateForm()
    
        return render(request, 'dashboard/category-create.html',{'fm':fm})
    return redirect('signindash')

def categoryedit(request,id):
    if request.user.is_authenticated:
     if request.user.is_superuser:
        data=Category.objects.get(id=id)
        if request.method=='POST':
            fm=CateForm(request.POST,instance=data)
            fm.save()
            return redirect ('category')
        else:
            fm=CateForm(instance=data)
        return render(request, 'dashboard/category-edit.html',{'fm':fm})
     return redirect('signindash')

def categorydelete(request,id):
    if request.user.is_authenticated:
     if request.user.is_superuser:
        data=Category.objects.get(id=id)
        data.delete()
        return redirect('category')
    return redirect('signindash')

def categoryview(request):
    if request.user.is_authenticated:
     if request.user.is_superuser:

       data=Category.objects.annotate(total_count=Count('product'))  
           
       return render(request, 'dashboard/category.html',{'data':data})
    return redirect('signindash')




def userdash(request):
       user=User.objects.filter(is_active=True)
       return render(request,'dashboard/user.html',{'user':user})

def userdelete(request,id):
    data=User.objects.get(id=id)
    data.delete()
    return redirect('userdash')
   

# dashboard order
def currentorder(request):
        if request.user.is_authenticated:
            usern=request.user
            cart=Order.objects.filter(order_status='placed')
            total=cart.annotate(total_sum=Sum('price'))
            total2=0
            for i in total:
                total2+=i.price
        else:
            cart=[]
        return render(request, 'dashboard/current-order.html' , {'data':cart,'total':total2})

def oldorder(request):
    if request.user.is_authenticated:
            cart=Order.objects.filter(order_status='confirm')
    return render(request, 'dashboard/old-order.html',{'data':cart})

def cancelorder(request):
    if request.user.is_authenticated:
            cart=Order.objects.filter(order_status='cancel')
    return render(request, 'dashboard/cancel-order.html',{'data':cart})

# dashboard signin
def signindash(request):
   
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        return redirect('dashboard')
    else:
        return render(request, 'dashboard/sign-in.html')


def signupdash(request):
    return render(request, 'dashboard/sign-up.html')

def orderconfirm(request,id):
    data=Order.objects.get(id=id)
    data.order_status='confirm'
    data.save()
    return redirect('old')

def ordercancel(request,id):
    data=Order.objects.get(id=id)
    data.order_status='cancel'
    data.save()
    return redirect('cancel')