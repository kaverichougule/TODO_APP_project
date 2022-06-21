from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'tasks':tasks, 'form':form}
    return render(request, 'task_list.html',context)

def updateTask(request,pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method =='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('//')
    context = {'form':form}
    return render(request, 'update_task.html', context)

def delete(request,pk):
    item = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'delete.html',context)

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form":form
        }
        return render(request, 'signup.html', context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            return HttpResponse("Form is valid")
        else:
            return HttpResponse("Form is invalid")