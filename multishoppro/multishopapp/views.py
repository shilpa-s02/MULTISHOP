from django.shortcuts import render,redirect
from .forms import ProductForm,RegisterForm,CheckoutForm
from .models import products,ModelRegister
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
# Create your views here.
def index(request):
    return render(request,'index.html')

def shop(request):
    form = products.objects.all()
    return render(request,'shop.html',{'form':form})


#add product to cart
def detail(request,pk):
    product= products.objects.get(id=pk)

    if request.method =='POST':
        cart = request.session.get('cart',{})
        product_id = str(product.id)
        quantity =int(request.POST.get('quantity',1))

        #add or update product in cart
        if product_id in cart:
            cart[product_id]['quantity'] += quantity
        else:
            cart[product_id] ={
                'productName':product.productName,
                'price':float(product.price),
                'image':product.image.url if product.image else '',
                'quantity': quantity,
            }
        request.session['cart'] = cart
        request.session.modified =True

        return redirect('cart')
    return render(request,'detail.html',{'product':product})


#to add product to cart
def cart(request):
    cart = request.session.get('cart',{})
    count = sum(item['quantity'] for item in cart.values())
    cart_items =[]
    total = 0
    for item in cart.values():
        item_total = item['price'] * item['quantity']
        total += item_total
        cart_items.append({
            #  use .get() to avoid keyerror
            'id':item.get('id') ,
            'productName': item['productName'],
            'price': item['price'],
            'image': item['image'],
            'quantity': item['quantity'],
            'total': item_total,
        })

    return render(request,'cart.html',{
        'cart_count':count,
        "cart_items":cart_items,
        'cart_total':total,
        'cart':cart,
        })


#remove from cart
def remove_from_cart(request):
    if request.method == 'POST':
        product_id = str(request.POST.get('product_id'))
        cart= request.session.get('cart',{})
        if product_id in cart:
            del cart[product_id]
            request.session['cart'] =cart
            request.session.modified =True
            print("Removed!")

    return redirect('cart')
                                  

def checkout(request):
    
    cart = request.session.get('cart', {})
    cart_items = []
    cart_subtotal = 0
    shipping_cost = 10

    for item in cart.values():
        item_total = item['price'] * item['quantity']
        cart_subtotal += item_total
        cart_items.append({
            'product': {'name': item['productName']},
            'total_price': item_total,
        })

    cart_total = cart_subtotal + shipping_cost

    # OTP verification step
    if request.method == 'POST':
        if 'otp' in request.POST:
            user_otp = request.POST.get('otp')
            session_otp = request.session.get('checkout_otp')
            if user_otp == session_otp:
                # OTP correct, save the order
                form = CheckoutForm(request.session.get('checkout_form_data'))
            if form.is_valid():
                order = form.save()
                # Send order placed email
                send_mail(
                    'Order Placed Successfully',
                    # 'Thank you for shopping with us! Your order has been placed successfully.',
                    # 'Our team is now processing it.',
                    'Thankyou for choosing us.',
                    'noreply@example.com',
                    [order.email],  # Make sure your CheckoutForm/model has an 'email' field
                    fail_silently=False,
                )
                del request.session['checkout_otp']
                del request.session['checkout_form_data']
                print("order placed successfully")
                return redirect('index')  # Redirect to a success page or home page
            else:
                form = CheckoutForm(request.session.get('checkout_form_data'))
                return render(request, 'checkout.html', {
                    'form': form,
                    'cart_items': cart_items,
                    'cart_subtotal': cart_subtotal,
                    'shipping_cost': shipping_cost,
                    'cart_total': cart_total,
                    'otp_error': 'Invalid OTP. Please try again.',
                    'show_otp': True,
                })
        else:
            form = CheckoutForm(request.POST)
            if form.is_valid():
                # Generate OTP
                otp = str(random.randint(100000, 999999))
                email = form.cleaned_data.get('email')
                # Send OTP to email
                send_mail(
                    'Your Checkout OTP',
                    f'Your OTP for checkout is: {otp}',
                    'noreply@example.com',
                    [email],
                    fail_silently=False,
                )
                # Store OTP and form data in session
                request.session['checkout_otp'] = otp
                request.session['checkout_form_data'] = request.POST
                
                return render(request, 'checkout.html', {
                    'form': form,
                    'cart_items': cart_items,
                    'cart_subtotal': cart_subtotal,
                    'shipping_cost': shipping_cost,
                    'cart_total': cart_total,
                    'show_otp': True,
                    'info': 'An OTP has been sent to your email. Please enter it below to complete your order.',
                })
            print("otp send successfully")
                
    else:
        form = CheckoutForm()
        

    return render(request, 'checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'cart_subtotal': cart_subtotal,
        'shipping_cost': shipping_cost,
        'cart_total': cart_total,
    })
    

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

#to add new product by seller
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

def new(request):
    return render(request,'new.html')

