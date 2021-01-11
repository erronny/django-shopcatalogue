from django.shortcuts import render
from .models import Products,Catagory

# Create your views here.

def product(request):
	products= Products.objects.all()
	context = {'title':"product page",
				'products':products
				}
	return render(request,'product/product_list.html',context)

def productdetails(request,id):
	products= Products.objects.get(id=id)

	context = {'title':"product page",
				'product':products
				}
	return render(request,'product/productdetails.html',context)