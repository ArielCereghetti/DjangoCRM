from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class RegisterUser(UserCreationForm):
    class_attr = 'signupform'
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": class_attr,
            })
    )
    email = forms.EmailField(
        label="Email", 
        widget=forms.EmailInput(
            attrs={
                "class": class_attr,
            }),
        max_length=170
        )
    password1 = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput(
            attrs={
                "class": class_attr,
                }), 
        max_length=100
        )
    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(
            attrs={
                "class": class_attr,
            }),
        max_length=100,
        )

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    class_attr = 'signupform'
    username = forms.CharField(max_length=100, label="Username", widget=forms.TextInput(
        attrs={
            'class': class_attr,
            })
        )
    password = forms.CharField(max_length=100, label="Password", widget=forms.PasswordInput(
        attrs={
            'class': class_attr,
        }
    ))
