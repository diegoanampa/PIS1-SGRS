from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

def task_list_and_create(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud01:crud_list')
    else:
        form = TaskForm()
    #tasks = Task.objects.all()
    complete_tasks = Task.objects.filter(is_created=True)
    incomplete_tasks = Task.objects.filter(is_created=False)



    return render(request, 'task_list.html',{
        'form':form,
     #   'tasks':tasks
        'complete_tasks':complete_tasks,
        'incomplete_tasks':incomplete_tasks
    })

def update_task(request,task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.is_created = not task.is_created
        task.save()
        return redirect('crud01:crud_list')

# Create your views here.
