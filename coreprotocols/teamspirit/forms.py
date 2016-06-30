from django.db import models
from teamspirit.models import Team
from django.forms import ModelForm


class TeamForm(ModelForm):

    class Meta:
        model  = Team
        exclude = []
