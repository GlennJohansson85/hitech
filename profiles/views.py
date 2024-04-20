#______________________________________________________________________________ HITECH/PROFILES/VIEWS.PY
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from .models import UserProfile

User = get_user_model()



#______________________________________________________________________________ PROFILE VIEW
def user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profiles/profile.html', {'profile': user_profile})


#______________________________________________________________________________ LOGIN VIEW
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful. Welcome back!')
                return redirect('home')  # Redirect to profile page after login
    else:
        form = UserLoginForm()

    return render(request, 'profiles/login.html', {'form': form})


#______________________________________________________________________________ REGISTER VIEW
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone_number = form.cleaned_data.get('phone_number')
            address = form.cleaned_data.get('address')
            country = form.cleaned_data.get('country')

            if form.cleaned_data.get('password2') != password:
                form.add_error('password2', 'Passwords do not match')
                return render(request, 'profiles/register.html', {'form': form})

            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )

                profile = UserProfile.objects.create(
                    user=user,
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone_number,
                    address=address,
                    country=country,
                )

                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')

            except Exception as e:
                messages.error(request, f'Registration failed: {str(e)}')

    else:
        form = UserRegisterForm()

    return render(request, 'profiles/register.html', {'form': form})



#______________________________________________________________________________ EDIT_PROFILE VIEW
def user_edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})
