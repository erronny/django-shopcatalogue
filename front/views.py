from django.shortcuts import render,redirect
from .forms import UserProfileModelForm,UserLoginForm
from .models import UserProfiles
from product.models import Catagory

# Create your views here.

def register_user(request):
	form=UserProfileModelForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('/loginuser')
		else:
			return redirect('/loginuser')


	context ={
	'form':form,
	'title':'User Registration',
	}
	return render(request,'front/registeruser.html',context)

def loginuser(request):
	form=UserLoginForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			try:
				user = UserProfiles.objects.get(email=email,password=password)
				request.session['email']=email
				return redirect('/success')
			except:
				return redirect('/unsuccessfull')
	context = {'form':form,
				'title':'login'}
	return render(request,'front/loginuser.html',context)


def success(request):
    return render(request,'front/success.html')		
def unsuccessfull(request):
    return render(request,'front/unsuccessfull.html')

def logout(request):
    return redirect('/home')


def home(request):
	objects=Catagories.objects.all()
	context={
	
	'title':'home',
	'object':objects,

	}
	return render(request,'front/home.html',context)