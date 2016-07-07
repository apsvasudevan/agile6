from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from teamspirit.models import Team
from teamspirit.models import Session
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep



class Test10UserCheckIn(LiveServerTestCase):

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

        # User clicks on Owned Teams
        self.browser.find_element_by_id('id_ownedteams').click()

        # User clicks on Test Team
        self.browser.find_element_by_id('id_ownedteam_name').click()

        # 6. User checks in "Sad"
        self.browser.find_element_by_id('id_member_sad').click()

        # User refreshes dashboard
        self.browser.refresh()

        # User clicks on Owned Teams
        self.browser.find_element_by_id('id_ownedteams').click()

        # User clicks on Test Team
        self.browser.find_element_by_id('id_ownedteam_name').click()

        # User click to see stats
        self.browser.find_element_by_id('id_member_stats').click()

        sleep(1)

        # delay = 10 # seconds
        # try:
        #     WebDriverWait(self.browser, delay).until(EC.presence_of_element_located(self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li/b[2]')))
        #     print "Page is ready!"
        # except TimeoutException:
        #     print "Loading took too much time!"

        # 8. User sees Nick has checked in Sad
        result = self.browser.find_element_by_xpath("//div[@role = 'tooltip']")
        self.assertIn('Check In - Sad', result.text)

        # self.browser.switch_to.window(main_window_handle)
        #
        # # 9. User returns to dashboard
        # self.browser.get(self.live_server_url + '/dashboard')
        #
        # # 10. User checks in "Glad"
        # self.browser.find_element_by_id('id_member_glad').click()
        #
        # # User refreshes dashboard
        # self.browser.refresh()
        #
        # # 11. User clicks on Stats
        # self.browser.find_element_by_id('id_member_stats').click()
        #
        # # 12. User sees Nick has checked in Glad
        # result = self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[2]')
        # self.assertIn('Check In - Glad', result.text)
        #
        # # 13. User returns to dashboard
        # self.browser.get(self.live_server_url + '/dashboard')
        #
        # # 14. User checks in "Mad"
        # self.browser.find_element_by_id('id_member_mad').click()
        #
        # # User refreshes dashboard
        # self.browser.refresh()
        #
        # # 15. User clicks on Stats
        # self.browser.find_element_by_id('id_member_stats').click()
        #
        # # 16. User sees Nick has checked in Mad
        # result = self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[3]')
        # self.assertIn('Check In - Mad', result.text)
        #
        # # 17. User returns to dashboard
        # self.browser.get(self.live_server_url + '/dashboard')
        #
        # # 18. User checks in "Afraid"
        # self.browser.find_element_by_id('id_member_afraid').click()
        #
        # # User refreshes dashboard
        # self.browser.refresh()
        #
        # # 19. User clicks on Stats
        # self.browser.find_element_by_id('id_member_stats').click()
        #
        # # 20. User sees Nick has checked in Afraid
        # result = self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[4]')
        # self.assertIn('Check In - Afraid', result.text)
        #
        # # 21. User returns to dashboard
        # self.browser.get(self.live_server_url + '/dashboard')
        #
        # # 22. User checks out
        # self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/div/div[2]/div/div[2]/button').click()
        #
        # # User refreshes dashboard
        # self.browser.refresh()
        #
        # # 23. User clicks on Stats
        # self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/button').click()
        #
        # # 24. User sees Nick has checked out
        # result = self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[5]')
        # self.assertIn('Checked Out', result.text)
        #
        # # 25. User returns to dashboard
        # self.browser.get(self.live_server_url + '/dashboard')
        #
        # # 26. User Passes
        # self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/div/div[3]/div/div[2]/button').click()
        #
        # # User refreshes dashboard
        # self.browser.refresh()
        #
        # # 27. User clicks on Stats
        # self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul[2]/li[1]/button').click()
        #
        # # 28. User sees Nick has passed
        # result = self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[6]')
        # self.assertIn('Passed', result.text)
        #
        # # 29. User returns to dashboard
        # self.browser.get(self.live_server_url + '/dashboard')
