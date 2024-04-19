#______________________________________________________________________________ HITECH/PROFILES/VIEWS.PY
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model

from .forms import UserLoginForm, UserRegisterForm
from .models import UserProfile

from django.contrib import messages

User = get_user_model()


#______________________________________________________________________________ PROFILE VIEW
@login_required
def user_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profiles/profile.html', {'profile': profile})


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
            # Process form data
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
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )

                # Create a Profile instance for the user
                profile = Profile.objects.create(
                    user=user,
                    phone_number=phone_number,
                    address=address,
                    country=country,
                    profile_picture=profile_picture
                )

                # Debug statement to confirm profile creation
                print("Created profile:", profile)

                # Add success message
                messages.success(request, 'Registration successful. You can now log in.')

                # Redirect to login page after successful registration
                return redirect('login')  # Redirect to the login page

            except Exception as e:
                # Add error message
                messages.error(request, f'Registration failed: {str(e)}')

    else:
        form = UserRegisterForm()

    return render(request, 'profiles/register.html', {'form': form})



#______________________________________________________________________________ EDIT_PROFILE VIEW
@login_required
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
