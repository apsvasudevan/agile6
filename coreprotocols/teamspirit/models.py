from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = (
                ('Sad', 'Sad'),
                ('Mad', 'Mad'),
                ('Glad', 'Glad'),
                ('Afraid', 'Afraid'),
                ('Check Out', 'Check Out'),
                ('Pass', 'Pass'),
               )


class Team(models.Model):
    owner   = models.ForeignKey(User, related_name="team_owner")
    members = models.ManyToManyField(User, related_name="team_members")
    name    = models.CharField(max_length=255, unique=True)


    def __str__(self):   
        return "{}".format(self.name)

class Session(models.Model):
    team       = models.ForeignKey(Team, related_name="session_team")
    name       = models.CharField(max_length=100)
    is_open    = models.BooleanField(default=True)
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):   
        return "{}".format(self.name)

class SessionState(models.Model):
    user                    = models.ForeignKey(User, related_name="session_state_user")
    session                 = models.ForeignKey(Session, related_name="session_state_session")
    state                   = models.CharField(max_length=100, choices=STATE_CHOICES)
    session_state_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):   
        return "{}".format(self.session.name)

    # def __str__(self):   
       #  return "{}-{}-{}".format(self.tank_number, self.rack, self.box)

