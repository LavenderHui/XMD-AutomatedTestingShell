import os
import random
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

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
print(carList1)

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
slide1 = "window.scrollTo(500,1000)"
driver.execute_script(slide1)
sleep(1)

#选择下发城市
#西藏
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div/div/form/div[9]/div[2]/div/span/div[1]/div/div/div[1]').click()
sleep(1)
driver.find_element_by_xpath('/html/body/div[7]/div/div/div/ul/li[27]').click()
sleep(1)
#林芝
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div/div/form/div[9]/div[2]/div/span/div[2]/div/div/div').click()
sleep(1)
driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul/li[7]').click()
sleep(1)


# 屏幕下滑
slide2= "window.scrollTo(1000,1700)"
driver.execute_script(slide2)
sleep(1)

# 点击城市,选择西藏
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[2]/div/span/div[1]/div/div/div[1]').click()
sleep(1)
driver.find_element_by_xpath("/html/body/div[9]/div/div/div/ul/li[27]").click()
# 选择城市“林芝”
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[2]/div/span/div[2]/div/div/div').click()
sleep(1)
driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[7]').click()
sleep(3)

# 屏幕上滑
slide3 = "window.scrollTo(1700,1600)"
driver.execute_script(slide3)
sleep(1)
# 点击搜索
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]/button[1]').click()
sleep(1)

# 点击添加(从查询列表中随机添加一个)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[4]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[%s]/td/span/a[1]'%carList1).click()
sleep(1)

# 屏幕上滑
slide4 = "window.scrollTo(1600,1200)"
driver.execute_script(slide4)
sleep(1)

#选择门店意向车源为用户意向
#driver.find_element_by_xpath('//*[@id="intentionType0"]/label[1]/span[1]/input').click()
#sleep(1)

#选择门店意向车源为座席推荐
driver.find_element_by_xpath('//*[@id="intentionType0"]/label[2]/span[1]/input').click()
sleep(1)

# 点击保存工单
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/span/button').click()
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
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/form/div[2]/div/div/div/span/button[1]').click()
sleep(1)

"""
# 勾选查询到的工单
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/table/tbody/tr/td[1]/span/label/span/input').click()
sleep(1)
# 点击分配销售工单
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/button[2]').click()
sleep(1)
# 点击并输入销售姓名
driver.find_element_by_xpath('//*[@id="name"]').send_keys("txh-销售")
sleep(1)
# 点击查询
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/div/span/button').click()
sleep(1)
# 点击分配
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div/table/tbody/tr/td[3]/span/a').click()
sleep(1)
# 关闭浏览器
driver.quit()
"""
