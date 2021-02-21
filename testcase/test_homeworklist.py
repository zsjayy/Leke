from basic.get_driver import GetDriver
from page.page_homeworklist import PageHomeworkList
from public.login import PLogin
import time


class TestHomeworklist:

    driver = None

    @classmethod
    def setup(cls):
        cls.driver = GetDriver().get_driver()
        cls.Phomeworklist = PageHomeworkList()

    @classmethod
    def teardown(cls):
        GetDriver().quit_driver()

    def test_assignment_button_is_successful(self):
        PLogin().P_login()
        time.sleep(2)
        self.Phomeworklist.page_homeworklist_home_button()
        self.Phomeworklist.page_homeworklist_assigment_button()


run = TestHomeworklist()
run.test_assignment_button_is_successful()
