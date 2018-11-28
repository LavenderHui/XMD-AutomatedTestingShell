from selenium import webdriver
import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

seed = "1234567890"
sa = []
for i in range(8):
    sa.append(random.choice(seed))
salt ='137'+ ''.join(sa)
print(salt)
#def web_work_orser():
driver = webdriver.Chrome()
driver.get("http://uat.crm.yxqiche.com/casserver/login?service=http://uat.crm.yxqiche.com/auth-web/shiro_cas")
driver.maximize_window()
driver.implicitly_wait(30)
# 输入账号密码
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='username']"))).send_keys("15715353528")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("uat.portal")
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fm1"]/section[4]/input[5]'))).click()
# 点击线索XPATH
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[1]/div/ul/li[5]/div/span/span'))).click()
# 点击新建c2线索
sleep(2)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="/clue$Menu"]/li[2]/a'))).click()
# 输入手机号
a =WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="telephone"]')))
a.clear()
a.send_keys(salt)
# 填写客户姓名
driver.find_element_by_xpath('//*[@id="name"]').send_keys("自动化测试")
# 点击是否分期
driver.find_element_by_xpath('//*[@id="purchaseMode"]/label[1]/span[1]/input').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="crmSource"]/div/div/div').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[2]').click()
sleep(1)
js1="window.scrollTo(0,600)"
# 最顶层
# 执行最底层
driver.execute_script(js1)
sleep(1)
driver.find_element_by_xpath('//*[@id="carCodeSource"]/label[1]/span[2]').click()
sleep(2)
a=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/form/div[5]/div[2]/div/span/div[1]/div/div/div[1]')
a.click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[27]').click()
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/form/div[5]/div[2]/div/span/div[2]/div/div/div').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[7]').click()
sleep(1)
js1="window.scrollTo(0,1500)"
# 最顶层
# 执行最底层
driver.execute_script(js1)
sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[4]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/span/a[1]').click()
sleep(2)
js2="window.scrollTo(1500,1300)"
driver.execute_script(js2)
sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/span/button').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/ul/li[12]/div/span/span').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="/salessinglecity$Menu"]/li[2]/a').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[1]/span/label/span/input').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/button[2]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="name"]').send_keys("txh-销售")
sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/div/span/button').click()
sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div/table/tbody/tr/td[3]/span/a').click()
sleep(1)
driver.quit()