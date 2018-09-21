from django import forms as fm


class LoginForm(fm.Form):
    username = fm.CharField(label="Username")
    password = fm.CharField(label="Password", widget=fm.PasswordInput())
