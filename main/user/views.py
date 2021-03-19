from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def loginUser(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Username or password is incorrect")
            return redirect('user:login')

        login(request, user)
        return redirect("csv:cvs-list")

    return render(request, "login.html", {"form": form})
