from selenium import webdriver
from config import CHROME_PROFILE_PATH, CHROME_PROFILE_NAME


options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir={}'.format(CHROME_PROFILE_PATH))
options.add_argument(r'--profile-directory={}'.format(CHROME_PROFILE_NAME)) #e.g. Profile 3
cService = webdriver.ChromeService(executable_path='selenium_utils/chromedriver')
driver = webdriver.Chrome(service=cService, options=options)