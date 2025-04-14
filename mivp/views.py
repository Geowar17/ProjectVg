from django.shortcuts import render, redirect
from .models import Projects,Tasks
from .forms import ProjectNewForm, TaskNewForm, RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    
    return render(request,'home.html')

def projects(request):
    projects= Projects.objects.all()
    return render(request, 'project/project.html',{
        'projects': projects
        
    })
def tasks(request):
    tasks= Tasks.objects.all()
    return render(request,'tasks/tasks.html', {
        
        'tasks':tasks
    })
                   
def create_project(request):
    if request.method == 'GET':
        return render(request,'project/create_project.html', {
            'form': ProjectNewForm()
        })
    else:    
        Projects.objects.create(
            name=request.POST['name'],
            name_contacto=request.POST['name_contacto'],
            number_contacto=request.POST['number_contacto'],
            mail=request.POST['mail'],
            direction_contac=request.POST['direction_contac']
        )
        return redirect('/projects')

def create_tasks(request):
        
     if request.method == 'GET':
        return render(request,'tasks/create_tasks.html', {
            'form': TaskNewForm()
        })
     else:  
        
        Tasks.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
        project=Projects.objects.get(id=request.POST['project'])
    )
        return redirect('/tasks')
    


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loguea automáticamente al registrarse
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home')  # Redirige a donde quieras
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login/')
