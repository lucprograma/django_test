from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
def index(request):
    """
    Test method 
    """
    return HttpResponse("Hello, world. You're at the polls index.")
def list_tasks(request):
    """ Gets all tasks from the database and renders them in a template.
    Args:
        request: HTTPRequest
    Returns: HTTPResponse
    """
    tasks = Task.objects.filter(user_ref=request.user.id)
    return render(request, "list_tasks.html", {'tasks': tasks})
def delete_task(request, id):
    """ Deletes a specific task from the database.
    Args:
        request: HTTPRequest
        id: int
    Returns: HTTPResponse
    
    """
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('list_tasks')
def create_task(request):
    """ Creates a new task in the database.
    Args:
        request: HTTPRequest"
    Returns: HTTPResponse
        """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            task = form.save(commit=False)
            task.user_ref_id = request.user.id
            task.save()
            return redirect('list_tasks')
    else:
        print("Form is invalid")
        form = TaskForm()
    return render(request, "create_task.html", {'form': form})

def update_task(request, id):
    """ Updates a specific task in the database.
    Args:
        request: HTTPRequest
        id: int"
        """
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            # task = form.save(commit=False)
            # task.user_ref_id = request.user.id
            task.save()
            return redirect('list_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, "update.html", {'form': form, 'task': task})

def navigation(request):
    """
    args:
        request: HTTPRequest
    returns: HTTPResponse
    """
    return render(request, "navigation.html")