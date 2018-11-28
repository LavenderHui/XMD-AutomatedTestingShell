import Page
from selenium.webdriver.common.by import By
import allure
from Base.Base import Base
import pytest, sys, os

sys.path.append(os.getcwd())
import random

# 随机生成vin码
seed = "1234567890ABCDEFGHLJKMNPRSTUVWXYZ"
sa = []
for i in range(17):
    sa.append(random.choice(seed))
salt = ''.join(sa)


class search(Base):
    # 生成随机vin码
    # 获取base
    def __init__(self, deiver):
        Base.__init__(self, deiver)

    # 登录采集车源账号
    def input_login(self, name="10000000145", passwo="uat.portal"):
        allure.attach("用户登陆信息：", "用户名:%s\n密码:%s" % (name, passwo))
        self.input_element(Page.username, name)
        self.input_element(Page.password, passwo)

    # 点击登录按钮
    def click_login(self):
        self.click_element(Page.lohin)

    # 点击取消更新按钮
    def click_cy_qx(self):
        self.click_element(Page.cancel)

    # 点击采集
    def clcick_rk(self):
        self.click_element(Page.cjrk)
        self.click_element(Page.jia)

    # 点击搜索
    def click_ss(self):
        self.click_element(Page.ss)

    # 选择门店列表第一个门店点击确定
    def click_md(self):
        md = self.search_elements(Page.xzmd)
        allure.attach("选择的门店是:", "{}".format(md[0].text))
        md[0].click()

    def click_okan(self):
        self.click_element(Page.okan)

    # 点击相机
    def click_xj(self):
        a = self.search_elements(Page.mtxj)
        a[0].click()

    def click_km(self):
        self.click_element(Page.xjkm)
        self.click_element(Page.gouzp)

    # 点击拍照按钮
    def click_ok(self):
        self.click_element(Page.vinkm)

    # 不识别vin
    def click_fou(self):
        self.click_element(Page.fou)

    # 选择车型
    def click_cx(self):
        self.click_element(Page.cx1)
        cpp1 = self.search_element(Page.cx2)
        allure.attach("车型选择信息：", "选择的车型:%s" % (cpp1.text))
        cpp1.click()
        cpp2 = self.search_element(Page.cx3)
        cpp2.click()
        cpp3 = self.search_element(Page.cx4)
        cpp3.click()

    # 输入表显里数以及vin
    def input_bxl(self, a="14", c=salt):
        allure.attach("采集车源信息：", "表显里程:%s万公里\n车源vin码:%s" % (a, c))
        self.input_element(Page.bxls, a)
        self.input_element(Page.vinsr, c)

    # 点击表显里程相机
    def ckick_bxxj(self):
        bcxj = self.search_elements(Page.mtxj)
        bcxj[1].click()

    # 点击车源照片相机
    def ckick_cyxj(self):
        bcxj = self.search_elements(Page.mtxj)
        bcxj[2].click()

    # 封面：左前45度
    def click_clzp1(self):
        self.click_element(Page.clzp1)

    # 点击快门
    def click_clzpkm(self):
        self.click_element(Page.clzp1KM)

    def click_clzp2(self):
        self.click_element(Page.clzp2)
        # 点击自己拍摄

    def click_xzxj(self):
        self.click_element(Page.xzxj)

    def click_clzp3(self):
        self.click_element(Page.clzp3)

    def click_clzp4(self):
        self.click_element(Page.clzp4)

    def click_clzp5(self):
        self.click_element(Page.clzp5)

    def click_clzp6(self):
        self.click_element(Page.clzp6)

    def click_clzp7(self):
        self.click_element(Page.clzp7)

    def click_clzp8(self):
        self.click_element(Page.clzp8)

    def click_clzp9(self):
        self.click_element(Page.clzp9)

    def click_clzp10(self):
        self.click_element(Page.clzp10)

    def click_clzp11(self):
        self.click_element(Page.clzp11)

    def click_clzp12(self):
        self.click_element(Page.clzp12)

    def click_clzp13(self):
        self.click_element(Page.clzp13)

    def click_clzp14(self):
        self.click_element(Page.clzp14)

    def click_clzp15(self):
        self.click_element(Page.clzp15)

    def click_clzp16(self):
        self.click_element(Page.clzp16)

    def click_wanc(self):
        self.click_element(Page.wanc)

    def click_fanhui(self):
        self.click_element(Page.fanhui)

    # 选择车身颜色（红色）
    def click_cys(self):
        self.click_element(Page.cys)
        self.click_element(Page.hongs)

    def click_neis(self):
        self.click_element(Page.nsys)
        self.click_element(Page.qianse)

    # 选择车辆性质(非营运车辆）
    def click_cxz(self):
        self.click_element(Page.clxz)
        self.click_element(Page.fyy)

    # 选择车辆类别（七座含以下普通小型汽车）
    def click_clb(self):
        self.click_element(Page.cllb)
        self.click_element(Page.qzyx)

    # 选择初等日期
    def click_cdrq(self):
        self.click_element(Page.cdrq)
        self.click_element(Page.okrq)

    # 售价
    def input_sj(self, jiage="120"):
        allure.attach("车辆价格:", "车辆价格是{}万".format(jiage))
        self.input_element(Page.sj, jiage)

    # 审核备注
    def input_clbz(self, beizhu="自动化采车"):
        self.input_element(Page.shbz, beizhu)

    # 车辆描述
    def input_cyms(self, abc="车辆vin是%s" %salt):
        self.input_element(Page.cyms, abc)

    # 点击保存
    def click_baoc(self):
        self.click_element(Page.baoc)
        self.click_element(Page.shang)

    # 获取tolas消息
    @allure.step(title="获取toast消息")
    def get_toastscy(self, message, yuqi):
        self.get_toast(message, yuqi)

    @allure.step(title="获取toast消息")
    #驳回
    def click_bohui(self):
        self.click_element(Page.bohui)

    #待审
    def click_daishen(self):
        self.click_element(Page.daishen)

    @allure.step(title="查看采集车源是否在待审列表")
    def element_vin(self):
        res_data_text_list = []
        res_list = self.search_elements(Page.vinxianshi)
        for o in res_list:
            res_data_text_list.append(o.text)
        i = salt
        print(res_data_text_list)
        print(i)
        if i in res_data_text_list:
            allure.attach("待审列表", "待审列表存在该车源")
        else:
            allure.attach("待审列表", "待审列表不存在该车源")
            assert 1 == 2

    # 点击我的
    def click_wode(self):
        self.click_element(Page.my)

    #点击退出
    def click_tuichu(self):
        self.click_element(Page.esc)
