import Page
from selenium.webdriver.common.by import By
import allure
from Base.Base import Base
import pytest, sys, os

sys.path.append(os.getcwd())
import random

class gongdan(Base):
    def __init__(self, deiver):
        Base.__init__(self, deiver)

    # 登录采集车源账号
    def input_login(self, name="10000000145", passwo="uat.portal"):
        allure.attach("用户登陆信息：", "用户名:%s\n密码:%s" % (name, passwo))
        self.input_element(Page.username, name)
        self.input_element(Page.password, passwo)

    # 点击登录按钮
    def click_login(self):
        self.click_element(Page.login)

    # 点击取消更新按钮
    def click_cy_qx(self):
        self.click_element(Page.cancel)

