from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .validators import validate_password_length
from django.core.exceptions import ValidationError

# Create your views here.


def login_view(request):

    context = {}

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'notes.html', context)

        else:
            context['error'] = 'Incorrect login crredentials'

    return render(request, 'login.html', context)


def register_view(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('confirm_password')

        print(email)
        print(username)
        print(password)
        print(password_confirm)

        if password != password_confirm:
            context['error'] = 'Passwords doesnt match'

        else:
            try:
                validate_password_length(password)

                if User.objects.filter(username=username).exists():
                    context['error'] = 'Username not available'

                elif User.objects.filter(email=email).exists():
                    context['error'] = 'Email already exists'

                else:
                    user = User(email=email, username=username,
                                password=make_password(password))
                    user.save()

                    return render(request, 'login.html', context)

            except ValidationError as e:
                context['error'] = e.messages[0] if e.messages else ''

    return render(request, 'register.html', context)


def notes_view(request):
    return render(request, 'notes.html')
