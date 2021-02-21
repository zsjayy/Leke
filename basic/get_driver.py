from selenium import webdriver


class GetDriver:
    driver = None

    # 获取driver
    '''只需要启用一次driver,所以需要使用类属性'''

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 实例化浏览器
            cls.driver = webdriver.Chrome("../tools/chromedriver.exe")
            # 最大化
            cls.driver.maximize_window()
            # 打开浏览器
            cls.driver.get('https://cas.leke.cn/login?service=')
        return cls.driver  # 操作玩之后再会到上面的if判断，保证单例

    # 退出driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:  # driver is not None
            cls.driver.quit()
            cls.driver = None  # 注意关闭之后【一定】要再次将driver置为空
