# from django.test import TestCase
# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User


class Test03AdminAddRemoveTeam(LiveServerTestCase):

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


