from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# le decorateur permet de restreindre l'accés au user non connecté
@login_required
def home(request):
    return render(request, 'home.html')