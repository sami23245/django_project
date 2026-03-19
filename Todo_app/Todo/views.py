from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from Todo import models
from .models import Todo

#Create your views here.

def login_view(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm,pwd) #JUST TO CLERIFY THE DATA IS COMING OR NOT
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            login(request, user)
            return render(request, 'todo.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        email = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        print(fnm,email,pwd) #JUST TO CLERIFY THE DATA IS COMING OR NOT

        mY_user = User.objects.create_user(username=email, email=email, password=pwd, first_name=fnm)
        mY_user.save()
        
        # Handle user registration logic here
        return redirect('login')

    return render(request, 'signup.html')

def todo_view(request):
    if request.method == 'POST':
        title = request.POST.get("Title")
        srno = request.POST.get("srno")
        print(title,srno)
        if srno == "":
            obj = Todo(title=title)
            obj.save()
        else:
            obj = Todo.objects.get(srno=srno)
            obj.title = title
            obj.save()
    return render(request, 'todo.html')