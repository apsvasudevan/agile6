# ./manage.py test --pattern="test_09_create_session.py"
from django.contrib.auth.models import User
from django.test import TestCase
from teamspirit.models import Team, Session


class Test09DjangoCreateSession(TestCase):

    def setUp(self):

        foxy = User.objects.create(username='foxy', email='admin@mysite.com', password='meantime', first_name="Fox", last_name="Panks")
        joan = User.objects.create(username='joan', email='admin@mysite.com', password='meantime', first_name="Joan", last_name="Torche")
        ellen = User.objects.create(username='ellen', email='admin@mysite.com', password='meantime', first_name="Ellen", last_name="Nice")

        # create team
        team = Team()
        team.owner=foxy
        team.name="TestTeam"
        team.save()
        team.members = [foxy, joan, ellen]
        team.save()

        # create session
        session = Session()
        session.team = team
        session.name = "StandUp Test"
        session.is_open = True
        session.save()

    def test_session_name(self):
        session = Session.objects.get(name="StandUp Test")
        self.assertEquals(session.name, "StandUp Test")

    def test_session_member_count(self):
        session = Session.objects.get(name="StandUp Test")
        self.assertEquals(session.team.name, "TestTeam")

    def test_session_is_open(self):
        session = Session.objects.get(name="StandUp Test")
        self.assertEquals(session.is_open, True)
