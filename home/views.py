#____________________________________________________________________  HOME/VIEWS.PY
from django.shortcuts import render


# --------------------------------------------------------- INDEX
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
