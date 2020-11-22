from basic.get_driver import GetDriver
from page.page_login import PageLogin


class Login(PageLogin):

    def login(self):
        self.driver.get('https://cas.leke.cn/login?service=')
        self.get_driver()
        self.page_input_username()
        self.page_input_password()
        self.page_login_button()


run = Login()
run.login()
