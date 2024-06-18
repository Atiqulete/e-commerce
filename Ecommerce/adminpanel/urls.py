from django.urls import path
from adminpanel import views


urlpatterns = [
    path('adminpanel',views.index,name='admin'),
    path('login',views.login_page,name='login_page'),
    path('reg',views.reg_page,name='reg_page'),
    path('logout_user',views.logout_page,name='logout_user'),
    path('change_password',views.change_pass,name='change_password'),
    #=====================slider================================================
    path('add_slider',views.create_slider,name='add_slider'),
    path('slider_info_edit/<int:id>',views.edit_slider,name='slider_info_edit'),
    path('update_slider/<int:id>',views.update_slider,name='update_slider'),
    path('slider_delete/<int:id>',views.delete_slider,name='slider_delete'),
    path('trush',views.trush_slider,name='trush'),
    path('restore/<int:id>',views.restore_slider,name='restore'),
    path('delete_all',views.delete_all,name='delete_all'),
    path('del_permanent/<int:id>',views.del_permanent,name='del_permanent'),
    #=====================cattegory============================================
    path('add_category',views.category_store,name='add_category'),
    path('cat_show',views.cat_show,name='cat_show'),
    path('cat_info_edit/<int:id>',views.edit_cat,name='cat_info_edit'),
    path('update_cat/<int:id>',views.update_cat,name='update_cat'),
    path('cat_delete/<int:id>',views.delete_cat,name='cat_delete'),
    #=====================Product===============================================
    path('product_store',views.product_store,name='product_store'),
    path('product/show',views.product_show,name='product/show'),
    path('pro_info_edit/<int:id>',views.edit_product,name='pro_info_edit'),
    path('update_pro/<int:id>',views.update_product,name='update_pro'),
    path('delete_pro/<int:id>',views.delete_pro,name='delete_pro'),
    
    path('product_details/<int:id>',views.product_details,name='product_details'),
    


]