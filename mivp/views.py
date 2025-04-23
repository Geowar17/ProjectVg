from django.shortcuts import render, redirect, get_object_or_404
from .models import Projects, Tasks, Stage
from .forms import ProjectNewForm, TaskNewForm, RegisterForm, StageForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Projects, ProjectDocument
from .forms import ProjectDocumentForm



# Página de inicio
def home(request):
    return render(request, 'home.html')

# Listar proyectos
def projects(request):
    projects = Projects.objects.all()
    return render(request, 'project/project.html', {'projects': projects})

# Vista general de etapas
def tasks(request):
    stages = Stage.objects.all()
    return render(request, 'tasks/tasks.html', {'stages': stages})

# Crear proyecto
def create_project(request):
    if request.method == 'GET':
        return render(request, 'project/create_project.html', {'form': ProjectNewForm()})
    else:
        Projects.objects.create(
            name=request.POST['name'],
            name_contacto=request.POST['name_contacto'],
            number_contacto=request.POST['number_contacto'],
            mail=request.POST['mail'],
            direction_contac=request.POST['direction_contac']
        )
        return redirect('/projects')

# Crear tarea
def create_tasks(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_tasks.html', {'form': TaskNewForm()})
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

# Registro
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/projects')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('home')

# ✅ Avanzar tarea con control de permisos por rol
@login_required
def advance_stage(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    user_role = request.user.profile.role
    stages = list(Stage.objects.all())
    current_index = stages.index(task.stage)

    if current_index < len(stages) - 1:
        next_stage = stages[current_index + 1]

        if task.stage.responsible_role == user_role or user_role == 'admin':
            task.stage = next_stage
            task.save()
        else:
            return HttpResponseForbidden("No tienes permiso para avanzar esta tarea.")

    return redirect('kanban')

# ✅ Retroceder tarea con validación también
@login_required
def back_stage(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    user_role = request.user.profile.role
    stages = list(Stage.objects.all())
    current_index = stages.index(task.stage)

    if current_index > 0:
        prev_stage = stages[current_index - 1]

        if task.stage.responsible_role == user_role or user_role == 'admin':
            task.stage = prev_stage
            task.save()
        else:
            return HttpResponseForbidden("No tienes permiso para retroceder esta tarea.")

    return redirect('kanban')

# ✅ Crear etapa con nuevo campo responsible_role
def create_stage(request):
    if request.method == 'POST':
        form = StageForm(request.POST)
        if form.is_valid():
            Stage.objects.create(
                name=form.cleaned_data['name'],
                default_user=form.cleaned_data['default_user'],
                responsible_role=form.cleaned_data['responsible_role']
            )
            return redirect('stage_list')
    else:
        form = StageForm()
    return render(request, 'stages/create_stage.html', {'form': form})

# Listar etapas
def stage_list(request):
    stages = Stage.objects.all()
    return render(request, 'stages/stage_list.html', {'stages': stages})

# ✅ Kanban: mostrar todas las etapas, pero restringir acciones en plantilla
@login_required
def kanban_board(request):
    stages = Stage.objects.all()
    projects = Projects.objects.filter(is_archived=False)

    tasks_by_project = {}
    for project in projects:
        tasks_by_stage = {}
        for stage in stages:
            tasks_by_stage[stage] = Tasks.objects.filter(project=project, stage=stage, is_completed=False)
        tasks_by_project[project] = tasks_by_stage

    return render(request, 'tasks/kanban.html', {
        'projects': projects,
        'stages': stages,
        'tasks_by_project': tasks_by_project,
    })

# views.py



@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    documents = project.documents.all()

    if request.method == 'POST':
        form = ProjectDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.project = project
            doc.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectDocumentForm()

    return render(request, 'project/project_detail.html', {
        'project': project,
        'documents': documents,
        'form': form
    })



@login_required
def delete_document(request, doc_id):
    doc = get_object_or_404(ProjectDocument, id=doc_id)
    project_id = doc.project.id
    doc.file.delete()  # Borra el archivo del sistema
    doc.delete()       # Borra el registro de la base de datos
    return redirect('project_detail', project_id=project_id)

# 🔥 Mostrar solo proyectos activos
@login_required
def active_projects(request):
    projects = Projects.objects.filter(is_archived=False)
    return render(request, 'project/project.html', {'projects': projects})

# 🔥 Mostrar proyectos archivados
@login_required
def archived_projects(request):
    projects = Projects.objects.filter(is_archived=True)
    return render(request, 'project/archived_projects.html', {'projects': projects})

# 🔥 Archivar un proyecto
@login_required
def archive_project(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    project.is_archived = True
    project.save()
    return redirect('projects')  # Redirige donde prefieras: 'active_projects' o 'projects'

# 🔥 Marcar una tarea como completada
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    user_role = request.user.profile.role
    if task.stage.responsible_role == user_role or user_role == 'admin':
        task.is_completed = True
        task.save()
    else:
        return HttpResponseForbidden("No tienes permiso para completar esta tarea.")
    return redirect('kanban')

# 🔥 Ver tareas completadas
@login_required
def completed_tasks(request):
    tasks = Tasks.objects.filter(is_completed=True)
    return render(request, 'tasks/completed_tasks.html', {'tasks': tasks})
from django.db.models import Q  # Asegúrate de tener esto importado

@login_required
def search_archived_and_completed(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Projects.objects.filter(
            Q(is_archived=True) | Q(tasks__is_completed=True),
            Q(name__icontains=query) | Q(name_contacto__icontains=query)
        ).distinct()

    return render(request, 'project/search_archived_and_completed.html', {
        'query': query,
        'results': results
    })

@login_required
def unarchive_project(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    project.is_archived = False
    project.save()
    return redirect('projects')
