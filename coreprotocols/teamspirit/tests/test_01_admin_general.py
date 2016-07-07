# from django.test import TestCase
# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class Test01AdminGeneral(LiveServerTestCase):

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


