from django.shortcuts import render,redirect,HttpResponse
from adminpanel.models import User,category,product,product_img,slider
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
import sweetify


def index(request):
    if request.user.is_authenticated:
        return render(request,'adminpanel/index.html')
    else:
        return redirect('login_page')
    
def reg_page(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        email = request.POST.get('email')
        password_1 = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        if password_1 != password_2:
            return redirect('reg_page')
        else:
            user_reg = User.objects.create_user(user_name,email,password_1)
            # user_reg.last_name = 'Islam'
            user_reg.save()
            return redirect('login_page')
    return render(request, 'adminpanel/reg.html')

def login_page(request):
    if request.method == 'POST':
         a = request.POST.get('name')
         b = request.POST.get('password')
         user = authenticate(username=a,password=b)
         user_type_check = User.objects.get(username = user)
        
         if user != None:   
            print(user_type_check.user_type.type_name) 
            if user_type_check.user_type.type_name == 'Admin':
                login(request,user)
            #  if request.user.user_type == 2:
            #  if User.objects.get(user_type_id = 1):
            #  if user_type_check.user_type.type_name =='Normal User':
            #  if user_type_check.user_type.type_name =='Admin':
            #     login(request,user)
                #  return HttpResponse('welcome To My Admin Palnel')
                return render(request,'adminpanel/index.html')
            else:
                return redirect('login_page')
         else:
             return redirect('login_page')
    return render(request, 'adminpanel/login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            old_pass = request.POST.get('old_pass')
            new_pass = request.POST.get('new_pass')
            confirm_pass = request.POST.get('confirm_pass')
            xyz = User.objects.get(id=request.user.id)
            if xyz.check_password(old_pass) and new_pass == confirm_pass:
                xyz.set_password(new_pass)
                xyz.save()
                update_session_auth_hash(request,xyz)
                return redirect('logout_user')
        return render(request,'adminpanel/change_pass.html')
    else:
        return redirect('login_page')

def category_store(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            cat_name= request.POST.get('cat_name')
            cat_img = request.FILES['cat_img']

            cat_store = category (
                 category_name = cat_name,
                 category_img = cat_img             
          )
            cat_store.save()
            sweetify.toast(request,'save category')
        return render(request,'adminpanel/category/add_category.html')
    else:
        return redirect('login_page')

def cat_show(request):
    if request.user.is_authenticated:
        category_show = category.objects.all()
        return render(request,'adminpanel/category/cat_show.html',{'category_show':category_show})
    else:
        return redirect('login_page')

def edit_cat(request,id):
    if request.user.is_authenticated:
        edit_cat = category.objects.filter(id=id)
        return render(request,'adminpanel/category/edit_cat.html',{'edit_cat':edit_cat})
    else:
        return redirect('add_category')

def update_cat(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            cat_name = request.POST.get('cat_name')
            cat_img = request.FILES['cat_img']
            cat_store = category.objects.filter(id=id)
            cat_store = category(
                id=id,
                category_name = cat_name,
                category_img = cat_img
            )
            cat_store.save()
            sweetify.toast(request,'category update')
        else:
            cat_name = request.POST.get('cat_name')
            cat_img_1 = request.POST.get('cat_img_1')

            cat_store = category.objects.filter(id=id)
            cat_store = category(
                id=id,
                category_name = cat_name,
                category_img = cat_img_1
            )
            cat_store.save()
            sweetify.toast(request,'category update')
        return render(request,'adminpanel/category/add_category.html')
    else:
        return redirect('cat_show')

def delete_cat(request,id):
    cat_del = category.objects.filter(id=id)
    cat_del.delete()
    sweetify.toast(request,'category delete')
    return redirect('cat_show')

def product_store(request):
    if request.user.is_authenticated:
        cat_name = category.objects.all()        
        if request.method == 'POST' and request.FILES:
            product_name= request.POST.get('product_name')
            product_old_price= request.POST.get('product_old_price')
            product_new_price= request.POST.get('product_new_price')
            product_cat = request.POST.get('product_cat')
            Product_iamge = request.FILES.getlist('product_pic')

            product_save = product(
                product_name =product_name,
                product_old_price = product_old_price,
                product_new_price = product_new_price,
                product_category_id = product_cat
            )
            product_save.save()
            product_id = product_save.id

            for i in Product_iamge:
                product_image_store = product_img(
                    product_Image_all = i,
                    product_table_id = product_id
                )
                product_image_store.save()
        return render(request,'adminpanel/Product/product_store.html',{'cat_name':cat_name})
    else:
        return redirect('login_page')

def product_show(request):
    if request.user.is_authenticated:
        product_show = product.objects.prefetch_related('prod')
        return render(request,'adminpanel/Product/product_show.html',{'product_show':product_show})
    else:
        return redirect('login_page')

def edit_product(request,id):
    if request.user.is_authenticated:
        cat_name = category.objects.all()
        edit_pro = product.objects.filter(id=id)
        return render(request,'adminpanel/Product/editpro_show.html',{'edit_pro':edit_pro,'cat_name':cat_name})
    else:
        return redirect('product_store')

def update_product(request,id):
    if request.user.is_authenticated: 
        if request.method == 'POST' and request.FILES:
            product_name= request.POST.get('product_name')
            product_old_price= request.POST.get('product_old_price')
            product_new_price= request.POST.get('product_new_price')
            product_cat = request.POST.get('product_cat')
            Product_iamge = request.FILES.getlist('product_pic')

            product_save = product(
                id = id,
                product_name =product_name,
                product_old_price = product_old_price,
                product_new_price = product_new_price,
                product_category_id = product_cat
            )
            product_save.save()
            product_id = id

            for i in Product_iamge:
                product_image_store = product_img(
                    product_Image_all = i,
                    product_table_id = product_id
                )
                product_image_store.save()
        return redirect('product/show')
    else:
        return redirect('login_page')

def delete_pro(request,id):
    pro_del = product.objects.filter(id=id)
    pro_del.delete()
    return redirect('product/show')

def product_details(request,id):
    if request.user.is_authenticated:
        product_show = product.objects.filter(id=id).prefetch_related('prod')
        return render(request,'adminpanel/Product/product_details.html',{'product_show':product_show})
    else:
        return redirect('login_page')

def create_slider(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            discount = request.POST.get('discount')
            description = request.POST.get('description')
            img = request.FILES['img']
            slider_save = slider(
                discount = discount,
                description = description,
                image = img
            )
            slider_save.save()
            # sweetify.success(request, 'You did it', text='Your Form has been Updated',persistent='Hell yeah')
            sweetify.toast(request,'save slider image')
        slider_show = slider.objects.filter(is_delete = 0)
        return render(request,'adminpanel/slider/add_slider.html',{'slider_show':slider_show})
    else:  
        return redirect('add_slider')
    
def edit_slider(request,id):
    if request.user.is_authenticated:
        edit_info = slider.objects.filter(id=id)
        return render(request,'adminpanel/slider/edit_slider.html',{'edit_info':edit_info})
    else:
        return redirect('add_slider')
    
def update_slider(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES:
            discount = request.POST.get('discount')
            description = request.POST.get('description')
            img = request.FILES['img']

            slider_store = slider.objects.filter(id=id)
            slider_store = slider(
                id=id,
                discount = discount,
                description = description,
                image = img
            )
            slider_store.save()
        else:
            discount = request.POST.get('discount')
            description = request.POST.get('description')
            img = request.POST.get('img_1')

            slider_store = slider.objects.filter(id=id)
            slider_store = slider(
                id=id,
                discount = discount,
                description = description,
                image = img
            )
            slider_store.save()
        return render(request,'adminpanel/slider/add_slider.html')
    else:
        return redirect('add_slider')
    
# def delete_slider(request,id):
#     slider_del = slider.objects.filter(id=id)
#     slider_del.delete()
#     return redirect('add_slider')

def delete_slider(request,id):
    slider_del = slider.objects.get(id=id)
    slider_del.is_delete = True
    slider_del.save()
    return redirect('add_slider')

def trush_slider(request):
    if request.user.is_authenticated:
        slider_show = slider.objects.filter(is_delete = 1)       
        return render(request,'adminpanel/slider/trush.html',{'slider_show':slider_show})
    else:
        return redirect('add_slider')

def restore_slider(request,id):
    slider_del = slider.objects.get(id=id)
    slider_del.is_delete = False
    slider_del.save()
    return redirect('trush')

def delete_all(request):
    del_sli = request.POST.getlist('slider_del')

    for i in del_sli:
        slider_all_del = slider(
            id = i 
        )
        slider_all_del.delete()
    return redirect('trush')

def del_permanent(request,id):
    parmanent_del_trush = slider.objects.get(id=id)
    parmanent_del_trush.delete()
    return redirect('trush')







