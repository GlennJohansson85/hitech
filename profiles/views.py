#____________________________________________________________________ PROFILES/VIEWS.PY
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm, RegisterForm

def user(request):
    
    return render(request, 'profiles/profiles.html', {})


#---------------------------------------------------------LOGIN
def login(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to home page after login
        else:
            context['error_message']='Invalid username or password'

    return render(request, 'allauth/login.html', context)


#---------------------------------------------------------REGISTER
User = get_user_model()

def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

        return render(request, 'allauth/register.html', context)