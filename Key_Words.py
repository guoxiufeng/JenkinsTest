# encoding:utf-8


from selenium import webdriver
import Common
import time
import datetime
from PIL import ImageGrab
import Gloabl_var


driver = webdriver.Ie()


def login(username, password):

        Common.test_user_login(driver, username, password)
        time.sleep(3)
        ImageGrab.grab().save(Gloabl_var.picture_path + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".png")


def log_out():

    Common.test_log_out(driver)
    ImageGrab.grab().save(Gloabl_var.picture_path + '/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + ".png")
