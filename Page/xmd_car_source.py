#!/usr/bin/env python
# -*- coding=UTF-8 -*-
import Page
import allure
from Base.Base import Base
import sys,os
from selenium.webdriver.common.by import By
sys.path.append(os.getcwd())
import random
from selenium import webdriver
from  time import sleep
# 随机生成vi
seed = "1234567890ABCDEFGHLJKMNPRSTUVWXYZ"
sa = []
for i in range(17):
    sa.append(random.choice(seed))
salt = ''.join(sa)
def web_shenhe():
    driver = webdriver.Chrome()
    driver.get("http://uat.crm.yxqiche.com/casserver/login?service=http://test.cheyuan.taoche.com/car-audit-api/shiro-cas")
    driver.maximize_window()
    driver.implicitly_wait(30)
    # 输入账号密码
    driver.find_element_by_xpath("//*[@id='username']").send_keys("17689551930")
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("uat.portal")
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//*[@id="fm1"]/section[4]/input[5]').click()
    # 点击审核中心
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/ul/li[1]/div').click()
    driver.implicitly_wait(30)
    sleep(2)
    # 点击b2c车源列表
    driver.find_element_by_xpath('//*[@id="/review$Menu"]/li[3]').click()
    driver.implicitly_wait(30)
    a = driver.find_element_by_xpath('//*[@id="vinCodeOrUnifiedNumber"]')
    a.clear()
    # 输入vin
    a.send_keys(salt)
    driver.implicitly_wait(30)
    sleep(2)
    # 点击查询
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div/form/div[8]/div/div/div/span/div/div/div/span/button[1]').click()
    sleep(2)
    # 点击审核按钮
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/div/div').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="extension"]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[1]/span/label/span/input').click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div/div/div[4]/div/button[2]').click()
class search(Base):
    # 生成随机vin码
    # 获取base
    def  __init__(self,deiver):
        Base.__init__(self,deiver)
    # 登录采集车源账号
    def input_login(self,name="10000000156",passwo="uat.portal"):
        allure.attach("用户登陆信息：", "用户名:%s\n密码:%s" % (name, passwo))
        self.input_element(Page.username,name)
        self.input_element(Page.password,passwo)
    # 点击登录按钮

    def click_login(self):
        self.click_element(Page.lohin)
    # 验证登录 抓tosta 断言元素存在
    @allure.step(title="验证是否登录成功")
    def judge_login(self):
        try:
            xpath = "//*[contains(@text,'{}')]".format("小马达:")
            toast_message = self.search_element((By.XPATH, xpath), timeout=5, poll=0.1).text
            allure.attach("登录异常提示：", toast_message)
            self.click_element(Page.lohin)
        except:
            self.search_element(Page.cancel)
            allure.attach("小马达：", "登录成功")
    # 点击取消更新按钮
    def click_cy_qx(self):
        self.click_element(Page.cancel)
    # 点击采集
    def clcick_rk(self):
            self.click_element(Page.cjrk)
    # 验证采集工作台采集入口
    def verify_inlet(self):
        try:
            self.search_element(Page.jia)
            allure.attach("工作台：", "采集入口存在")
            self.click_element(Page.fanhui)
        except:
            allure.attach("工作台：","采集入口不存在")
            assert 1=="2"
    # 验证门店业务工作台
    def click_voip(self):
        self.click_element(Page.Store_business)
        md = self.search_elements(Page.xzmd)
        md[0].click()
        self.click_element(Page.Collecting_entrance)
    def verify_voip(self):
        try:
            self.search_element(Page.jia)
            allure.attach("门店业务：", "采集入口存在")
            self.click_element(Page.fanhui)
            sleep(1)
            self.click_element(Page.fanhui)
            sleep(1)
            self.click_element(Page.fanhui)
        except:
            allure.attach("门店业务：", "采集入口不存在")
            assert 1 == "2"
    # 待办事项
    def click_backlog(self):
        self.click_element(Page.backlog)
    def verify_backlog(self):
        try:
            self.search_element(Page.jia)
            allure.attach("待办事项：","采集工作台存在")
            self.click_element(Page.fanhui)
        except:
            allure.attach("待办事项：","采集入口不存在")
            assert 1=="2"
    def click_gather(self):
        self.click_element(Page.cjrk)
        self.click_element(Page.jia)
    def click_ss(self):
        self.click_element(Page.Store_business)
        md = self.search_elements(Page.xzmd)
        array=(len(md))
        self.click_element(Page.fanhui)
        self.click_element(Page.cjrk)
        self.click_element(Page.jia)
        self.click_element(Page.ss)
        collect = self.search_elements(Page.xzmd)
        collect_array = (len(collect))
        try:
            assert array==collect_array
            allure.attach("直接点击搜索：", "查询到是该销售的所有门店")
            self.click_element(Page.fanhui)
            sleep(1)
            self.click_element(Page.fanhui)
        except:
            allure.attach("直接点击搜索：", "查询到不是该销售的所有门店")
            assert 1 == "2"
    def input_seek(self,name_1="淘车二手车(M001481)"):
        list_md=["淘车二手车","M001481","淘车"]
        for i in list_md:
            self.input_element(Page.srmd,i)
            self.click_element(Page.ss)
            try:
                shop_name=self.search_element(Page.xzmd)
                assert shop_name.text==name_1
                allure.attach("门店%s搜索："%i, "搜索正常")
                self.click_element(Page.fanhui)
                self.click_element(Page.jia)
            except:
                allure.attach("门店%s搜索："%i, "搜索异常")
                assert 1 == "2"
    def click_seek_cj(self):
        self.click_element(Page.ss)
        md = self.search_elements(Page.xzmd)
        md[0].click()
        try:
            hint=self.search_element(Page.hint)
            assert hint.text=="是否确认选择淘车二手车?"
            allure.attach("选择门店后提示为：",hint.text)
        except:
            allure.attach("选择门店后：","没有提示")
            assert 1 == "2"
    def verify_qx(self):
        self.click_element(Page.cancel)
        try:
            self.search_element(Page.shop_title)
            allure.attach("点击取消：","反回选择门店页")
        except:
            allure.attach("点击取消：", "未返回选择门店页")
            assert 1 == "2"
    def click_shop_1(self):
        md = self.search_elements(Page.xzmd)
        md[0].click()
        self.click_element(Page.okan)
        try:
            self.search_element(Page.add_car)
            allure.attach("点击确定：", "页面跳转到添加车源页面")
            self.click_element(Page.fanhui)
        except:
            allure.attach("点击确定：", "页面未跳转到添加车源页面")
            assert 1 == "2"
    def virify_fh(self):
        try:
            car_text=self.search_element(Page.hint)
            assert car_text.text=="是否保存所做的更改？"
            allure.attach("点击返回：", "页面提示为%s" % car_text.text)
            self.click_element(Page.Add)
        except:
            allure.attach("点击返回：", "页面提示有误" )
    def vitify_Return_to_save(self):
        number=self.search_elements(Page.car_image)
        car_number=len(number)
        self.click_element(Page.jia)
        self.click_element(Page.ss)
        md = self.search_elements(Page.xzmd)
        md[0].click()
        self.click_element(Page.okan)
        self.click_element(Page.fanhui)
        self.click_element(Page.Add)
        number1 = self.search_elements(Page.car_image)
        car_number1 = len(number1)
        try:
            assert car_number<car_number1
            allure.attach("点击是：", "返回采集车源管理页，待上传列表数据+1")
        except:
            allure.attach("点击是：", "返回采集车源管理页，待上传列表数据没有改变")
            assert 1 == "2"
    def click_cjrk(self):
        self.click_element(Page.cjrk)
    def vitify_button(self):
        self.click_element(Page.jia)
        self.click_element(Page.ss)
        md = self.search_elements(Page.xzmd)
        md[0].click()
        self.click_element(Page.okan)
        # self.click_element(Page.baocun)
        # self.get_toast("小马达：","小马达：保存成功")
        # try:
        #     wc=self.search_element(Page.wancheng).text
        #     allure.attach(wc, "按钮存在")
        #     self.search_element(Page.close)
        #     allure.attach("关闭", "按钮存在")
        #     cjxl=self.search_element(Page.Collect_the_next_car).text
        #     allure.attach(cjxl, "按钮存在")
        #     sc=self.search_element(Page.shang).text
        #     allure.attach(sc, "按钮存在")
        #     self.click_element(Page.close)
        # except:
        #     allure.attach("按钮","不存在")
        #     assert 1 == "2"

#     # 点击相机
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
    def click_save_car(self):
        self.click_element(Page.baocun)
        self.get_toast("小马达：保存","小马达：保存成功")
        self.click_element(Page.shang)
        self.get_toast("小马达：车辆信息","小马达：车辆信息不完整。请先完善信息后再上传")
        self.click_element(Page.close)
    def click_cx(self):
        self.click_element(Page.cx1)
        cpp1 = self.search_element(Page.cx2)
        allure.attach("车型选择信息：", "选择的车型:%s" % (cpp1.text))
        cpp1.click()
        cpp2= self.search_element(Page.cx3)
        cpp2.click()
        cpp3= self.search_element(Page.cx4)
        cpp3.click()
    # 输入表显里数以及vin
    # 循环输入vin
    def input_bxl(self,a="14"):
        allure.attach("采集车源信息：", "表显里程:%s万公里"% a)
        self.input_element(Page.bxls,a)
    # 验证输入vin
    def input_vin(self,a=salt):
        self.input_element(Page.vinsr,a)
# 点击表显里程相机
    def ckick_bxxj(self):
        bcxj=self.search_elements(Page.mtxj)
        bcxj[1].click()
    # 点击车源照片相机
    def ckick_cyxj(self):
        bcxj=self.search_elements(Page.mtxj)
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
    def click_fanhu(self):
        self.click_element(Page.fanhui)
    # 选择车身颜色（红色）
    def click_cys(self):
        self.click_element(Page.cys)
        self.click_element(Page.hongs)
    def click_neis(self):
        self.click_element(Page.nsys)
        self.click_element(Page.qianse)
    # 选择车辆性质(非营运车辆）以及车辆类别
    def click_cxz(self,x="非营运",l="七座（含）以下普通小型汽车"):
        allure.attach("采集车源信息：", "车辆性质:%s\n车辆类别:%s" % (x, l))
        self.click_element(Page.clxz)
        self.click_element(Page.fyy)
        self.click_element(Page.cllb)
        self.click_element(Page.cllbxz)
    # 选择初等日期
    def click_cdrq(self):
        self.click_element(Page.cdrq)
        self.click_element(Page.okrq)
    # 售价
    def input_sj(self,jiage="120"):
        allure.attach("车辆价格:", "车辆价格是{}万".format(jiage))
        self.input_element(Page.sj,jiage)
    # 审核备注
    def input_clbz(self,beizhu="自动化采车"):
        self.input_element(Page.shbz,beizhu)
    # 车辆描述
    def input_clms(self,abc="车辆vin是%s"%salt):
        self.input_element(Page.cyms,abc)
    # 点击保存
    def click_baoc(self):
        self.click_element(Page.baoc)
    # 点击完成按钮
    def click_wanccheng(self):
        self.click_element(Page.wancheng)
    # 断言待上传列表存在该采集车源
    def element_dsc(self):
        res_data_text_list = []
        res_list=self.search_elements(Page.vinxianshi)
        for o in res_list:
            res_data_text_list.append(o.text)
        i=salt
        print(i)
        a=self.search_element(Page.cybs).text
        if i in res_data_text_list and a=="新采集":
            allure.attach("待上传列表", "待上传列表存在该车源且车源标识为%s"%a)
        else:
            allure.attach("待上传列表", "待上传列表不存在该车源")
            assert 1==2
    # 获取采集车源vin
    def input_vin_web(self):
        a=self.search_elements(Page.vinxianshi)
        return a[0].text
    # 点击进入车源详细a
    def click_chyxx(self):
        self.click_element(Page.che)
    # 点击上传车源s
    def click_sc(self):
        self.click_element(Page.shang)
    # 获取tolas消息
    @allure.step(title="获取toast消息")
    def get_toastscy(self, message,yuqi):
        self.get_toast(message,yuqi)
    @allure.step(title="获取toast消息")
    def click_daishen(self):
        sleep(10)
        self.click_element(Page.daishen)
    @allure.step(title="查看采集车源是否在待审列表")
    def element_vin(self):
        res_data_text_list = []
        res_list=self.search_elements(Page.vinxianshi)
        for o in res_list:
            res_data_text_list.append(o.text)
        i=salt
        if i in res_data_text_list:
            allure.attach("待审列表", "待审列表存在该车源")
        else:
            allure.attach("待审列表", "待审列表不存在该车源")
            assert 1==2

    # 点击我的
    def click_wode(self):
        self.click_element(Page.my)
        self.click_element(Page.esc)

