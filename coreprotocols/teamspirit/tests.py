# from django.test import TestCase
# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class Test01AdminTestsGeneral(LiveServerTestCase):

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@mysite.com', 'meantime')
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_admin_pages_login(self):

        # 2. Admin can get /admin URL
        self.browser.get(self.live_server_url + '/admin/')

        # 3. Admin sees the appropriate page title
        self.assertIn('Log in | Django site admin', self.browser.title)

        # 4. Admin sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # 5. Admin types in the username and passwords and hits return
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('meantime')
        password_field.send_keys(Keys.RETURN)

        # 6. The username and password are accepted, and admin is taken to
        # the Site Administration page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # 7. Admin now sees a hyperlink that says "Groups"
        groups_links = self.browser.find_elements_by_link_text('Groups')
        self.assertEquals(len(groups_links), 1)

        # 8. Admin now sees a hyperlink that says "Users"
        users_links = self.browser.find_elements_by_link_text('Users')
        self.assertEquals(len(users_links), 1)

        # 9. Admin now sees a hyperlink that says "Session states"
        session_states_links = self.browser.find_elements_by_link_text('Session states')
        self.assertEquals(len(session_states_links), 1)

        # 10. Admin now sees a hyperlink that says "Sessions"
        sessions_links = self.browser.find_elements_by_link_text('Sessions')
        self.assertEquals(len(sessions_links), 1)

        # 11. Admin now sees a hyperlink that says "Teams"
        teams_links = self.browser.find_elements_by_link_text('Teams')
        self.assertEquals(len(teams_links), 1)

        # 12. Admin logs out
        self.browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/a[3]').click()

        # 13. Admin verifies he is logged out
        result = self.browser.find_element_by_xpath('/html/body/div/div[3]/h1')
        self.assertIn('Logged out', result.text)


class Test02AdminTestsAddRemoveUser(LiveServerTestCase):

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@mysite.com', 'meantime')
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url + '/admin/')
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('meantime')
        password_field.send_keys(Keys.RETURN)

    def tearDown(self):
        self.browser.quit()

    def test_admin_add_remove_user(self):
        # 1. Admin Clicks add user button
        self.browser.find_element_by_css_selector('.model-user .addlink').click()

        # 2. Admin sees the user page
        self.assertIn('Add user | Django site admin', self.browser.title)

        # 3. Admin enters username
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('john')

        # 4. Admin enters password1
        inputbox = self.browser.find_element_by_id('id_password1')
        inputbox.send_keys('t3$t!ng123')

        # 5. Admin enters password2
        inputbox = self.browser.find_element_by_id('id_password2')
        inputbox.send_keys('t3$t!ng123')

        # 6. Admin Clicks save
        SAVE_BUTTON_XPATH = '//input[@type="submit" and @value="Save"]'
        button = self.browser.find_element_by_xpath(SAVE_BUTTON_XPATH)
        button.click()

        # 7. Admin receives success dialog
        success = self.browser.find_element_by_css_selector('html body.app-auth.model-user.change-form div#container ul.messagelist li.success')
        self.assertIn('The user "john" was added successfully. You may edit it again below.', success.text)

        # 8. Go back to /admin
        self.browser.get(self.live_server_url + '/admin/')

        # 9. Admin clicks  Change User button
        self.browser.find_element_by_css_selector('.model-user .changelink').click()

        # 10. Admin sees the edit user page
        self.assertIn('Select user to change | Django site admin', self.browser.title)

        # 11. Admin checks box for user "john"
        self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[2]/td[1]/input").click()

        # 12. Admin selects delete user option
        el = self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/label/select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'Delete selected users':
                option.click()
                break

        # 13. Admin clicks the "Go" button to delete the user
        self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/button').click()

        # 14. Admin clicks the "Yes I am sure" button to confirm user deletion
        self.browser.find_element_by_xpath('/html/body/div/div[3]/form/div/input[4]').click()

        # 15. Admin notified that the user has been deleted
        success = self.browser.find_element_by_xpath('/html/body/div/ul/li')
        self.assertIn('Successfully deleted 1 user.', success.text)

class Test03AdminTestsAddRemoveTeam(LiveServerTestCase):

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@mysite.com', 'meantime')
        User.objects.create_user('nick', 'nick@mysite.com', 'meantime')
        User.objects.create_user('truman', 'nick@mysite.com', 'meantime')
        User.objects.create_user('brian', 'nick@mysite.com', 'meantime')
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url + '/admin/')
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('meantime')
        password_field.send_keys(Keys.RETURN)

    def tearDown(self):
        self.browser.quit()

    def test_admin_add_remove_team(self):
        # 1. Admin Clicks add team button
        self.browser.find_element_by_css_selector('.model-team .addlink').click()

        # 2. Admin sees the team page
        self.assertIn('Add team | Django site admin', self.browser.title)

        # 3. Admin selects nick as team owner
        el = self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/fieldset/div[1]/div/div/select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'nick':
                option.click()
                break

        # 4. Admin selects brian and truman as team members
        el = self.browser.find_element_by_id('id_members')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'brian':
                option.click()
            if option.text == 'truman':
                option.click()
                break

        # 5. Admin enters the name "Test Team" for the team
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Test Team')

        # 6. Admin submits to create team
        self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/div/input[1]').click()

        # 7. Admin verifies the team was created successfully
        result = self.browser.find_element_by_xpath('/html/body/div/ul/li')
        self.assertIn('The team "Test Team" was added successfully.', result.text)

        # 8. Admin returns to main admin page
        self.browser.get(self.live_server_url + '/admin/')

         # 9. Admin selects to modify teams
        self.browser.find_element_by_css_selector('.model-team .changelink').click()

        # 10. Admin verifies he is on the change team page
        result = self.browser.find_element_by_xpath('/html/body/div/div[3]/h1')
        self.assertIn('Select team to change', result.text)

        # 11. Admin clicks on the link for "Test Team" team to modify it
        self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a').click()

        # 12. Admin de-selects brian to remove him from the team
        el = self.browser.find_element_by_id('id_members')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'brian':
                option.click()

        # 13. Admin clicks the Save button to modify the team
        self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/div/input[1]').click()

        # 14. Admin returns to main admin page
        self.browser.get(self.live_server_url + '/admin/')

        # 15. Admin selects to modify teams
        self.browser.find_element_by_css_selector('.model-team .changelink').click()

        # 16. Admin verifies he is on the change team page
        result = self.browser.find_element_by_xpath('/html/body/div/div[3]/h1')
        self.assertIn('Select team to change', result.text)

        # 17. Admin checks the box for "Test Team" team
        self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/td').click()

        # 18. Admin selects to delete the team
        el = self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/label/select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'Delete selected teams':
                option.click()
                break

        # 19. Admin clicks the Go button to delete the team
        self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/button').click()

        # 20. Admin gets page to confirm they really wish to delete team
        result = self.browser.find_element_by_xpath('/html/body/div/div[3]/h1')
        self.assertIn('Are you sure?', result.text)

        # 21. Admin clicks to confirm deletion of team
        self.browser.find_element_by_xpath('/html/body/div/div[3]/form/div/input[4]').click()

        # 22. Admin notified the session has been deleted
        success = self.browser.find_element_by_xpath('/html/body/div/ul/li')
        self.assertIn('Successfully deleted 1 team.', success.text)

class Test04AdminTestsAddRemoveSession(LiveServerTestCase):

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@mysite.com', 'meantime')
        User.objects.create_user('nick', 'nick@mysite.com', 'meantime')
        User.objects.create_user('truman', 'nick@mysite.com', 'meantime')
        User.objects.create_user('brian', 'nick@mysite.com', 'meantime')
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url + '/admin/')
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('meantime')
        password_field.send_keys(Keys.RETURN)
        self.browser.find_element_by_css_selector('.model-team .addlink').click()
        el = self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/fieldset/div[1]/div/div/select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'nick':
                option.click()
                break
        el = self.browser.find_element_by_id('id_members')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'brian':
                option.click()
            if option.text == 'truman':
                option.click()
                break
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Test Team')
        self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/div/input[1]').click()
        self.browser.get(self.live_server_url + '/admin/')

    def tearDown(self):
        self.browser.quit()

    def test_admin_add_remove_session(self):
        # 1. Admin clicks to add a new session
        self.browser.find_element_by_css_selector('.model-session .addlink').click()

        # 2. Admin sees the session page
        self.assertIn('Add session | Django site admin', self.browser.title)

        # 3. Admin selects "Test Team" to add the session to
        el = self.browser.find_element_by_id('id_team')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'Test Team':
                option.click()
                break

        # 4. Admin enters "Test Session" as the session name
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Test Session')

        # 5. Admin clicks "Save"
        self.browser.find_element_by_xpath('/html/body/div/div[3]/div/form/div/div/input[1]').click()

        # 6. Admin checks to make sure "Test Session" was create successfully
        result = self.browser.find_element_by_xpath('/html/body/div/ul/li')
        self.assertIn('The session "Test Session" was added successfully.', result.text)

        # 7. Admin navigates to main /admin page
        self.browser.get(self.live_server_url + '/admin/')

        # 8. Admin selects to modify sessions
        self.browser.find_element_by_css_selector('.model-session .changelink').click()

        # 16. Admin verifies he is on the change session page
        result = self.browser.find_element_by_xpath('/html/body/div/div[3]/h1')
        self.assertIn('Select session to change', result.text)

        # 17. Admin checks the box for "Test Session" team
        self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/td/input').click()

        # 18. Admin selects to delete the session
        el = self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/label/select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'Delete selected sessions':
                option.click()
                break

        # 19. Admin clicks the Go button to delete the session
        self.browser.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/button').click()

        # 20. Admin gets page to confirm they really wish to delete session
        result = self.browser.find_element_by_xpath('/html/body/div/div[3]/h1')
        self.assertIn('Are you sure?', result.text)

        # 21. Admin clicks to confirm deletion of session
        self.browser.find_element_by_xpath('/html/body/div/div[3]/form/div/input[4]').click()

        # 22. Admin notified the session has been deleted
        success = self.browser.find_element_by_xpath('/html/body/div/ul/li')
        self.assertIn('Successfully deleted 1 session.', success.text)