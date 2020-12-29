from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render(request, 'todo/index.html')


@login_required
def add_todo(request):
    logged_in_user = request.user
    todo = Todo.objects.filter(user=logged_in_user).order_by('-created_date')
    form = TodoForm()
    params = {'form': form, 'todo': todo}

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'Your todo-list added/updated successfully.')
            return redirect('/todo/add_todo/')

    return render(request, 'todo/add_todo.html', params)


# @login_required
# def list_todo(request):
#     todo = Todo.objects.all().order_by('-created_date')
#     params = {'todo': todo}
#     return render(request, 'todo/list_todo.html', params)

@login_required
def list_todo(request):
    logged_in_user = request.user
    todo = Todo.objects.filter(user=logged_in_user).order_by('-created_date')
    params = {'todo': todo}
    return render(request, 'todo/list_todo.html', params)


@login_required
def search_todo(request):
    logged_in_user = request.user
    q = request.GET['searching']
    todo = Todo.objects.filter(user=logged_in_user, title__contains=q)
    params = {'todo': todo}
    return render(request, 'todo/list_todo.html', params)


def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todo/add_todo/')


def update_todo(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    todo.delete()
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/todo/list_todo/')
    params = {'form': form}
    return render(request, 'todo/update_todo.html', params)


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo/login/')
    params = {'form': form}
    return render(request, 'todo/register.html', params)


def login(request):
    form = LoginForm()
    params = {'form': form}
    return render(request, 'todo/login.html', params)


def logout(request):
    return render(request, 'todo/logout.html')


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UpdateUserForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, ' Your account has been updated successfully.')
            return redirect('/todo/profile/')
    u_form = UpdateUserForm(instance=request.user)

    params = {
        'u_form': u_form,
    }

    return render(request, 'todo/profile.html', params)
