import sys,os,allure
sys.path.append(os.getcwd())
from Page.xmd_work_order import crm_work_order
from time import sleep
from Page.xmd_work_order import gongdan
from Base.get_driver import get_driver
class test_gongdan:
    #CRM下发工单
    #def crm_xfgd(self):
    #    crm_work_order()

    def setup_class(self):
        self.obj = gongdan(get_driver())

    @allure.step(title="登录操作")
    def test_denglu(self):
        self.obj.input_login()

    @allure.step(title="点击B2C销售管理")
    def test_seller_management(self):
        self.obj.click_b2c_xsgl()

    @allure.step(title="点击工单管理")
    def test_work_management(self):
        self.obj.click_work_management()

    @allure.step(title="搜索工单")
    def test_search_workOrder(self):
        self.obj.click_gl_search()
    #   self.obj.click_gdsousuo()
        self.obj.search_work_num()
        self.obj.click_searchButton()

    @allure.step(title="分配工单")
    def test_allot_workOrder(self):
        self.obj.click_allotWorkOrder()

    @allure.step(title="屏幕上滑")
    #屏幕上滑
    def test_slide1(self):
        self.obj.slide(490, 1902, 490, 112, 2000)

    #选择txh-销售
    @allure.step(title="选择销售")
    def test_chooseSeller(self):
        self.obj.choose_seller()
    def test_confirm(self):
        self.obj.click_confirm()

    @allure.step(title="断言分配成功")
    def test_dybc(self):
        self.obj.get_toastscy("小马达：分配", "小马达：分配成功")


