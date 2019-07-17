from linkedin_scraper import Person, actions
from selenium import webdriver

class LiExp:

    def __init__(self, url):
        self.url = url

    def li_login_scrape(self):
        driver = webdriver.Chrome('/path/to/chromedriver.exe')
        email = 'your-emaail@email.com'
        password = '********'
        actions.login(driver, email, password)
        driver.get(self.url)
        experience = driver.find_elements_by_css_selector('#experience-section .pv-profile-section')
        for item in experience:
            print(item.text)
        return experience
