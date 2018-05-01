"""
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# add geckodriver to path, unix with following
# wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
# tar -xvzf geckodriver-v0.18.0-linux64.tar.gz
# chmod +x geckodriver
# export PATH=$PATH:/path-to-extracted-file/geckodriver
class ViewsIntegrationTest(LiveServerTestCase):

	def setUp(self):
		self.selenium = webdriver.Firefox()

	def tearDown(self):
		self.selenuim.quit()

	def test_register(self):
		
		selenium = self.selenium

		selenium.get('http://127.0.0.1:8000/admin/')

		user_name = selenium.find_element_by_id('id_username')
		password = selenium.find_element_by_id('id_password')

		log_in = selenium.find_element_by_css_selector('.submit-row')

		user_name.send_keys('clock')
		password.send_keys('clock383')
		log_in.send_keys(Keys.RETURN)
		"""