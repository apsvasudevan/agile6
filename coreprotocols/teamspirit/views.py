from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def landing_page(request):
    context = {}
    return render(request, 'teamspirit/landing.html', { "context" : context })
