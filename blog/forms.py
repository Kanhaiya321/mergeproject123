from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

# from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]    
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class update_profile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    mobileNumber = forms.IntegerField(null=True,blank=True)
    cityname = forms.CharField(max_length=100,null=True,blank=True)
    statename = forms.CharField(max_length=100,null=True,blank=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','mobileNumber','cityname','statename')
        
