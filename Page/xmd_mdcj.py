import Page
from Base.Base import Base
from selenium.webdriver.common.by import By
import allure
import pytest, sys, os

sys.path.append(os.getcwd())


# 随机生成门店编码
class search1(Base):
    import random, string

    upper = random.sample(string.ascii_uppercase, 6)
    res = ''.join(upper)

    # 获取base
    def __init__(self, deiver):
        Base.__init__(self, deiver)

    # 输入采集账号
    def import_login(self, name="10000000145", passsword="uat.portal"):
        allure.attach("用户登陆信息：", "用户名:%s\n密码:%s" % (name, passsword))
        self.input_element(Page.username, name)
        self.input_element(Page.password, passsword)

    # 点击登录按钮
    def click_login(self):
        self.click_element(Page.lohin)

    # 点击取消更新
    def click_bgx(self):
        self.click_element(Page.cancel)

    # 点击门店采集入口
    def click_mdcj(self):
        self.click_element(Page.mdcj)
        self.click_element(Page.cjjai)

    # 输入门店名称
    def input_md_mame(self, ma_name="自动化测试", md_mb=res):
        allure.attach("采集门店信息：", "门店名称:%s\n门店段编码:%s" % (ma_name, md_mb))
        self.input_element(Page.mdmc, ma_name)
        self.input_element(Page.bm, md_mb)

    # 拍摄门头照片
    def click_mdzp(self, ):
        a = self.search_elements(Page.mtxj)
        a[0].click()

    # 点击快门
    def click_xzzp(self):
        self.click_element(Page.xjkm)
        self.click_element(Page.gouzp)
        # 门店位置定位

    def click_gzp(self):
        self.click_element(Page.xxdz)
        c = self.search_elements(Page.wizhi)
        c[0].click()
        self.click_element(Page.okwz)

    # 补充位置填写
    def input_pcwz(self, weizhi="自动化测试门店"):
        allure.attach("位置补充信息:", "{}".format(weizhi))
        self.input_element(Page.wzbc, weizhi)

    # 选择所在市场
    def click_szsh(self):
        self.click_element(Page.sssh)
        self.click_element(Page.xzsc)

    # 填写车位数
    def input_cws(self, cwsl="99"):
        allure.attach("车位数量:", "{}个车位".format(cwsl))
        self.input_element(Page.cws, cwsl)

    # 车位拍摄入口
    def click_cwrk(self):
        b = self.search_elements(Page.mtxj)
        b[1].click()

    # 输入名字数
    def input_name(self, mdname="自动化"):
        allure.attach("门店联系人名字:", "{}".format(mdname))
        self.input_element(Page.name, mdname)

    # 输入手机号
    def input_cal(self, sjh="17689551930"):
        allure.attach("门店联系人手机号:", "门店联系手机号{}".format(sjh))
        self.input_element(Page.cal, sjh)

    # 选择是否是老板
    def clicj_lb(self):
        self.click_element(Page.sflb)
        self.click_element(Page.yes)

    # 屏幕向上滑动
    def hd(self):
        self.aaa(12)

    # 点击保存
    def click_bc(self):
        self.click_element(Page.baoc)

    # 断言toast消息
    @allure.step(title="获取toast消息")
    def get_toasts(self, message, yuqi):
        self.get_toast(message, yuqi)

    # 点击返回
    def click_fh(self):
        self.click_element(Page.fanhui)

    # 退出登录
    def click_esc(self):
        self.click_element(Page.my)
        self.click_element(Page.esc)
