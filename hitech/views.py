#----------------------------------------------------------------------------  HITECH/VIEWS.PY
from django.shortcuts import render, redirect
from .forms import ContactForm

#---------------------------------------------------------ABOUT
def about(request):
    context = {
        'title': 'About Page',
        'content': 'Welcome to the About Page!',
    }
    return render(request, 'hitech/about.html', context)


#---------------------------------------------------------CONTACT
def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'content': 'Welcome to the Contact Page!',
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'hitech/contact.html', context)