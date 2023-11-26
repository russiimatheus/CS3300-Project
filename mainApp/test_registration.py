import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UserRegistrationTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_user_registration_successful(self):
        self.selenium.get(f'{self.live_server_url}/register/')
        time.sleep(2)

        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password1')
        password_repeat_input = self.selenium.find_element(By.NAME, 'password2')

        username_input.send_keys('newuser')
        password_input.send_keys('ValidPassword123')
        password_repeat_input.send_keys('ValidPassword123')
        time.sleep(1)

        
        self.selenium.find_element(By.CSS_SELECTOR, 'form button').click()
        time.sleep(3)

        current_url = self.selenium.current_url
        self.assertIn('/login/', current_url)  

    def test_user_registration_unsuccessful(self):
        self.selenium.get(f'{self.live_server_url}/register/')
        time.sleep(2)

       
        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password1')
        password_repeat_input = self.selenium.find_element(By.NAME, 'password2')

        username_input.send_keys('newuser')
        password_input.send_keys('pwd')
        password_repeat_input.send_keys('pwd')
        time.sleep(1)

        
        self.selenium.find_element(By.CSS_SELECTOR, 'form button').click()
        time.sleep(3)

        errors = self.selenium.find_elements(By.CLASS_NAME, 'error')
        self.assertTrue(len(errors) > 0)
