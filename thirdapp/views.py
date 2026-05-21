from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.

def register_page(request):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('password')
        User.objects.create_user(username=a, password=b)
        return redirect('login')
    return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('password')
        c = authenticate(username=a, password=b)
        if c:
            login(request,c)
            return redirect('dashboard')

    return render(request, 'login.html')


def dashboard(request):
    c=Task.objects.filter(user=request.user)
    if request.method == "POST":
        task=request.POST.get('task')
        Task.objects.create(user=request.user,task=task)
        return redirect('dashboard')
    return render(request, 'dashboard.html',{'c':c})
def logout_page(request):
    logout(request)
    print
    return redirect('login')
def delete_task(request, id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('dashboard')
def update_task(request, id):
    todo = get_object_or_404(Task,id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        todo.task=title
        todo.save()
        return redirect('dashboard')
    return render(request,'update.html',{'todo':todo})

