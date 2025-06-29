from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path("",views.index,name='index'),
    path("shop/",views.shop,name='shop'),
    path("detail/<int:pk>/",views.detail,name='detail'),
    path("cart/",views.cart,name='cart'),
    path("checkout/",views.checkout,name='checkout'),
    path("contact/",views.contact,name='contact'),
    # path("product",views.add_product,name='add_product'),
    path("fashion/",views.fashion,name='fashion'),
    path("login/",views.login_view,name='login'),
    path("register_view/",views.register_views,name='register_now'),
    path("product/",views.product,name='product'),
    path("seller/",views.seller,name='seller'),
    path("sellerheader/",views.seller_header,name='seller_header'),
    path("new/",views.new,name='new'),
    path("remove_from_cart/",views.cart,name="remove_from_cart"),
]