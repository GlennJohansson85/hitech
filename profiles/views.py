from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm, RegisterForm, UserProfileForm
from .models import UserProfile


# Profile view
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    return render(request, 'profiles/profile.html')


# Login view
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('profile')  # Redirect to profile page after login
    else:
        form = LoginForm()

    return render(request, 'profiles/login.html', {'form': form})


# Register view
User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone_number = form.cleaned_data.get('phone_number')
            address = form.cleaned_data.get('address')
            country = form.cleaned_data.get('country')
            profile_picture = form.cleaned_data.get('profile_picture')

            # Check if the passwords match
            if form.cleaned_data.get('password2') != password:
                form.add_error('password2', 'Passwords do not match')
                return render(request, 'profiles/register.html', {'form': form})

            # Create a new user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            # Create a UserProfile instance for the user
            UserProfile.objects.create(
                user=user,
                phone_number=phone_number,
                address=address,
                country=country,
                profile_picture=profile_picture
            )

            # Redirect to login page after successful registration
            return redirect('profile')
    else:
        form = RegisterForm()

    return render(request, 'profiles/register.html', {'form': form})


# Profile edit view
def edit_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})
