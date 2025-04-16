from django import forms
from .models import Projects, Stage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Formulario para crear un nuevo proyecto
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

# Formulario para crear una nueva tarea
class TaskNewForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label='Título de la Tarea',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        label='Descripción'
    )
    project = forms.ModelChoiceField(
        queryset=Projects.objects.all(),
        label='Proyecto',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Responsable',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    priority = forms.ChoiceField(
        choices=[
            ('low', 'Baja'),
            ('medium', 'Media'),
            ('high', 'Alta')
        ],
        label='Prioridad',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Fecha de Vencimiento'
    )
    stage = forms.ModelChoiceField(
        queryset=Stage.objects.all(),
        label='Etapa',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

# Formulario personalizado para registro simple (no usado si se usa RegisterForm)
class registerNewForm(forms.Form):
    user = forms.CharField(
        max_length=200,
        label='User Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Password'
    )
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    name = forms.CharField(
        max_length=200,
        label='Full Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=20,
        label='Phone Number',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

# Formulario para login de usuario
class loginForm(forms.Form):
    username = forms.CharField(
        max_length=200,
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Password'
    )

# Formulario basado en UserCreationForm de Django, más completo para registro
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

# Formulario para crear nuevas etapas
class StageForm(forms.Form):
    name = forms.CharField(
        label='Nombre de la etapa',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    default_user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label='Responsable por defecto',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

