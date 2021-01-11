from django.urls import path
from product import views


urlpatterns = [
    path('product/', views.product),
    path('productdetails/<id>', views.productdetails),

   
]