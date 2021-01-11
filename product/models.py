from django.db import models
import random,os
from django.db.models import CASCADE

# Create your models here.

class Brand(models.Model):
	brand_name=models.CharField(max_length=80,unique=True)
	
	def __str__(self):
		return self.brand_name


class Catagory(models.Model):
	add_catagory=models.CharField(max_length=100)
	catagory_image=models.ImageField(null=True,blank=True)
	
	def __str__(self):
		return self.add_catagory



	

def get_filename_ext(filepath):
	base_name=os.path.basename(filepath)
	name,ext=os.path.splitext(base_name)
	return name,ext

def upload_image_path(instance,filename):
	new_filename=random.randint(1,99999999999999)
	name,ext=get_filename_ext(filename)
	final_filename=f"{new_filename}{ext}"
	return 'myproducts-'+f"{new_filename}/{final_filename}"


class Products(models.Model):
	title=models.CharField(max_length=80)
	description=models.TextField(max_length=1000)
	price=models.CharField(max_length=80,blank=False)
	image=models.ImageField(null=True,blank=True,upload_to=upload_image_path)
	brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
	weight=models.CharField(max_length=80)
	warranty=models.CharField(max_length=80)
	model_number=models.CharField(max_length=80)
	mfgdate=models.DateField(blank=True,null=True)
	#category=models.ForeignKey(Catagory,on_delete=CASCADE,default=1)




	def __str__(self):
		return self.title+","+self.description+","+self.brand.brand_name+","+self.price+","+self.weight+","+self.warranty+","+self.model_number+","+self.mfgdate







	