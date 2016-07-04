from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from teamspirit.models import Team


class Test04UserAddRemoveSession(LiveServerTestCase):

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@mysite.com', 'meantime')
        nick = User.objects.create_user('nick', 'nick@mysite.com', 'meantime')
        truman=User.objects.create_user('truman', 'nick@mysite.com', 'meantime')
        brian=User.objects.create_user('brian', 'nick@mysite.com', 'meantime')
        # Team.objects.create(owner=nick, name='Test Team', members=[nick, truman, brian])
        team = Team()
        team.owner=nick
        team.name="Test Team"
        team.save()
        team.members.add(nick.id, truman.id, brian.id)

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

        # self.browser.get(self.live_server_url + '/admin/')
        # username_field = self.browser.find_element_by_name('username')
        # username_field.send_keys('admin')
        # password_field = self.browser.find_element_by_name('password')
        # password_field.send_keys('meantime')
        # password_field.send_keys(Keys.RETURN)
        # self.browser.find_element_by_css_selector('.model-team .addlink').click()
        # el = self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/fieldset/div[1]/div/div/select')
        # for option in el.find_elements_by_tag_name('option'):
        #     if option.text == 'nick':
        #         option.click()
        #         break
        # el = self.browser.find_element_by_id('id_members')
        # for option in el.find_elements_by_tag_name('option'):
        #     if option.text == 'brian':
        #         option.click()
        #     if option.text == 'truman':
        #         option.click()
        #         break
        # inputbox = self.browser.find_element_by_id('id_name')
        # inputbox.send_keys('Test Team')
        # self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/div/input[1]').click()
        # self.browser.get(self.live_server_url + '/admin/')
#
#     def tearDown(self):
#         self.browser.quit()
#
    def test_user_add_remove_session(self):

        # 1. User goes to main page
        self.browser.get(self.live_server_url + '/')

        # 2. User selects to Sign In
        self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/p[2]/a[2]').click()

        # 3. User enters username
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('nick')

        # 4. User enters password
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('meantime')

        # 5. User clicks to Sign In button
        self.browser.find_element_by_xpath('/html/body/div/div/div[2]/form/button').click()

        # 1. User clicks to add a new session
        self.browser.find_element_by_xpath('/html/body/div[2]/div/div/ul[1]/a[2]').click()

        # 2. User sees the session page
        self.assertIn('Add Session To Team', self.browser.title)

        # 4. User enters "Test Session" as the session name
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Test Session')

        # 5. User clicks "Submit"
        self.browser.find_element_by_xpath('/html/body/div/div/div/form/input[2]').click()

        # 6. User checks to make sure "Test Session" was create successfully
        result = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/ul[1]/ul[2]/li')
        self.assertIn('Test Session', result.text)

        # 7. User closes session
        self.browser.find_element_by_xpath('/html/body/div[2]/div/div/ul[1]/ul[2]/li/button').click()
        
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