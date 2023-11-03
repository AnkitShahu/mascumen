from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('product/', views.product, name='product'),
    path('<slug>/', views.product, name="product_details")
]