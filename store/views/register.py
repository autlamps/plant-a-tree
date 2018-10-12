from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from store.forms import RegisterForm


@require_http_methods(["POST"])
def register_view(request):
    form = RegisterForm(request.POST)

    if form.is_vaild():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        passwordV = form.cleaned_data['passwordV']
        if password is passwordV:
            user = authenticate(username=username, password=password)
            return redirect('home')

    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})