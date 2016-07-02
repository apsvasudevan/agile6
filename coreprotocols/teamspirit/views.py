from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from teamspirit.forms import TeamForm
from teamspirit.models import Team
from django.contrib.auth.models import User

@login_required
def landing_page(request):
    context = {}
    context['teams'] = Team.objects.all().order_by('name')
    return render(request, 'teamspirit/landing.html', { "context" : context })

@login_required
def team_create(request):
    if request.method == 'POST': # If the form has been submitted...
        data = request.POST.copy()
        data['owner'] = request.user.id
        data.setlist( 'members', [request.user.id] )
        form = TeamForm(data) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return redirect('landing_page')
        else:
            pass
    else:
        form = TeamForm() # An unbound form

    return render(request, 'teamspirit/team_create.html', { "form" : form })

@login_required
def add_member(request, pk):
    team = Team.objects.get(id=pk)
    context = {}
    context['team'] = team
    context['users'] = User.objects.all().order_by('name')
    if request.method == 'POST': # If the form has been submitted...
        data = request.POST.copy()
        data['owner'] = team.owner.id
        data['name']  = team.name
        form = TeamForm(data, instance=team) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return redirect('landing_page')
        else:
            pass
    else:
        formData = {
            'members' : team.members,
        }
        form = TeamForm() # An unbound form

    return render(request, 'teamspirit/add_member.html', { "form" : form, 'context':context })
