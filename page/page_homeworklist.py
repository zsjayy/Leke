from basic.get_driver import GetDriver


class PageHomeworkList(GetDriver):

    def page_homeworklist_home_button(self):
        self.driver.find_element_by_path('//*[@id="pageHome"]/div/div[2]/div/ul/li[4]/div/p').click()

    def page_homeworklist_homeworklist_tab(self):
        self.driver.find_element_by_link_text('作业管理').click()

    def page_homeworklist_voicecenter_tab(self):
        self.driver.find_element_by_link_text('口语中心').click()

    def page_homeworklist_assigment_button(self):
        self.driver.find_element_by_class_name('button_3Ym-z').click()