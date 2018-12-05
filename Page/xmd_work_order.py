import Page
import allure
from Base.Base import Base
import sys,os
sys.path.append(os.getcwd())
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

seed = "1234567890"
seed1 = "12345"
sa = []
digit = []
carList = []
# 手机号随机8位
for i in range(8):
    sa.append(random.choice(seed))
tell_num = '137' + ''.join(sa)
# print(salt)

# 客户姓名随机4位
for j in range(4):
    digit.append(random.choice(seed))
digit1 = ''.join(digit)

# 随机添加车源
for k in range(1):
    carList.append(random.choice(seed1))
carList1 = ''.join(carList)
#print(carList1)

def crm_work_order():
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.get("http://uat.login.taoche.com/casserver/login?service=http://uat.crm.yxqiche.com/auth-web/shiro_cas")
    # 浏览器最大化
    driver.maximize_window()
    driver.implicitly_wait(30)
    # 输入账号和密码
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("15715353528")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("uat.portal")
    # 点击登录
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="fm1"]/section[4]/input[5]'))).click()
    # 点击线索管理
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/ul/li[5]/div/span/span').click()
    sleep(1)
    # 点击新建C2线索
    driver.find_element_by_xpath('//*[@id="/clue$Menu"]/li[2]/a').click()
    sleep(2)
    # 点击填写手机号
    driver.find_element_by_xpath('//*[@id="telephone"]').send_keys(tell_num)
    sleep(1)
    # 点击填写姓名
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("自动化工单%s" %digit1)
    '''
    #选择性别为女性
    driver.find_element_by_xpath('//*[@id="gender"]/label[2]/span[1]/input').click()
    sleep(1)
    '''
    '''
    #婚否选择已婚
    driver.find_element_by_xpath('//*[@id="maritalStatus"]/label[1]/span[1]/input').click()
    sleep(1)
    '''
    # 婚否选择未婚
    driver.find_element_by_xpath('//*[@id="maritalStatus"]/label[2]/span[1]/input').click()
    sleep(1)
    # 点击输入年龄
    driver.find_element_by_xpath('//*[@id="age"]').send_keys("18")
    sleep(1)
    # 点击选择职业
    driver.find_element_by_xpath('//*[@id="career"]/div/div/div').click()
    # 销售|客服|市场
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()
    sleep(1)
    # 点击填写购车预算
    # 初始值
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[3]/div[1]/div/div[2]/div/span/input[1]').send_keys(
        "5")
    # 结束值
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[3]/div[1]/div/div[2]/div/span/input[2]').send_keys(
        "15")
    sleep(1)
    # 是否分期选择“是”
    driver.find_element_by_xpath('//*[@id="purchaseMode"]/label[1]/span[1]/input').click()
    sleep(1)
    '''
    #是否分期选择“否”
    driver.find_element_by_xpath('//*[@id="purchaseMode"]/label[2]/span[1]/input').click()
    sleep(1)
    '''

    # 选择客户类型为个人
    driver.find_element_by_xpath('//*[@id="customerType"]/label[1]/span[1]/input').click()

    # 选择客户类型为公司
    # driver.find_element_by_xpath('//*[@id="customerType"]/label[2]/span[1]/input').click()

    # 屏幕下滑
    slide = "window.scrollTo(0, 500)"
    driver.execute_script(slide)
    sleep(1)

    # 点击来源渠道
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div/div/form/div[2]/div[2]/div/span/div/span/input').click()
    sleep(1)
    # 选择淘车网
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[4]').click()
    sleep(1)
    # 选择B2C淘车网
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul[2]/li').click()
    sleep(1)

    # 选择用途为个人
    driver.find_element_by_xpath('//*[@id="carUse"]/div/div/div').click()
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[1]').click()
    sleep(1)

    # 选择客户标签为置换
    driver.find_element_by_xpath('//*[@id="customerLabels"]/label[1]/span[1]/input').click()
    sleep(1)

    # 选择客户标签为回购
    # driver.find_element_by_xpath('//*[@id="customerLabels"]/label[2]/span[1]/input').click()
    # sleep(1)

    # 选择用户意向等级为3天
    driver.find_element_by_xpath('//*[@id="buyCarPlan"]/div/div/div').click()
    driver.find_element_by_xpath('/html/body/div[6]/div/div/div/ul/li[1]').click()
    sleep(1)

    # 点击用户意向
    # driver.find_element_by_xpath('//*[@id="carCodeSource"]/label[1]/span[1]/input').click()
    # 点击座席推荐
    driver.find_element_by_xpath('//*[@id="carCodeSource"]/label[2]/span[1]/input').click()

    # 选择看车时间
    # driver.find_element_by_xpath('//*[@id="appointTimeRange"]/span/i/svg').click()
    # sleep(1)

    # 屏幕下滑
    slide1 = "window.scrollTo(500,1700)"
    driver.execute_script(slide1)
    sleep(1)

    # 点击城市,选择西藏
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[2]/div/span/div[1]/div/div/div[1]').click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[7]/div/div/div/ul/li[27]").click()
    # 选择城市“林芝”
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[2]/div/span/div[2]/div/div/div').click()
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul/li[7]').click()
    sleep(3)

    # 屏幕上滑
    slide2 = "window.scrollTo(1700,1600)"
    driver.execute_script(slide2)
    sleep(1)
    # 点击搜索
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]/button[1]').click()
    sleep(1)

    # 点击添加(从查询列表中随机添加一个)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[4]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[%s]/td/span/a[1]'%carList1).click()
    sleep(1)

    # 屏幕上滑
    slide3 = "window.scrollTo(1600,1200)"
    driver.execute_script(slide3)
    sleep(1)

    # 点击保存工单
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/span/button').click()
    sleep(1)

    # 点击小马达管理专用
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/ul/li[12]/div/span/span').click()
    sleep(1)

    # 点击小马达销售工单
    driver.find_element_by_xpath('//*[@id="/salessinglecity$Menu"]/li[3]/a').click()
    sleep(1)
    # 点击客户电话
    driver.find_element_by_xpath('//*[@id="customerTelephone"]').send_keys(tell_num)
    sleep(1)
    # 点击查询
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/form/div[2]/div/div/div/span/button[1]').click()
    sleep(1)
    # 勾选查询到的工单
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/table/tbody/tr/td[1]/span/label/span/input').click()
    sleep(1)
    # 点击分配销售工单
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/button[2]').click()
    sleep(1)
    # 点击并输入销售姓名
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("txh-销售")
    sleep(1)
    # 点击查询
    driver.find_element_by_xpath(
        '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/div/span/button').click()
    sleep(1)
    # 点击分配
    driver.find_element_by_xpath(
        '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div/table/tbody/tr/td[3]/span/a').click()
    sleep(1)
    # 关闭浏览器
    driver.quit()

class gongdan(Base):
    def  __init__(self,deiver):
        Base.__init__(self,deiver)

    def input_login(self,userName=10000000146,password="uat.portal"):
        allure.attach("用户登陆信息：", "用户名:%s\n密码:%s" % (userName, password))
        self.input_element(Page.username,userName)
        self.input_element(Page.password,password)
        self.click_element(Page.login)
        self.click_element(Page.cancel)

    #点击B2C销售管理
    def click_b2c_xsgl(self):
        self.click_element(Page.b2c_xsgl)

    #点击工单管理
    def click_work_management(self):
        self.click_element(Page.work_management)

    #点击管理列表的搜索按钮
    def click_gl_search(self):
        self.click_element(Page.gd_search)

    #点击工单搜索框
    #def click_gdsousuo(self):
    #    self.input_element(Page.gdSearchText, tell_num)

    #通过工单号搜索工单
    def search_work_num(self, workNum=154390772501401):
        self.input_element(Page.gd_searchText, workNum)

    #点击搜索按钮
    def click_searchButton(self):
        self.click_element(Page.gd_sousuo)

    #点击分配工单
    def click_allotWorkOrder(self):
        self.click_element(Page.fenpeigongdan)

    #选择销售
    def choose_seller(self):
        self.click_element(Page.seller)

    #点击确定
    def click_confirm(self):
        self.click_element(Page.okrq)

    # 获取toast消息
    @allure.step(title="获取toast消息")
    def get_toastscy(self, message, yuqi):
        self.get_toast(message, yuqi)

    #点击返回
    def click_return(self):
        self.click_element(Page.fanhui)

    # 点击我的
    def click_wode(self):
        self.click_element(Page.my)

    #点击退出
    def click_tuichu(self):
        self.click_element(Page.esc)

    #登录销售账号
    def input_denglu(self,userName=10000000145,password="uat.portal"):
        allure.attach("用户登陆信息：", "用户名:%s\n密码:%s" % (userName, password))
        self.input_element(Page.username,userName)
        self.input_element(Page.password,password)
        self.click_element(Page.login)
        self.click_element(Page.cancel)

    #点击B2C销售
    def click_b2cSeller(self):
        self.click_element(Page.b2c_seller)

    #点击工单
    def click_workOrder(self):
        self.click_element(Page.work_order)

    #点击搜索
    def click_sousuo(self):
        self.click_element(Page.gd_search)

    #输入工单号搜索
    def search_workNum(self):
        self.input_element(Page.gd_searchText)

    #点击搜索按钮
    def click_sousuoButton(self):
        self.click_element(Page.gd_sousuo)

    #验证工单搜索是否正确,且工单状态是待邀约
    def verify_result(self):
        try:
            pass
        except:
            pass

    #点击添加邀约记录
    def click_inviteRecord(self):
        self.click_element(Page.addInvite_record)

    #点击预约日期
    def click_reservationDate(self):
        reservationDate = self.search_elements(Page.reservation_date)
        allure.attach("选择的门店是:", "{}".format(reservationDate[0].text))
        reservationDate[0].click()

    #选择预约日期为当前日期前一天
    def choose_reservationDate(self):
        pass

    #点击预约时间并确定
    def click_reservationTime(self):
        pass

    #点击预约地点
    def click_reservationPlace(self):
        pass

    #选择地点并确定
    def click_firstPlace(self):
        pass

    #点击并填写跟进记录
    def click_followRecord(self):
        pass

    #点击保存并确认
    def click_saveRecord(self):
        pass

    #断言预约成功




