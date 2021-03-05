from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def register(request):

    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':

        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('password2', None)

        response_data = {}

        if not (username and email and password and re_password):
            response_data['error'] = 'Please fill in all the required information.'

        elif password != re_password:
            response_data['error'] = 'Passwords do not match. Please try again.'

        else:
            user = User(
                username=username,
                useremail=email,
                password=make_password(password),
            )
            user.save()

        # if there are any errors found
        if response_data:
            return render(request, 'register.html', response_data)

        else:
            return redirect('/user/login')
