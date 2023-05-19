from django.urls import path
from . import views

app_name = 'marketplace'

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("product/<int:prod_id>/", views.products, name='product'),
    path("cart/", views.cart, name='cart'),
    path("checkout/", views.checkout, name='checkout'),
    path("wishlist/", views.wishlist, name='wishlist')
]