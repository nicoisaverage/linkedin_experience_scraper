from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome('/path/to/chromedriver.exe')
email = 'email address'
password = 'linkedin password'
actions.login(driver, email, password)
driver.get('linkedin user url')
experience = driver.find_elements_by_css_selector('#experience-section .pv-profile-section')
for item in experience:
    print(item.text)
    print("")
