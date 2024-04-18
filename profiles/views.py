#____________________________________________________________________ PROFILES/VIEWS.PY
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm, RegisterForm, UserProfileForm


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    
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
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        # Redirect to the login page after successful registration
        return redirect(reverse('account_login'))

    context = {'form': form}
    return render(request, 'allauth/register.html', context)
