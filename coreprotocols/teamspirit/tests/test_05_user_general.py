# -*- coding: iso-8859-15 -*-
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class Test05UserGeneral(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    # def tearDown(self):
    #     self.browser.quit()

    def test_user_pages_login(self):

        # 1. User can get /user URL
        self.browser.get(self.live_server_url + '/team/signup/')

        # 2. User sees the appropriate page
        self.assertIn('Sign UP', self.browser.title)

        # 3. User fills in Username field
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('user')

        # 4. User fills in Email field
        email_field = self.browser.find_element_by_name('email')
        email_field.send_keys('user@somewhere.com')

        # 5. User fills in Password field
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('m3@nt!m3')

        # 6. User fills in First Name field
        first_name_field = self.browser.find_element_by_name('first_name')
        first_name_field.send_keys('Some')

        # 7. User fills in Last Name field
        last_name_field = self.browser.find_element_by_name('last_name')
        last_name_field.send_keys('One')

        # 8. User clicks on sign up button
        self.browser.find_element_by_xpath('/html/body/div/div/form/input[2]').click()

        # 9. User find themselves on the correct page
        self.assertIn(u'Team\u2605Spirit', self.browser.title)

        # 10. User logs out
        self.browser.find_element_by_xpath('/html/body/div[1]/div/nav/div/div[2]/ul/li[3]/a').click()

        # # 5. Admin types in the username and passwords and hits return
        # username_field = self.browser.find_element_by_name('username')
        # username_field.send_keys('admin')
        #
        # password_field = self.browser.find_element_by_name('password')
        # password_field.send_keys('meantime')
        # password_field.send_keys(Keys.RETURN)
        #
        # # 6. The username and password are accepted, and admin is taken to
        # # the Site Administration page
        # body = self.browser.find_element_by_tag_name('body')
        # self.assertIn('Django administration', body.text)
        #
        # # 7. Admin now sees a hyperlink that says "Groups"
        # groups_links = self.browser.find_elements_by_link_text('Groups')
        # self.assertEquals(len(groups_links), 1)
        #
        # # 8. Admin now sees a hyperlink that says "Users"
        # users_links = self.browser.find_elements_by_link_text('Users')
        # self.assertEquals(len(users_links), 1)
        #
        # # 9. Admin now sees a hyperlink that says "Session states"
        # session_states_links = self.browser.find_elements_by_link_text('Session states')
        # self.assertEquals(len(session_states_links), 1)
        #
        # # 10. Admin now sees a hyperlink that says "Sessions"
        # sessions_links = self.browser.find_elements_by_link_text('Sessions')
        # self.assertEquals(len(sessions_links), 1)
        #
        # # 11. Admin now sees a hyperlink that says "Teams"
        # teams_links = self.browser.find_elements_by_link_text('Teams')
        # self.assertEquals(len(teams_links), 1)
        #
        # # 12. Admin logs out
        # self.browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/a[3]').click()
        #
        # # 13. Admin verifies he is logged out
        # result = self.browser.find_element_by_xpath('/html/body/div/div[3]/h1')
        # self.assertIn('Logged out', result.text)
        #
        #
