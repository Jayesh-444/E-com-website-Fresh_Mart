from django.shortcuts import render,redirect
from app.models import Product,Categories,order,User
from django.contrib.auth.decorators import login_required 
from cart.cart import Cart


def MASTER(request):
    return render(request, 'main/master.html')




def INDEX(request):
    return render(request, 'main/index.html')


def ABOUT(request):
    return render(request, 'about.html')



def SHOP(request):
    products = Product.objects.filter(status = 'Publish') 
    categories = Categories.objects.all()

    cat_id = request.GET.get('Categories')

    if cat_id:
        products = Product.objects.filter(category=cat_id, status='Publish')

    else:
        products = Product.objects.filter(status='Publish')

    context = { 
        'Categories': categories,
        'products': products
    }
    return render(request, 'shop.html',context)




def GALLERY(request):
    return render(request, 'gallery.html')


def CONTACT_US(request):
    return render(request, 'contact-us.html')


@login_required(login_url='/login/')
def CHECKOUT(request):
    return render(request, 'checkout.html')


@login_required(login_url='/login/')
def MYACCOUNT(request):
    return render(request, 'my-account.html')


@login_required(login_url='/login/')
def WISHLIST(request):
    return render(request, 'wishlist.html')









@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'cart.html')




@login_required(login_url="/login/")
def place_order(request):
    if request.method == "POST":
        user = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        zip = request.POST.get('zip')
        state = request.POST.get('state')
        country = request.POST.get('country')
        amount = request.POST.get('amount')
        
        # Create and save the order
        Order = order(
            user=user,
            firstname=firstname,
            lastname=lastname,
            email=email,
            username=username,
            address1=address1,
            address2=address2,
            zip=zip,
            state=state,
            country=country,
            amount=amount,
        )
        Order.save()  # Save the order to the database

        return render(request, 'place_order.html', {'user': user, 'order': Order})

    return render(request, 'place_order.html')
