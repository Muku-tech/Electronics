from django.urls import path
from .views import *
from .views import AllProductView
app_name = "ecomapp"
urlpatterns = [
    path("home/", HomeView.as_view(),name="home"),
    path("about/",AboutView.as_view(),name="about"),
    path("contact-us/",ContactView.as_view(),name="contact"),
    path("all-products/",AllProductView.as_view(),name="all products"),
    path("product/<slug:slug>/",ProductDetailView.as_view(),name="productdetail"),

    path("add-to_cart-<int:pro_id>/",AddToCartView.as_view(),name="addtocart"),
    path("my-cart/",MyCartView.as_view(),name="mycart"),
    path("manage_cart/<int:cp_id>",ManageCartView.as_view(),name="managecart"),
    path("empty-cart/",EmptyCartView.as_view(), name="emptycart"),
    path("checkout/",CheckoutView.as_view(),name="checkout"),

    path("register/",CustomerRegistration.as_view(),name="customerregistration"),
]
