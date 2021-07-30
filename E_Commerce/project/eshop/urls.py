from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="Home"),
    path('about/',views.about,name="About"),
    path('contact/',views.contact,name="Contact"),
    path('tracker/',views.tracker,name="TrackingStatus"),
    path('search/',views.search,name="Search"),
    path('productview',views.productView,name="ProductView"),
    path('checkout',views.checkout,name="Checkout"),   
]