# from django.test import TestCase
# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User


class Test02AdminAddRemoveUser(LiveServerTestCase):

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
