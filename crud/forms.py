from django import forms 
from crud.models import Mobiles
from django.contrib.auth.models import User

class MobileForm(forms.ModelForm):
    
    class Meta:
        model = Mobiles
        fields = '__all__'                                              
        
class Register(forms.ModelForm):
    class Meta:
        model = User 
        fields=['username','password','first_name','last_name','email']
    
class Signin(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField( max_length=100)