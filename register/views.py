from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.shortcuts import render

class AdminLogin(LoginView):#вход на сайт
    template_name = 'LoginView_form.html'


class LogOutView(TemplateView):#Выход и направляет на главную страницу
    template_name = "index.html"


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'reg_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'reg.html', {'user_form': user_form})