from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):

    if request.method == "POST":
        username = request.POST.get('username_or_email', '')
        password = request.POST.get('password', '')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                else:
                    messages.warning(request, "کاربری  با این نام وجود ندارد")
                    return redirect("users:login")
        else:
            messages.warning(request, "فرم ورود را تکمیل کنید")

    return render(request, 'login.html', {})

def register_view(request):

    if request.method == "POST":
        username = request.POST.get('username', "")