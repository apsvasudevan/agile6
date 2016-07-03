# from django.test import TestCase
# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User


class Test03UserAddRemoveTeam(LiveServerTestCase):

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@mysite.com', 'meantime')
        User.objects.create_user('nick', 'nick@mysite.com', 'meantime')
        User.objects.create_user('truman', 'nick@mysite.com', 'meantime')
        User.objects.create_user('brian', 'nick@mysite.com', 'meantime')
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url + '/')

#     def tearDown(self):
#         self.browser.quit()

    def test_user_add_remove_team(self):

        # 1. User Clicks create team button
        self.browser.find_element_by_xpath('/html/body/div[1]/div/nav/div/div[2]/ul/li[2]/a').click()

        # 2. User is prompted to sign in
        self.assertIn(u'Team\u2605Spirit', self.browser.title)

        # 3. User fills in Username field
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('nick')

        # 4. User fills in Password field
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('meantime')

        # 5. User clicks Sign In button
        self.browser.find_element_by_xpath('/html/body/div/div/div[2]/form/button').click()

        # 6. User is on the Create Team page
        result = self.browser.find_element_by_xpath('/html/body/div/div/div/h3')
        self.assertIn('Create Team', result.text)

        # 7. User enters team name
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Test Team')

        # 8. User hits Submit to create team
        self.browser.find_element_by_xpath('/html/body/div/div/div/form/input[2]').click()

        # 9. User gets page to add team members
        result = self.browser.find_element_by_xpath('/body/div/h3')
        self.assertIn('Add Members To Team: Test Team', result.text)

#         # 3. User selects nick as team owner
#         el = self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/fieldset/div[1]/div/div/select')
#         for option in el.find_elements_by_tag_name('option'):
#             if option.text == 'nick':
#                 option.click()
#                 break
#
        # 10. User selects brian and truman as team members
        el = self.browser.find_element_by_id('id_members')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'brian':
                option.click()
            if option.text == 'truman':
                option.click()
                break

        # 11. User presses Submit button
        self.browser.find_element_by_xpath('/html/body/div/form/input[2]').click()


#
#         # 7. User verifies the team was created successfully
#         result = self.browser.find_element_by_xpath('/html/body/div/ul/li')
#         self.assertIn('The team "Test Team" was added successfully.', result.text)
#
#         # 8. User returns to main User page
#         self.browser.get(self.live_server_url + '/admin/')
#
#          # 9. User selects to modify teams
#         self.browser.find_element_by_css_selector('.model-team .changelink').click()
#
#         # 10. User verifies he is on the change team page
#         result = self.browser.find_element_by_xpath('/html/body/div/div[3]/h1')
#         self.assertIn('Select team to change', result.text)
#
#         # 11. User clicks on the link for "Test Team" team to modify it
#         self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a').click()
#
#         # 12. User de-selects brian to remove him from the team
#         el = self.browser.find_element_by_id('id_members')
#         for option in el.find_elements_by_tag_name('option'):
#             if option.text == 'brian':
#                 option.click()
#
#         # 13. User clicks the Save button to modify the team
#         self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/div/input[1]').click()
#
#         # 14. User returns to main User page
#         self.browser.get(self.live_server_url + '/admin/')
#
#         # 15. User selects to modify teams
#         self.browser.find_element_by_css_selector('.model-team .changelink').click()
#
#         # 16. User verifies he is on the change team page
#         result = self.browser.find_element_by_xpath('/html/body/div/div[3]/h1')
#         self.assertIn('Select team to change', result.text)
#
#         # 17. User checks the box for "Test Team" team
#         self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/td').click()
#
#         # 18. User selects to delete the team
#         el = self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/label/select')
#         for option in el.find_elements_by_tag_name('option'):
#             if option.text == 'Delete selected teams':
#                 option.click()
#                 break
#
#         # 19. User clicks the Go button to delete the team
#         self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/button').click()
#
#         # 20. User gets page to confirm they really wish to delete team
#         result = self.browser.find_element_by_xpath('/html/body/div/div[3]/h1')
#         self.assertIn('Are you sure?', result.text)
#
#         # 21. User clicks to confirm deletion of team
#         self.browser.find_element_by_xpath('/html/body/div/div[3]/form/div/input[4]').click()
#
#         # 22. User notified the session has been deleted
#         success = self.browser.find_element_by_xpath('/html/body/div/ul/li')
#         self.assertIn('Successfully deleted 1 team.', success.text)
#
