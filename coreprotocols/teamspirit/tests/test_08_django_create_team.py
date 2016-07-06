# ./manage.py test --pattern="test_08_django_create_team.py"
from django.contrib.auth.models import User
from django.test import TestCase
from teamspirit.models import Team


class Test08DjangoCreateTeam(TestCase):

    def setUp(self):
        foxy = User.objects.create(username='foxy', email='admin@mysite.com', password='meantime', first_name="Fox", last_name="Panks")
        team = Team()
        team.owner=foxy
        team.name="TestTeam"
        team.save()
        team.members = [foxy]
        team.save()

    def test_team_name(self):
    	team = Team.objects.get(name="TestTeam")
        self.assertEquals(team.name, "TestTeam")

    def test_owner_name(self):
    	team = Team.objects.get(name="TestTeam")
        self.assertEquals(team.owner.first_name, "Fox")        
        self.assertEquals(team.owner.last_name, "Panks")        
        self.assertEquals(team.owner.username, "foxy")

    def test_members(self):
    	team = Team.objects.get(name="TestTeam")
    	self.assertEquals(team.members.count(), 1)

