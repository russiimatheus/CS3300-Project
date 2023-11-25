import time
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UserLoginTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

        # Create a test user
        User.objects.create_user(username='Matheus', password='Mamae30613004!')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_user_login_successful(self):
        self.selenium.get(f'{self.live_server_url}/login/')
        time.sleep(2)

        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password')

        username_input.send_keys('Matheus')
        time.sleep(1)
        password_input.send_keys('Mamae30613004!')
        time.sleep(1)

        password_input.send_keys(Keys.RETURN)
        time.sleep(3)

        # Replace this with an appropriate condition for your application
        # Example: Check if a certain element (like 'logout' link, 'profile' button, etc.) is present
        # self.assertTrue(self.selenium.find_element(By.ID, 'unique-element-after-login'))

    def test_user_login_with_incorrect_password(self):
        self.selenium.get(f'{self.live_server_url}/login/')
        time.sleep(2)

        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password')

        username_input.send_keys('Matheus')
        time.sleep(1)
        password_input.send_keys('WrongPassword!')
        time.sleep(1)

        password_input.send_keys(Keys.RETURN)
        time.sleep(3)

        # Check if the user is still on the login page, indicating login failure
        current_url = self.selenium.current_url
        self.assertIn('/login/', current_url)
