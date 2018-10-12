from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from store.forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            passwordV = form.cleaned_data['passwordV']

            is_user = User.objects.filter(username=username).exists()
            if is_user:
                messages.error(request, 'User already exists!')
                return redirect('store:register')

            else:
                if password == passwordV:
                    user = User.objects.create_user(username=username,
                                                    password=password)
                    user.save()
                    login(request=request, user=user)

                    return redirect('store:index')

                else:
                    messages.error(request, 'Passwords do not match!')
                    return redirect('store:register')

        else:
            form = RegisterForm()

            return render(request, 'register.html', {'form': form})

    elif request.method == 'GET':
        form = RegisterForm()

        return render(request, 'register.html', {'form': form})
