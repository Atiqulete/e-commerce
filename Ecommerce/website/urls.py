from django.urls import path
from website import views


urlpatterns = [
path('',views.index,name='home'),
path('product_by_cat/<int:id>',views.show_product_by_cat,name='product_by_cat'),
path('product_details_website/<int:id>',views.product_details_website,name='product_details'),
path('shop',views.shop,name='shop'),
path('search',views.search,name='search'),
path('customer_reg',views.customer_signup,name='customer_reg'),
path('customer_login',views.customer_login,name='customer_login'),
path('customer_logout',views.customer_logout,name='customer_logout'),
path('wish_list/<int:id>',views.add_to_wish,name='wish_list'),
path('wish_details',views.wish_detalis,name='wish_details'),
path('wish_remove/<int:id>',views.wishlist_remove,name='wish_remove'),
path('add_to_cart/<int:poduct_id>',views.add_to_cart,name='add_to_cart'),
path('view_cart',views.view_cart,name='view_cart'),
path('del_cart/<int:poduct_id>',views.delete_cart,name='del_cart'),

]