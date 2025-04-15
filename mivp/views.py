from django.shortcuts import render, redirect, get_object_or_404
from .models import Projects,Tasks, Stage
from .forms import ProjectNewForm, TaskNewForm, RegisterForm, StageForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    
    return render(request,'home.html')

def projects(request):
    projects= Projects.objects.all()
    return render(request, 'project/project.html',{
        'projects': projects
        
    })
    
def tasks(request):
    stages = Stage.objects.all()
    return render(request, 'tasks/tasks.html', {
        'stages': stages
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
        return render(request, 'tasks/create_tasks.html', {
            'form': TaskNewForm()
        })
    else:  
        Tasks.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project=Projects.objects.get(id=request.POST['project']),
            assigned_to=User.objects.get(id=request.POST['assigned_to']),
            stage=Stage.objects.get(id=request.POST['stage']),
            priority=request.POST['priority'],
            due_date=request.POST['due_date']
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
    return redirect('/home/')



def advance_stage(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    stages = list(Stage.objects.all())
    current_index = stages.index(task.stage)
    if current_index < len(stages) - 1:
        task.stage = stages[current_index + 1]
        task.save()
    return redirect('kanban')

def back_stage(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    stages = list(Stage.objects.all())
    current_index = stages.index(task.stage)
    if current_index > 0:
        task.stage = stages[current_index - 1]
        task.save()
    return redirect('kanban')



def create_stage(request):
    if request.method == 'POST':
        form = StageForm(request.POST)
        if form.is_valid():
            Stage.objects.create(
                name=form.cleaned_data['name'],
                default_user=form.cleaned_data['default_user']
            )
            return redirect('stage_list')
    else:
        form = StageForm()
    
    return render(request, 'stages/create_stage.html', {'form': form})


def stage_list(request):
    stages = Stage.objects.all()
    return render(request, 'stages/stage_list.html', {'stages': stages})



@login_required
def kanban_board(request):
    stages = Stage.objects.all()
    tasks_by_stage = {stage: Tasks.objects.filter(stage=stage) for stage in stages}

    return render(request, 'tasks/kanban.html', {
        'tasks_by_stage': tasks_by_stage
    })
