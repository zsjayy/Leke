from basic.get_driver import GetDriver


class PageLogin(GetDriver):

    def page_input_username(self):
        self.driver.find_element_by_id("loginName").send_keys('2525545')

    def page_input_password(self):
        self.driver.find_element_by_id("password").send_keys('leke1234')

    def page_login_button(self):
        self.driver.find_element_by_id("j-sign-on").click()
