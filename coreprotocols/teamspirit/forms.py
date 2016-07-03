from django.db import models
from teamspirit.models import Team, Session
from django.forms import ModelForm
from django.contrib.auth.models import User

class TeamForm(ModelForm):

    class Meta:
        model   = Team
        exclude = []

class SignUpForm(ModelForm):

	class Meta:
		model = User
		fields = ['email', 'username', 'password', 'first_name', 'last_name']

class SessionForm(ModelForm):

    class Meta:
        model   = Session
        exclude = []