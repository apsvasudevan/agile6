from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from teamspirit.models import Team
from teamspirit.models import Session

'''
class Test04UserCheckIn(LiveServerTestCase):

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
        session = Session()
        session.team = team
        session.name = "Test Session"
        session.save()
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    # def tearDown(self):
    #     self.browser.quit()

    def test_user_checkin(self):

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

        # 6. User checks in "Sad"
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/div/div[1]/div/div[2]/button[1]').click()

        # 7. User clicks on Stats
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/a[2]/button').click()

        # 8. User sees Nick has checked in Sad
        result = self.browser.find_element_by_xpath('/html/body/div/div/ul/li/b[2]')
        self.assertIn('Check In - Sad', result.text)

        # 9. User returns to dashboard
        self.browser.get(self.live_server_url + '/dashboard')

        # 10. User checks in "Glad"
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/div/div[1]/div/div[2]/button[2]').click()

        # 11. User clicks on Stats
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/a[2]/button').click()

        # 12. User sees Nick has checked in Glad
        result = self.browser.find_element_by_xpath('/html/body/div/div/ul/li[2]/b[2]')
        self.assertIn('Check In - Glad', result.text)

        # 13. User returns to dashboard
        self.browser.get(self.live_server_url + '/dashboard')

        # 14. User checks in "Mad"
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/div/div[1]/div/div[2]/button[3]').click()

        # 15. User clicks on Stats
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/a[2]/button').click()

        # 16. User sees Nick has checked in Mad
        result = self.browser.find_element_by_xpath('/html/body/div/div/ul/li[3]/b[2]')
        self.assertIn('Check In - Mad', result.text)

        # 17. User returns to dashboard
        self.browser.get(self.live_server_url + '/dashboard')

        # 18. User checks in "Afraid"
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/div/div[1]/div/div[2]/button[4]').click()

        # 19. User clicks on Stats
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/a[2]/button').click()

        # 20. User sees Nick has checked in Afraid
        result = self.browser.find_element_by_xpath('/html/body/div/div/ul/li[4]/b[2]')
        self.assertIn('Check In - Afraid', result.text)

        # 21. User returns to dashboard
        self.browser.get(self.live_server_url + '/dashboard')

        # 22. User checks out
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/div/div[2]/div/div[2]/button').click()

        # 23. User clicks on Stats
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/a[2]/button').click()

        # 24. User sees Nick has checked out
        result = self.browser.find_element_by_xpath('/html/body/div/div/ul/li[5]/b[2]')
        self.assertIn('Checked Out', result.text)

        # 25. User returns to dashboard
        self.browser.get(self.live_server_url + '/dashboard')

        # 26. User checks out
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/div/div[3]/div/div[2]/button').click()

        # 27. User clicks on Stats
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/a[2]/button').click()

        # 28. User sees Nick has passed
        result = self.browser.find_element_by_xpath('/html/body/div/div/ul/li[5]/b[2]')
        self.assertIn('Passed', result.text)

        # 29. User returns to dashboard
        self.browser.get(self.live_server_url + '/dashboard')
'''