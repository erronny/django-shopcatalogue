from django.urls import path
from front import views

urlpatterns = [
    path('registeruser/', views.register_user),
    path('loginuser/', views.loginuser),
    path('home/',views.home),
	path('success/',views.success),
	path('Logout/',views.logout),
	path('unsuccessfull/',views.unsuccessfull),
   
]