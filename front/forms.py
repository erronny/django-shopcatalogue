from django import forms
from .models import UserProfiles

class UserProfileModelForm(forms.ModelForm):
	class Meta:
		model =UserProfiles
		fields ='__all__'
		widgets = {
			'password':forms.PasswordInput(
				attrs={
				'class':'form-control',
				}
			),
		}



class UserLoginForm(forms.Form):
	email=forms.EmailField(widget=forms.EmailInput())
	password=forms.CharField(widget=forms.PasswordInput())