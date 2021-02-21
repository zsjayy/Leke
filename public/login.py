import time

from basic.get_driver import GetDriver
from page.page_login import PageLogin


class PLogin:
    # 设置driver属性
    driver = None

    def __init__(self):
        # 调用driver驱动
        self.driver = GetDriver().get_driver()
        # 实例化 获取页面对象PageLogin
        self.login = PageLogin()

    def P_login(self):
        # 调用登录方法
        time.sleep(3)
        self.login.page_login_input_username()
        self.login.page_login_input_password()
        self.login.page_login_login_button()


run = PLogin()
run.P_login()
