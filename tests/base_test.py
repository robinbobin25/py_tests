from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com")

#clovz
driver.quit()