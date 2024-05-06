#______________________________________________________________________________ HITECH/PROFILES/VIEWS.PY
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile

@login_required
def user_profile(request):
    return render(request, 'profiles/profile.html')

@login_required
def user_edit_profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # If UserProfile does not exist for the current user, create it
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=user_profile)
        
    return render(request, 'profiles/edit_profile.html', {'form': form})
