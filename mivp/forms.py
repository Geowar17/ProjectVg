from django import forms
from .models import Projects
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProjectNewForm(forms.Form):
    name = forms.CharField(max_length=200, label='Project Name')
    name_contacto = forms.CharField(max_length=200, label='Contact Name')
    number_contacto = forms.CharField(max_length=20, label='Contact Number')
    mail = forms.EmailField(label='Email Address')
    direction_contac = forms.CharField(max_length=200, label='Contact Address')
   

class TaskNewForm(forms.Form):
    title = forms.CharField(max_length=200, label='Task Title')
    description = forms.CharField(widget=forms.Textarea, label='Task Description')
    project = forms.ModelChoiceField(queryset=Projects.objects.all(), label='Project')
   

class registerNewForm(forms.Form):
    user = forms.CharField(max_length=200, label='User Name')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    email = forms.EmailField(label='Email Address')
    name = forms.CharField(max_length=200, label='Full Name')
    phone = forms.CharField(max_length=20, label='Phone Number')
    
class loginForm(forms.Form):
    username = forms.CharField(max_length=200, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
