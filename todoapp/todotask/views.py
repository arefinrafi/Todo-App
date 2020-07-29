from django.shortcuts import render, redirect
from .models import Task
from .forms import TodoForm


# Create your views here.


def task(request):
    tasks = Task.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'todo/task.html', {'tasks': tasks, 'form': form})


def update(request, pk):
    tasks = Task.objects.all()
    update_task = Task.objects.get(id=pk)
    form = TodoForm(instance=update_task)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=update_task)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'todo/update.html', {'tasks': tasks, 'form': form})


def task_delete(request, pk):
    delete_task = Task.objects.get(id=pk)
    delete_task.delete()
    return redirect('task')
