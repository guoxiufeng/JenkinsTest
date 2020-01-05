# encoding:utf-8


from PageObject import Page
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver import ActionChains
import imageio
from PIL import ImageGrab
import time
import Gloabl_var
from jinja2 import Environment, FileSystemLoader


class LoginPage(Page):
    login_link = (By.XPATH, '//div[@id="u1"]//a[@name="tj_login"]')
    username_loc = (By.XPATH, '//input[@name="userName"]')
    password_loc = (By.XPATH, '//input[@name="password"]')
    loginpage_exist = (By.XPATH, '//p[contains(text(),"用户名密码登录")]')
    login_button = (By.XPATH, '//p[contains(text(),"用户名密码登录")]/following-sibling::p[last()]/input')
    start_element = (By.XPATH, '//div[@class="vcode-slide-button"]')
    end_element = (By.XPATH, '//div[@class="vcode-slide-bottom"]')

    def click_login_link(self):
        self.find_element(self.login_link).click()

    def type_username(self, username):
        result = self.find_element(self.loginpage_exist).is_displayed()
        print(result)
        if result:
            self.find_element(self.username_loc).send_keys(username)
        else:
            exit()

    def type_password(self, password):
        self.find_element(self.password_loc).send_keys(password)

    def click_login_button(self):
        self.find_element(self.login_button).click()
        # self.driver.get_screenshot_as_file(Gloabl_var.picture_path + '/' + time.strftime('%Y%m%d%H%M%S%f', time.localtime(time.time())) + '.png')
        ImageGrab.grab().save(Gloabl_var.picture_path + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".png")
        #start = self.find_element(self.start_element)
        #end = self.find_element(self.end_element)
        #print(start.location)
        #print(end.location)
        #print(start.size)
        #print(end.size)
        time.sleep(1)
        # ActionChains(self.driver).drag_and_drop(start, end).perform()
        #ImageGrab.grab().save(Gloabl_var.picture_path + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".png")
        #action = ActionChains(self.driver)
        #action.click_and_hold(start).perform()
       # action.drag_and_drop_by_offset(start, 210, 0).perform()
        ImageGrab.grab().save(Gloabl_var.picture_path + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".png")
        time.sleep(0.6)


class LoginOut(Page):
    loginout_link = (By.XPATH, '//div[@id="u_sp"]//span[@class="user-name"]')
    quit_link = (By.XPATH, '//div[@id="s_user_name_menu"]//a[@class="quit"]')
    loginout_confirm = (By.XPATH, '//a[contains(text(),"确定")]')

    def logout(self):
        logout_element = self.find_element(self.loginout_link)
        action = ActionChains(self.driver)
        action.move_to_element(logout_element).perform()
        ImageGrab.grab().save(Gloabl_var.picture_path + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".png")
        quit_element = self.find_element(self.quit_link)
        quit_element.click()
        ImageGrab.grab().save(Gloabl_var.picture_path + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".png")
        self.find_element(self.loginout_confirm).click()


def test_user_login(driver, username, password):

        login_page = LoginPage(driver)
        login_page.open()
        ImageGrab.grab().save(Gloabl_var.picture_path + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".png")

        login_page.click_login_link()
        ImageGrab.grab().save(Gloabl_var.picture_path + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".png")

        login_page.type_username(username)
        ImageGrab.grab().save(Gloabl_var.picture_path + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".png")

        login_page.type_password(password)
        ImageGrab.grab().save(Gloabl_var.picture_path + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".png")

        login_page.click_login_button()
        ImageGrab.grab().save(Gloabl_var.picture_path + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".png")


def test_log_out(driver):
    log_out = LoginOut(driver)
    log_out.logout()


def create_gif(source, name, duration):
        frames = []
        for img in source:
            frames.append(imageio.imread(Gloabl_var.picture_path + '/' + img))
        imageio.mimsave(name, frames, duration = duration)


def generate_html(body, starttime, stoptime):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('template.html')
    with open(Gloabl_var.picture_path + './' + Gloabl_var.result_pathname + '.html', 'w+') as fout:
        html_content = template.render(start_time=starttime, stop_time=stoptime, body=body)
        fout.write(html_content)


