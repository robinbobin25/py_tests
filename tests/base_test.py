from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure
from allure_commons.types import AttachmentType

class TestGoogleSearch:

    def setup(self):
        #create a new Chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    @allure.feature('Open pages')
    @allure.story('Open Google')
    def test_google_search(self):
        self.driver.get("https://www.google.com")
        with allure.step("Screenshot shoot"):
            allure.attach(self.driver.get_screenshot_as_png(), name="pic", attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Google'

    def teardown(self):
        self.driver.quit()