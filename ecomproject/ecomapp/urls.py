from django.urls import path
from .views import *
from .views import AllProductView
app_name = "ecomapp"
urlpatterns = [
    path("", HomeView.as_view(),name="home"),
    path("about/",AboutView.as_view(),name="about"),
    path("contact-us/",ContactView.as_view(),name="contact"),
    path("all-products/",AllProductView.as_view(),name="all products"),
    path("product/<slug:slug>/",ProductDetailView.as_view(),name="productdetail"),

    path("add-to_cart-<int:pro_id>/",AddToCartView.as_view(),name="addtocart"),
    path("my-cart/",MyCartView.as_view(),name="mycart"),
    path("manage_cart/<int:cp_id>",ManageCartView.as_view(),name="managecart"),
    path("empty-cart/",EmptyCartView.as_view(), name="emptycart"),
    path("checkout/",CheckoutView.as_view(),name="checkout"),

    path("register/",
         CustomerRegistrationView.as_view(), name="customerregistration"),
    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),     
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),  
    path("profile/",CustomerProfileView.as_view(),name="customerprofile"),
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(),
         name="customerorderdetail"),
    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),     
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(),
         name="adminorderdetail"),

    path("admin-all-orders/", AdminOrderListView.as_view(), name="adminorderlist"),
    path("search/", SearchView.as_view(), name="search"),
    path("admin-order-<int:pk>-change/",AdminOrderStatusChangeView.as_view(), name="adminorderstatuschange")

]
