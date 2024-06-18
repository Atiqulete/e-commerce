from django.shortcuts import render,redirect,HttpResponse
from adminpanel.models import category,product,product_img,slider
from website.models import customer,wishlist
from django.db.models import Q
from django.contrib.auth.hashers import make_password,check_password



def wish_counter(request):
    if request.session.has_key('customer_login'):
        wish_list_count = wishlist.objects.filter(customer_id_id = request.session['customer_login']).count()
        # wish_list_couter = {'wish_list_count':wish_list_count}
        return wish_list_count
    else:
        wish_list_count = 0
        return wish_list_count

def index(request):
    cat_name = category.objects.all()
    slider_info = slider.objects.all()
    a = wish_counter(request)

    context = {
       'cat_name' : cat_name,
       'wish_list_count' : a,
       'slider_info': slider_info
    }
    return render(request,'website/index.html',context)

def show_product_by_cat(request,id):
    cat_name = category.objects.all()
    product_by_cat = product.objects.filter(product_category_id=id).prefetch_related('prod')
    a = wish_counter(request)
    context = {
       'cat_name' : cat_name,
       'product_by_cat' : product_by_cat,
       'wish_list_count' : a
    }
    return render(request,'website/product_by_cat.html',context)

def product_details_website(request,id):
    cat_name = category.objects.all()
    product_details = product.objects.filter(id=id).prefetch_related('prod')
    a = wish_counter(request)
    context = {
        'cat_name' : cat_name,
        'product_details' : product_details,
        'wish_list_count' : a
    }
    return render(request,'website/product_details.html',context)

def shop(request):
    cat_name = category.objects.all()
    product_all = product.objects.all()
    a = wish_counter(request)

    context = {
        'cat_name' : cat_name,
        'product_all' : product_all,
        'wish_list_count' : a
    }
    return render(request,'website/product_shop.html',context)

def search(request):
    if request.method == 'GET':
        p_search = request.GET.get('p_search')
        if p_search != None:
            product_search = product.objects.filter(Q(product_name__icontains = p_search) | Q(product_new_price__icontains = p_search))
        else:
            HttpResponse('NOT FOUND')
    context = {
       'product_search' : product_search
    }
    return render(request,'website/product_search.html',context)

def customer_signup(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        pass_1 = request.POST.get('password')
        pass_2 = request.POST.get('password_2')

        if pass_1 == pass_2:
            customer_reg = customer(
                username = username,
                email = email,
                mobile = mobile,
                password = make_password(pass_1)
            )
            customer_reg.save()
            return redirect('customer_login')
    return render(request,'website/reg.html')

def customer_login(request):
    if request.method == 'POST':
        x = request.POST.get('name')
        y = request.POST.get('password')

        abcd = customer.customer_check(x)

        if abcd:
            psw = check_password(y,abcd.password)
            if psw:
                request.session['customer_login'] = abcd.id
                return redirect('home')
            else:
                return redirect('customer_login')
        else:
            return redirect('customer_login')  
    return render(request,'website/login.html')

def customer_logout(request):
    try:
        del request.session['customer_login']
    except:
        pass
    return redirect('home')
 
def add_to_wish(request,id):
    if request.session.has_key('customer_login'):
        wish_list = wishlist(
            product_id_id = id,
            customer_id_id = request.session.get('customer_login',id)
        )
        wish_list.save()
        return redirect('shop')
    else:
        return redirect('customer_login')

def wish_detalis(request):
    if request.session.has_key('customer_login'):
        wish_list = wishlist.objects.filter(customer_id_id = request.session['customer_login'])
        return render(request,'website/wishlist.html',{'wish_list':wish_list})
    else:
        return redirect('customer_login')
    
def wishlist_remove(request,id):
    if request.session.has_key('customer_login'):
        wish_list = wishlist.objects.filter(customer_id_id = request.session['customer_login']).filter(id=id)
        wish_list.delete()
        return redirect('wish_details')
    else:
        return redirect('customer_login')

def add_to_cart(request,poduct_id,quantity=1):
    cart = request.session.get('cart',{})

    quantity = int(request.POST.get('quantity',1))
    cart[poduct_id] = cart.get(poduct_id,0) + quantity
    request.session['cart'] = cart

    return redirect('shop')

def view_cart(request):
    cart = request.session.get('cart',{})
    cart_item = []

    for poduct_id,quantity in cart.items():
        products = product.objects.get(id=poduct_id)
        total_price = sum(i['products'].product_new_price * i['quantity'] for i in cart_item )
        cart_item.append({'products':products,'quantity':quantity,'total_price':total_price})
    return render(request,'website/cart.html',{'cart_item':cart_item})

def delete_cart(request,poduct_id):
    cart = request.session.get('cart',{})
    pd_id = str(poduct_id)
    del request.session['cart'].pd_id
    request.session['cart'] = cart
    return redirect('view_cart')