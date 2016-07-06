from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from teamspirit.models import Team


class Test04UserAddRemoveSession(LiveServerTestCase):

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@mysite.com', 'meantime')
        nick   = User.objects.create_user('nick', 'nick@mysite.com', 'meantime')
        truman = User.objects.create_user('truman', 'nick@mysite.com', 'meantime')
        brian  = User.objects.create_user('brian', 'nick@mysite.com', 'meantime')
        # Team.objects.create(owner=nick, name='Test Team', members=[nick, truman, brian])
        team = Team()
        team.owner = nick
        team.name = "Test Team"
        team.save()
        team.members.add(nick.id, truman.id, brian.id)


    def tearDown(self):
        self.browser.quit()

    def test_user_add_remove_session(self):

        # 1. User goes to main page
        self.browser.get(self.live_server_url + '/')

        # 2. User selects to Sign In
        self.browser.find_element_by_id('id_signin').click()

        # 3. User enters username
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('nick')

        # 4. User enters password
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('meantime')

        # 5. User clicks to Sign In button
        self.browser.find_element_by_id('id_signin').click()

        # User selects team
        self.browser.find_element_by_xpath('/html/body/div/div/ul/li[2]/ul/li/a').click()

        # 1. User clicks to add a new session
        self.browser.find_element_by_xpath('/html/body/div/div/div/div/ul[2]/li/a').click()

        # 2. User sees the session page
        result = self.browser.find_element_by_xpath('/html/body/div/div/div/h3')
        self.assertIn('Create session for Team: Test Team', result.text)

        # 4. User enters "Test Session" as the session name
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Test Session')

        # 5. User clicks "Submit"
        self.browser.find_element_by_xpath('/html/body/div/div/div/form/input[2]').click()

        # 6. User checks to make sure "Test Session" was create successfully
        result = self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/strong')
        self.assertIn('Test Session', result.text)

        # 7. User closes session
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/a[1]/button').click()

        # 8. User verifies session is closed
        result = self.browser.find_element_by_xpath('/html/body')
        self.assertIn('session closed', result.text)
