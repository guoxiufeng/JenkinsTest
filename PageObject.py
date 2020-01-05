# encoding:utf-8


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):

    login_url = 'http://www.baidu.com/'

    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def open(self):
        url = self.base_url
        self.driver.get(url)
        self.driver.maximize_window()

        title = self.driver.title

        print(title)

    def find_element(self, arg):
        self.driver.implicitly_wait(20)
        return WebDriverWait(self.driver, 30).until(EC.visibility_of(self.driver.find_element(by=arg[0], value=arg[1])))

