from django.shortcuts import render,redirect
from .forms import ProductForm,RegisterForm
from .models import products,ModelRegister
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,'index.html')

def shop(request):
    form = products.objects.all()
    return render(request,'shop.html',{'form':form})


def detail(request,pk):
    product= products.objects.get(id=pk)
    return render(request,'detail.html',{'product':product})

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')

def add_product(request):
    # if request.method == 'POST':
    #     form =ProductForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         print("product added successfully")
    return render(request,'add_product.html')

def fashion(request):
    return render(request,'fashion.html')


def login_view(request):

    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = ModelRegister.objects.get(email=email)
            if user.password == password:
               print('user logged successfully')
               return redirect('seller')
            
            elif user.email !=email:
                messages.error(request,"email doesnot exist")
                return redirect("login")
            
            elif user.password !=password:
                messages.error(request,'password doesnot exist')
                return redirect("login")
            else:
                messages.error(request,'invalid email or password')
                print('invalid email or password')
                return redirect('login')
                                    
        except ModelRegister.DoesNotExist:
            messages.error(request,'This email is not registered yet!.')
            print('email doesnot exist')
            return redirect('login')
        
    return render(request,'login.html')

def register_views(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            send_mail(
                subject='Registration successful.',
                message=f"""Hello {user.ownerName},\n
                Thankyou for registering with us.Your account has been created successfully.
                You can now log in and start using our services.
                Best regards.""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )
            print('Registration successfull')
            return redirect("seller")
    else:
        form = RegisterForm()
        
    return render(request,'register_view.html',{'form': form})

def product(request):
    if request.method == 'POST':
        form =ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("product added successfully")
            messages.success (request,"product added successfully")
        else:
            messages.error(request,"you have an error")
    else:
        form =ProductForm()

    return render(request,'product.html',{'form':form})

def seller(request):
    return render(request,'seller_dashboard.html')

def seller_header(request):
    return render(request,'seller_header.html')

