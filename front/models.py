from django.db import models

# Create your models here.
class City(models.Model):
	cityname=models.CharField(max_length=80,unique=True)



	def __str__(self):
		return self.cityname


class UserProfiles(models.Model):
	name=models.CharField(max_length=80)
	email=models.EmailField(max_length=80,unique = True)
	password=models.CharField(max_length=80)
	city=models.ForeignKey(City,on_delete=models.CASCADE)
	mobile=models.CharField(max_length=10,unique=True,blank=True,null=True)
	date_of_birth=models.DateField(max_length=15)
	profile_image=models.ImageField(null=True,blank=True)
	gender=models.CharField(choices=(('male','male'),('female','female'),('others','others')),max_length=20)
	address=models.TextField(default="bhopal")

	
	def __str__(self):
		return self.name+","+self.email+","+self.city.cityname+","+self.address+","+self.password+","+self.mobile+","+str(self.date_of_birth)



