from basic.get_driver import GetDriver
import page

class PageLogin(GetDriver):

    def page_login_input_username(self):
        self.driver.find_element_by_id("loginName").send_keys('3168399')

    def page_login_input_password(self):
        self.driver.find_element_by_id("password").send_keys('leke1234')

    def page_login_login_button(self):
        self.driver.find_element_by_id("j-sign-on").click()
