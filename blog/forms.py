from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.models import User
# from .models import Profile
from django.db.migrations.state import get_related_models_tuples
from .models import Comment
from django.utils.translation import gettext_lazy as _



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        

        fields = ['content','parent']
        
        labels = {
            'content': _(''),
        }
        
        widgets = {
            'content' : forms.TextInput(),
        }

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category')
        


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

 
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))                         
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    # mobileNumber = forms.IntegerField(max_length = 50)
    # cityname = forms.CharField(max_length=200)
    # statename = forms.CharField(max_length=200)
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']
                               
                               




