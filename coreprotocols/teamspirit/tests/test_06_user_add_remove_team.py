from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class Test06UserAddRemoveTeam(LiveServerTestCase):

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@mysite.com', 'meantime')
        User.objects.create_user('nick', 'nick@mysite.com', 'meantime')
        User.objects.create_user('truman', 'nick@mysite.com', 'meantime')
        User.objects.create_user('brian', 'nick@mysite.com', 'meantime')
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url + '/')

    def tearDown(self):
        self.browser.quit()

    def test_user_add_remove_team(self):

        # 1. User is prompted to sign in
        self.assertIn(u'Team\u2605Spirit', self.browser.title)

        # 2. User clicks to Sign In button
        self.browser.find_element_by_id('id_signin').click()

        # 3. User fills in Username field
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('nick')

        # 4. User fills in Password field
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('meantime')

        # 5. User clicks Sign In button
        self.browser.find_element_by_id('id_signin').click()

        # 6. User Clicks create team button
        self.browser.find_element_by_xpath('/html/body/div/div[2]/div/nav/div/div[2]/ul/li[2]/a').click()

        # 7. User is on the Create Team page
        result = self.browser.find_element_by_xpath('/html/body/div/div[2]/div/div/h3')
        self.assertIn('Create Team', result.text)

        # 8. User enters team name
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Test Team')

        # 9. User hits Submit to create team
        self.browser.find_element_by_xpath('/html/body/div/div[2]/div/div/form/input[3]').click()

        # 10. User gets page to add team members
        result = self.browser.find_element_by_xpath('/html/body/div/div/div/h3')
        self.assertIn('Add Members To Team: Test Team', result.text)

        # 11. User selects brian and truman as team members
        el = self.browser.find_element_by_id('id_members')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'brian':
                option.click()
            if option.text == 'truman':
                option.click()

        # 12. User presses Submit button
        self.browser.find_element_by_xpath('/html/body/div/div/div/form/input[2]').click()

        # 13. User presses Cancel to bypass creating a session
        self.browser.find_element_by_xpath('/html/body/div/div[2]/div/div/a/button').click()

        # 14. User checks to see if Team is listed as one they own
        result = self.browser.find_element_by_xpath('/html/body/div/div[2]/div/ul/li[2]/ul/li/a')
        self.assertIn('Test Team', result.text)



        # 16. User selects to modify teams
        self.browser.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[1]/div/div[1]/a[1]').click()

        # 17. User verifies he is on the change team page
        result = self.browser.find_element_by_xpath('/html/body/div/div/div/h3')
        self.assertIn('Add Members To Team: Test Team', result.text)

        # 18. User de-selects brian to remove him from the team
        el = self.browser.find_element_by_id('id_members')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'brian':
                option.click()

        # 19. User presses Cancel button to cancel out of creating a session
        self.browser.find_element_by_xpath('/html/body/div/div/div/a/button').click()
