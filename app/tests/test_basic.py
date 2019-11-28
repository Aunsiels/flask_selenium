import unittest
from urllib.request import urlopen

from flask_testing import LiveServerTestCase

from app import app

from selenium import webdriver


class BasicTest(LiveServerTestCase):

    browser = None

    def create_app(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
        return app

    def test_server_is_up_and_running(self):
        response = urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Firefox()

    def test_get_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello World!")

    def test_selenium(self):
        self.browser.get("http://example.com")
        print(self.browser.page_source)
        self.assertTrue("html" in self.browser.page_source)

    def test_selenium_on_app(self):
        self.browser.get(self.get_server_url())
        self.assertTrue("Hello World!" in self.browser.page_source)

    def test_login_page_exists(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)

    def test_form_in_login(self):
        self.browser.get(self.get_server_url() + "/login")
        print(self.browser.page_source)
        forms = self.browser.find_elements_by_xpath("//form")
        self.assertEqual(len(forms), 1)

    def test_username_field_in_login_form(self):
        self.browser.get(self.get_server_url() + "/login")
        username_inputs = self.browser.find_elements_by_xpath("//form//input[@type='text' and @name='username']")
        self.assertEqual(len(username_inputs), 1)

    def test_password_field_in_login_form(self):
        self.browser.get(self.get_server_url() + "/login")
        password_inputs = self.browser.find_elements_by_xpath("//form//input[@type='password' and @name='password']")
        self.assertEqual(len(password_inputs), 1)

    def test_submit_field_in_login_form(self):
        self.browser.get(self.get_server_url() + "/login")
        submit_buttons = self.browser.find_elements_by_xpath("//form//input[@type='submit']")
        self.assertEqual(len(submit_buttons), 1)

    def test_click_submit_field_in_login_form(self):
        self.browser.get(self.get_server_url() + "/login")
        submit_button = self.browser.find_elements_by_xpath("//form//input[@type='submit']")[0]
        submit_button.click()
        self.assertEqual(self.browser.current_url, self.get_server_url() + "/login")

    def test_click_submit_field_in_login_form_no_field(self):
        self.browser.get(self.get_server_url() + "/login")
        submit_button = self.browser.find_elements_by_xpath("//form//input[@type='submit']")[0]
        submit_button.click()
        forms = self.browser.find_elements_by_xpath("//form")
        self.assertEqual(len(forms), 1)

    def tearDown(self) -> None:
        self.browser.delete_all_cookies()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main()
