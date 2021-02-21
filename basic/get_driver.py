from selenium import webdriver
import time


class GetDriver(object):

    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome(r'..\tools\chromedriver.exe')

    def get_driver(self):
        self.driver.maximize_window()


