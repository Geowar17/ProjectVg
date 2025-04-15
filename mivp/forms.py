from django import forms
from .models import Projects, Stage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProjectNewForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label='Project Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    name_contacto = forms.CharField(
        max_length=200,
        label='Contact Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    number_contacto = forms.CharField(
        max_length=20,
        label='Contact Number',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mail = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    direction_contac = forms.CharField(
        max_length=200,
        label='Contact Address',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
class TaskNewForm(forms.Form):
    title = forms.CharField(max_length=200, label='Título de la Tarea')
    description = forms.CharField(widget=forms.Textarea, label='Descripción')
    project = forms.ModelChoiceField(queryset=Projects.objects.all(), label='Proyecto')
    assigned_to = forms.ModelChoiceField(queryset=User.objects.all(), label='Responsable')
    priority = forms.ChoiceField(choices=[
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta')
    ], label='Prioridad')
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de Vencimiento')
    
    # 🔧 Añadir este campo
    stage = forms.ModelChoiceField(queryset=Stage.objects.all(), label='Etapa')

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


class StageForm(forms.Form):
    name = forms.CharField(label='Nombre de la etapa', max_length=100)
    default_user = forms.ModelChoiceField(queryset=User.objects.all(), required=False, label='Responsable por defecto')
