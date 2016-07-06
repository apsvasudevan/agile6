from django.contrib import admin
from teamspirit.models import Session, Team, SessionState, MOTD

# Register your models here.
admin.site.register(Team)
admin.site.register(Session)
admin.site.register(SessionState)
admin.site.register(MOTD)