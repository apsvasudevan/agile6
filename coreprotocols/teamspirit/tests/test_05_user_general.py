# -*- coding: iso-8859-15 -*-
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class Test05UserGeneral(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(4)

    # def tearDown(self):
    #     self.browser.quit()

    def test_user_pages_login(self):

        # 1. User can get main URL
        self.browser.get(self.live_server_url + '/')

        # 2. User sees the appropriate page
        self.assertIn(u'Team\u2605Spirit', self.browser.title)

        # 3. User presses Sign Up button
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/p[2]/a[1]').click()

        # 4. User confirms they are on the sign up page
        result = self.browser.find_element_by_xpath('/html/body/div/div/div/h3')
        self.assertIn('Sign up using your email', result.text)

        # 5. User fills in Username field
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('user')

        # 6. User fills in Email field
        email_field = self.browser.find_element_by_name('email')
        email_field.send_keys('user@somewhere.com')

        # 7. User fills in Password field
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('m3@nt!m3')

        # 8. User fills in First Name field
        first_name_field = self.browser.find_element_by_name('first_name')
        first_name_field.send_keys('Some')

        # 9. User fills in Last Name field
        last_name_field = self.browser.find_element_by_name('last_name')
        last_name_field.send_keys('One')

        # 10. User checks box to accept Core Protocols
        self.browser.find_element_by_id('protocol1').click()

        # 11. User clicks on sign up button
        self.browser.find_element_by_xpath('/html/body/div/div/div/div/form/input[2]').click()

        # 12. User find themselves on the correct page
        self.assertIn(u'Team\u2605Spirit', self.browser.title)

        # 13. User logs out
        self.browser.find_element_by_xpath('/html/body/div[1]/div/nav/div/div[2]/ul/li[3]/a').click()

        # 14. User Presses Sign In button
        self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/p[2]/a[2]').click()

        # 15. User fills in Username field
        username_field = self.browser.find_element_by_id('id_username')
        username_field.send_keys('user')

        # 16. User fills in Password field
        password_field = self.browser.find_element_by_id('id_password')
        password_field.send_keys('m3@nt!m3')

        # 17. User presses Sign In button
        self.browser.find_element_by_xpath('/html/body/div/div/div[2]/form/button').click()

        # 18. User logs out
        self.browser.find_element_by_xpath('/html/body/div[1]/div/nav/div/div[2]/ul/li[3]/a').click()