# from django.test import TestCase
# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User


# class Test04UserAddRemoveSession(LiveServerTestCase):
#
#     def setUp(self):
#         User.objects.create_superuser('admin', 'admin@mysite.com', 'meantime')
#         User.objects.create_user('nick', 'nick@mysite.com', 'meantime')
#         User.objects.create_user('truman', 'nick@mysite.com', 'meantime')
#         User.objects.create_user('brian', 'nick@mysite.com', 'meantime')
#         self.browser = webdriver.Firefox()
#         self.browser.implicitly_wait(3)
#         self.browser.get(self.live_server_url + '/admin/')
#         username_field = self.browser.find_element_by_name('username')
#         username_field.send_keys('admin')
#         password_field = self.browser.find_element_by_name('password')
#         password_field.send_keys('meantime')
#         password_field.send_keys(Keys.RETURN)
#         self.browser.find_element_by_css_selector('.model-team .addlink').click()
#         el = self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/fieldset/div[1]/div/div/select')
#         for option in el.find_elements_by_tag_name('option'):
#             if option.text == 'nick':
#                 option.click()
#                 break
#         el = self.browser.find_element_by_id('id_members')
#         for option in el.find_elements_by_tag_name('option'):
#             if option.text == 'brian':
#                 option.click()
#             if option.text == 'truman':
#                 option.click()
#                 break
#         inputbox = self.browser.find_element_by_id('id_name')
#         inputbox.send_keys('Test Team')
#         self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/div/input[1]').click()
#         self.browser.get(self.live_server_url + '/admin/')
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_user_add_remove_session(self):
#         # 1. User clicks to add a new session
#         self.browser.find_element_by_css_selector('.model-session .addlink').click()
#
#         # 2. User sees the session page
#         self.assertIn('Add session | Django site admin', self.browser.title)
#
#         # 3. User selects "Test Team" to add the session to
#         el = self.browser.find_element_by_id('id_team')
#         for option in el.find_elements_by_tag_name('option'):
#             if option.text == 'Test Team':
#                 option.click()
#                 break
#
#         # 4. User enters "Test Session" as the session name
#         inputbox = self.browser.find_element_by_id('id_name')
#         inputbox.send_keys('Test Session')
#
#         # 5. User clicks "Save"
#         self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/div/input[1]').click()
#
#         # 6. User checks to make sure "Test Session" was create successfully
#         result = self.browser.find_element_by_xpath('/html/body/div/ul/li')
#         self.assertIn('The session "Test Session" was added successfully.', result.text)
#
#         # 7. User navigates to main /User page
#         self.browser.get(self.live_server_url + '/admin/')
#
#         # 8. User selects to modify sessions
#         self.browser.find_element_by_css_selector('.model-session .changelink').click()
#
#         # 16. User verifies he is on the change session page
#         result = self.browser.find_element_by_xpath('/html/body/div/div[3]/h1')
#         self.assertIn('Select session to change', result.text)
#
#         # 17. User checks the box for "Test Session" team
#         self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/td/input').click()
#
#         # 18. User selects to delete the session
#         el = self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/label/select')
#         for option in el.find_elements_by_tag_name('option'):
#             if option.text == 'Delete selected sessions':
#                 option.click()
#                 break
#
#         # 19. User clicks the Go button to delete the session
#         self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/button').click()
#
#         # 20. User gets page to confirm they really wish to delete session
#         result = self.browser.find_element_by_xpath('/html/body/div/div[3]/h1')
#         self.assertIn('Are you sure?', result.text)
#
#         # 21. User clicks to confirm deletion of session
#         self.browser.find_element_by_xpath('/html/body/div/div[3]/form/div/input[4]').click()
#
#         # 22. User notified the session has been deleted
#         success = self.browser.find_element_by_xpath('/html/body/div/ul/li')
#         self.assertIn('Successfully deleted 1 session.', success.text)