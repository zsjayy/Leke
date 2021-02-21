from basic.get_driver import GetDriver
import page

class PageLogin(GetDriver):

<<<<<<< HEAD
    def page_login_input_username(self):
=======
    def page_input_username(self):
>>>>>>> 9148a8f73a2ae7d4de39b67b9ae201b0273784d9
        self.driver.find_element_by_id("loginName").send_keys('3168399')

    def page_login_input_password(self):
        self.driver.find_element_by_id("password").send_keys('leke1234')

    def page_login_login_button(self):
        self.driver.find_element_by_id("j-sign-on").click()
