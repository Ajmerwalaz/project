from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import *
import random
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
import uuid
# Create
def blog_details(request):
    cid=category.objects.all().order_by("-id")
    uid=user.objects.get(name=request.session['name'])
    wid_count=wishlist.objects.filter(user=uid).count()
    cid_count=Cart.objects.filter(user=uid,order_status=False).count()
    shop_items = Cart.objects.filter(user=uid,order_status=False).select_related('product')
    l1 = [i.total_price for i in shop_items]
    sub_total = sum(l1)
    shipping = 0 if sub_total == 0 or sub_total > 99 else 20
    total = sub_total + shipping
    contaxt={
            "cid":cid,
            "wid_count": wid_count,
            "cid_count": cid_count,
            "uid":uid,
            "shop_items": shop_items,
            "sub_total": sub_total,
            "shipping": shipping,
            "total": total,
        }
    
    return render(request, 'blog_details.html', contaxt)

def blog(request):
    cid=category.objects.all().order_by("-id")
    uid=user.objects.get(name=request.session['name'])
    wid_count=wishlist.objects.filter(user=uid).count()
    cid_count=Cart.objects.filter(user=uid,order_status=False).count()
    shop_items = Cart.objects.filter(user=uid,order_status=False).select_related('product')
    l1 = [i.total_price for i in shop_items]
    sub_total = sum(l1)
    shipping = 0 if sub_total == 0 or sub_total > 99 else 20
    total = sub_total + shipping
    contaxt={
            "cid":cid,
            "wid_count": wid_count,
            "cid_count": cid_count,
            "uid":uid,
            "shop_items": shop_items,
            "sub_total": sub_total,
            "shipping": shipping,
            "total": total
        }
    return render(request, 'blog.html', contaxt)

def checkout(request):
    cid=category.objects.all().order_by("-id")
    uid=user.objects.get(name=request.session['name'])
    wid_count=wishlist.objects.filter(user=uid).count()
    cid_count=Cart.objects.filter(user=uid,order_status=False).count()
    cart_items = Cart.objects.filter(user=uid,order_status=False).select_related('product')
    l1 = [i.total_price for i in cart_items]

    subtotal = sum(item.total_price for item in cart_items)
    shipping = 0 if subtotal > 99 else 20
    total = subtotal + shipping

    contaxt={
            "cid":cid,
            "uid":uid,
            "wid_count": wid_count,
            "cid_count": cid_count,
            "cart_items": cart_items,
            "subtotal": subtotal,
            "shipping": shipping,
            "total": total,
        }
    return render(request, 'checkout.html', contaxt)

def contact(request):
    cid=category.objects.all().order_by("-id")
    uid=user.objects.get(name=request.session['name'])
    wid_count=wishlist.objects.filter(user=uid).count()
    cid_count=Cart.objects.filter(user=uid,order_status=False).count()
    shop_items = Cart.objects.filter(user=uid,order_status=False).select_related('product')
    l1 = [i.total_price for i in shop_items]
    sub_total = sum(l1)
    shipping = 0 if sub_total == 0 or sub_total > 99 else 20
    total = sub_total + shipping

    # ✅ Handle form submission
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to model
        contact_us.objects.create(
            name=name,
            email=email,
            message=message
        )
        messages.success(request, "Your message has been sent!")
    contaxt={
            "cid":cid,
            "wid_count": wid_count,
            "cid_count": cid_count,
            "uid":uid,
            "shop_items": shop_items,
            "sub_total": sub_total,
            "shipping": shipping,
            "total": total
        }
    return render(request, 'contact.html', contaxt)

def index(request):
    if "name" in request.session:
        uid=user.objects.get(name=request.session['name'])
        cid=category.objects.all().order_by("-id")
        wishlist_items = []
        wishlist_items = wishlist.objects.filter(user=uid).values_list('product_id', flat=True)
        wid_count=wishlist.objects.filter(user=uid).count()
        cid_count=Cart.objects.filter(user=uid,order_status=False).count()
        search_query = request.GET.get('query')
        pid = product.objects.all().order_by("-id")
        shop_items = Cart.objects.filter(user=uid,order_status=False).select_related('product')
        l1 = [i.total_price for i in shop_items]
        sub_total = sum(l1)
        shipping = 0 if sub_total == 0 or sub_total > 99 else 20
        total = sub_total + shipping
        # Handle category filter
        cate = request.GET.get("cate")
        if cate:
            pid = pid.filter(category=cate)
        
        # Pagination
        pagination = Paginator(pid, 2)
        page = request.GET.get("page")
        pid = pagination.get_page(page)

        if search_query:
            pid = pid.filter(name__icontains=search_query)       
        contaxt={
            "cid":cid,
            "uid":uid,
            "pid": pid,
            "wishlist_items": wishlist_items,
            "wid_count": wid_count,
            "cid_count": cid_count,
            "search_query": search_query,
            "shop_items": shop_items,
            "sub_total": sub_total,
            "shipping": shipping,
            "total": total
        }
        return render(request, 'index.html' , contaxt)
    else:
        return redirect(login)

def main(request):
    return render(request, 'main.html')

def shop_details(request):
    cid=category.objects.all().order_by("-id")
    uid=user.objects.get(name=request.session['name'])
    wid_count=wishlist.objects.filter(user=uid).count()
    cid_count=Cart.objects.filter(user=uid,order_status=False).count()
    pid = product.objects.all().order_by("-id")
    shop_items = Cart.objects.filter(user=uid,order_status=False).select_related('product')
    l1 = [i.total_price for i in shop_items]
    sub_total = sum(l1)
    shipping = 0 if sub_total == 0 or sub_total > 99 else 20
    total = sub_total + shipping

    contaxt={
            "cid":cid,
            "wid_count": wid_count,
            "cid_count": cid_count,
            "pid": pid,
            "uid":uid,
            "shop_items": shop_items,
            "sub_total": sub_total,
            "shipping": shipping,
            "total": total
        }
    return render(request, 'shop_details.html',contaxt)

def shop_grid(request):
    cid = category.objects.all().order_by("-id")
    uid=user.objects.get(name=request.session['name'])
    wid_count=wishlist.objects.filter(user=uid).count()
    cid_count=Cart.objects.filter(user=uid,order_status=False).count()
    wishlist_items = []
    shop_items = Cart.objects.filter(user=uid,order_status=False).select_related('product')
    l1 = [i.total_price for i in shop_items]
    sub_total = sum(l1)
    shipping = 0 if sub_total == 0 or sub_total > 99 else 20
    total = sub_total + shipping
    
    # Get wishlist items if user is logged in
    if 'name' in request.session:
        uid = user.objects.get(name=request.session['name'])
        wishlist_items = wishlist.objects.filter(user=uid).values_list('product_id', flat=True)
    
    # Get price filter parameters
    min_price = request.GET.get('min_price', '').replace('$', '')
    max_price = request.GET.get('max_price', '').replace('$', '')
    # Base queryset
    pid = product.objects.all().order_by("-id")
    
    # Apply price filter if provided
    if min_price and max_price:
        try:
            min_price = float(min_price)
            max_price = float(max_price)
            pid = pid.filter(price__gte=min_price, price__lte=max_price)
        except (ValueError, TypeError):
            pass
    
    # Handle category filter
    cate = request.GET.get("cate")
    if cate:
        pid = pid.filter(category=cate)
    
    # Pagination
    pagination = Paginator(pid, 2)
    page = request.GET.get("page")
    pid = pagination.get_page(page)

    context = {
        "cid": cid,
        "pid": pid,
        "uid":uid,
        "wid_count": wid_count,
        "cid_count": cid_count,
        "wishlist_items": wishlist_items,
        "min_price": min_price if min_price else 10,
        "max_price": max_price if max_price else 540,
        "shop_items": shop_items,
        "sub_total": sub_total,
        "shipping": shipping,
        "total": total
    }
    return render(request, "shop_grid.html", context)

# def shoping_cart(request):
#     cid=category.objects.all().order_by("-id")
#     contaxt={
#             "cid":cid
#         }
#     return render(request, 'shoping_cart.html' , contaxt)

def shoping_cart(request):
    # Check if user is logged in
    if 'name' not in request.session:
        return redirect('login')

    # Get user instance
    uid=user.objects.get(name=request.session['name'])
    wid_count=wishlist.objects.filter(user=uid).count()
    cid_count=Cart.objects.filter(user=uid,order_status=False).count()
    pid = product.objects.all().order_by("-id")


    # Get cart items for the user, including related product
    shop_items = Cart.objects.filter(user=uid,order_status=False).select_related('product')
    l1=[i.total_price for i in shop_items]
    sub_total=sum(l1)
    if sub_total == 0:
        shipping=0
    elif sub_total > 99:
        shipping=0
    else:
        shipping=20
    total=sub_total+shipping
    # Get categories
    cid = category.objects.all().order_by("-id")

    # Prepare context for the template
    context = {
        "cid": cid,
        "uid":uid,
        "pid": pid,
        "wid_count": wid_count,
        "cid_count": cid_count,
        "shop_items": shop_items,
        "sub_total": sub_total,
        "shipping": shipping,
        "total": total,

    }

    return render(request, "shoping_cart.html", context)

def register(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print(name,email,password1,password2)
        uid=user.objects.filter(email=email).exists()
        user_uid=user.objects.filter(name=name).exists()
        print(uid)
        if user_uid:
            contaxt={
                "msg":"name already exist"
            }
            return render(request, 'register.html',contaxt)
        elif uid:
            contaxt={
                "msg":"Email already registered"
            }
            return render(request, 'register.html',contaxt)
        else:
            if password1 == password2:
                user.objects.create(name=name,email=email,password=password1)
                return render(request, 'register.html')
            else:
                contaxt={
                    "msg":"Password Not match"
                }
                return render(request, 'register.html',contaxt)
    return render(request, 'register.html')

def login(request):
    if "name" in request.session:
        return redirect(index)
    else:
        if request.POST:
            name=request.POST['name']
            password=request.POST['password1']
            print(name,password)
            user_uid=user.objects.filter(name=name).exists()
            if user_uid:
                user_uid=user.objects.get(name=name)
                if user_uid.password == password:
                    request.session["name"]=user_uid.name
                    return redirect(index)
                else:
                    contaxt={
                            "msg":"Incorrect password"
                        }
                    return render(request,"login.html",contaxt)
            else:
                contaxt={
                        "msg":"User Not exists"
                    }
                return render(request,"login.html",contaxt)
    return render(request,"login.html")

def logout(request):
    del request.session['name']
    return redirect(login)

def profile(request):
    uid=user.objects.get(name=request.session['name'])
    print(uid)
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        if request.FILES:
            image=request.FILES['image']
            uid.name=name
            uid.email=email
            uid.phone_number=phone_number
            uid.image=image
            uid.save()
        else:
            uid.name=name
            uid.email=email
            uid.phone_number=phone_number
            uid.save()
        request.session["name"]=uid.name
    con={
        "uid":uid
    }
    return render(request, 'profile.html',con)

def f_password(request):
    if request.POST:
        email=request.POST['email']
        otp=random.randint(1000,9999)
        print(email)
        uid=user.objects.filter(email=email).exists()
        if uid:
            send_mail("Ogani Reset password",f"Your OTP for reset password is: {otp}","naman6865@gmail.com",[email])
            uid=user.objects.get(email=email)
            uid.otp=otp
            uid.save()
            con={
                "uid":uid
            }
            return render(request, 'confirm_password.html',con)
        else:
            con={
                "msg":"Invalid Email"
            }
            return render(request, 'f_password.html',con)

    return render(request, 'f_password.html')

def confirm_password(request):
    if request.method == 'POST':
        email=request.POST['email']
        otp=request.POST['otp']
        new_password=request.POST['new_password']
        confirm_password1=request.POST['confirm_password']
        print(email,otp,new_password,confirm_password)
        uid=user.objects.get(email=email)
        print(type(uid.otp),type(otp))
        if uid.otp == int(otp):
            print("okokok")
            if new_password == confirm_password1:
                uid.password=new_password
                uid.save()
                return redirect(login)
            else:
                contaxt={
                    "msg":"Password Not match",
                    "uid":uid
                }
                return render(request, 'confirm_password.html',contaxt)
        else:
            contaxt={
                "msg":"Invalid OTP",
                "uid":uid
            }
            return render(request, 'confirm_password.html',contaxt)    
    else:
        return render(request,"confirm_password.html")
    
def search_fun(request):
    search=request.GET.get('search')
    print("abcd",search)
    pid=product.objects.filter(name__contains=search)
    contaxt={
        "pid":pid
    }
    return render(request,"shop_grid.html",contaxt)

def add_wishlist(request, id):
    if 'name' not in request.session:
        return redirect('login')  # Not logged in

    uid=user.objects.get(name=request.session['name'])
    pid = product.objects.filter(id=id).first()

    existing = wishlist.objects.filter(user=uid, product=pid)
    if existing.exists():
        existing.delete()  # Remove from wishlist
    else:
        wishlist.objects.create(user=uid, product=pid)  # Add to wishlist

    # return redirect('shop_grid')  # Or use request.META.get('HTTP_REFERER') to go back to same page
    referer = request.META.get('HTTP_REFERER', '')
    if 'wishlists' in referer:
        return redirect('wishlists')  # your wishlist page URL name
    else:
        return redirect('shop_grid')  # fallback if not from wishlist

# Show wishlist page
def wishlists(request):
    if 'name' not in request.session:
        return redirect('login')

    uid=user.objects.get(name=request.session['name'])
    wid_count=wishlist.objects.filter(user=uid).count()
    cid_count=Cart.objects.filter(user=uid,order_status=False).count()
    wishlist_items = wishlist.objects.filter(user=uid).select_related('product')
    shop_items = Cart.objects.filter(user=uid,order_status=False).select_related('product')
    l1 = [i.total_price for i in shop_items]
    sub_total = sum(l1)
    shipping = 0 if sub_total == 0 or sub_total > 99 else 20
    total = sub_total + shipping
    context = {
        "uid":uid,
        "wid_count": wid_count,
        "cid_count": cid_count,
        "wishlist_items": wishlist_items,
        "shop_items": shop_items,
        "sub_total": sub_total,
        "shipping": shipping,
        "total": total
        
    }    
    return render(request, "wishlist1.html", context)

def add_cart(request, id):
    if 'name' not in request.session:
        return redirect('login')

    uid = user.objects.get(name=request.session['name'])
    pid = product.objects.filter(id=id).first()
    if not pid:
        return redirect('shop_grid')  # Handle invalid product ID

    existing = Cart.objects.filter(user=uid, product=pid,order_status=False).first()

    if existing:
        existing.quantity += 1
        existing.total_price = existing.quantity * pid.price
        existing.save()
    else:
        Cart.objects.create(user=uid, product=pid, quantity=1, total_price=pid.price)
    referer = request.META.get('HTTP_REFERER', '')
    if 'shoping_cart' in referer:
        return redirect('shoping_cart')
    else:
        return redirect('shop_grid')

def cart_plus(request,id):
    cid=Cart.objects.get(id=id)
    cid.quantity+=1
    cid.total_price=cid.product.price*cid.quantity
    cid.save()
    return redirect(shoping_cart)

def cart_minus(request,id):
    cid=Cart.objects.get(id=id)
    # cid.quantity-=1
    # cid.total_price=cid.product.price*cid.quantity
    # cid.save()
    # return redirect(shoping_cart)
    if cid.quantity > 1:
        cid.quantity -= 1
        cid.total_price = cid.quantity * cid.product.price
        cid.save()
    else:
        cid.delete()  # Remove from cart if quantity is 1 and user clicks minus

    return redirect('shoping_cart')

def remove_cart_item(request, id):
    if 'name' not in request.session:
        return redirect('login')

    uid = user.objects.get(name=request.session['name'])
    pid = product.objects.filter(id=id).first()
    
    cart_item = Cart.objects.filter(user=uid, product=pid).first()
    if cart_item:
        cart_item.delete()

    return redirect('shoping_cart')

def add_billing(request):

    if 'name' not in request.session:
        return redirect('login')


    uid = user.objects.get(name=request.session['name'])
    wid_count = wishlist.objects.filter(user=uid).count()
    cid_count = Cart.objects.filter(user=uid,order_status=False).count()
    cid = Cart.objects.filter(user=uid,order_status=False)
    subtotal=sum([i.total_price for i in cid])
    
    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        country = request.POST['country']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        phone_number = request.POST['phone_number']
        email = request.POST['email']

        Billing_Details.objects.create(
            user=uid,
            first_name=first_name,
            last_name=last_name,
            country=country,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            phone_number=phone_number,
            email=email
        )
        messages.success(request, "Billing details saved successfully.")
        latest_address=Billing_Details.objects.filter(user=uid).order_by("-id")[0]
        order_id = str(uuid.uuid4()).replace('-', '')[:12]
        oid=order.objects.create(user=uid,address=latest_address,subtotal=subtotal,total=subtotal,order_id=order_id)
        oid.product.set(cid)
        for i in cid:
            i.order_status=True
            i.save()

        return redirect('checkout')

    context = {
        "uid": uid,
        "wid_count": wid_count,
        "cid_count": cid_count
    }
    return render(request, 'checkout.html', context)

def order_detail(request):
    if 'name' not in request.session:
        return redirect('login')

    uid = user.objects.get(name=request.session['name'])
    orders = order.objects.filter(user=uid).order_by('-datetime')

    context = {
        "orders": orders,
    }
    return render(request, 'order_list.html', context)

def single_orders (request,id):
    uid = user.objects.get(name=request.session['name'])
    oid=order.objects.get(id=id)
    wid_count = wishlist.objects.filter(user=uid).count()
    cid_count = Cart.objects.filter(user=uid,order_status=False).count()
    shop_items = Cart.objects.filter(user=uid,order_status=False).select_related('product')
    l1 = [i.total_price for i in shop_items]
    sub_total = sum(l1)
    shipping = 0 if sub_total == 0 or sub_total > 99 else 20
    total = sub_total + shipping
    
    con={
        "oid":oid,
        "uid":uid,
        "wid_count":wid_count,
        "cid_count":cid_count,
        "shop_items": shop_items,
        "sub_total": sub_total,
        "shipping": shipping,
        "total": total
    }
    return render (request, "single_order.html",con)