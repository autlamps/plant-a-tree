from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from store.forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request=request, user=user)
                return redirect('store:index')

            else:
                messages.error(request, 'Incorrect Username or Password!')
                return redirect('store:login')
        else:
            messages.error(request, 'Incorrect Username or Password!')
            return redirect('store:login')

    elif request.method == 'GET':
        form = LoginForm()

        return render(request, 'login.html', context={
            'form': form,
            'page_title': "Login",
        })