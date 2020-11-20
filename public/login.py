from basic.get_driver import GetDriver
import time


class Login(GetDriver):

    def login(self):
        self.get_driver()
        url = 'https://cas.leke.cn/login?service='
        self.driver.get(url)
        time.sleep(3)
        self.driver.find_element_by_id("loginName").send_keys('2525545')
        self.driver.find_element_by_id("password").send_keys('leke1234')
        self.driver.find_element_by_id("j-sign-on").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("close--2npdy").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='pageHome']/div/div[3]/div[1]/span/span/span").click()


run = Login()
run.login()
