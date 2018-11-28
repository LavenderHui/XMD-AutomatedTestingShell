import sys, os

sys.path.append(os.getcwd())
import allure
from time import sleep
from Page.xmd_cycj import search
from Base.get_driver import get_driver


class Test_1:
    @allure.step(title="获取权限成功")
    def setup_class(self):
        self.obj = search(get_driver())

    @allure.step(title="输入账号密码")
    def test_2(self):
        self.obj.input_login()

    @allure.step(title="点击登录")
    def test_1(self):
        self.obj.click_login()

    @allure.step(title="点击取消更新")
    def test_qx(self):
        self.obj.click_cy_qx()

    @allure.step(title="车源采集入口")
    def test_3(self):
        self.obj.clcick_rk()


    @allure.step(title="点击搜索门店")
    def test_4(self):
        self.obj.click_ss()

    @allure.step(title="选择门店门店")
    def test_5(self):
        self.obj.click_md()
        self.obj.click_okan()

    @allure.step(title="拍摄vim照片")
    def test_xj(self):
        self.obj.click_xj()
        self.obj.click_ok()

    @allure.step(title="选择不识别vin码")
    def test_fou(self):
        self.obj.click_fou()

    @allure.step(title="输入表显历程和vin码")
    def test_bxl(self):
        self.obj.input_bxl()

    @allure.step(title="选择车型")
    def test_cxm(self):
        self.obj.click_cx()

    @allure.step(title="点击表显相机")
    def test_bxxj(self):
        self.obj.ckick_bxxj()
        self.obj.click_km()

    @allure.step(title="点击车源相机")
    def test_cyxj(self):
        self.obj.ckick_cyxj()

    @allure.step(title="拍摄车辆照片")
    def test_clzp(self):
        self.obj.click_clzp1()
        self.obj.click_clzpkm()
        self.obj.click_clzp2()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp3()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp4()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp5()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp6()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp7()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp8()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp9()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp10()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp11()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp12()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp13()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp14()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp15()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        self.obj.click_clzp16()
        self.obj.click_xzxj()
        self.obj.click_clzpkm()
        self.obj.click_wanc()
        sleep(3)
        self.obj.click_fanhui()

    @allure.step(title="选择车辆颜色")
    def test_clys(self):
        self.obj.click_cys()

    @allure.step(title="选择车内饰颜色")
    def test_nsys(self):
        self.obj.click_neis()

    @allure.step(title="选择车辆性质")
    def test_clxz(self):
        self.obj.click_cxz()

    @allure.step(title="选择车辆类别")
    def test_cllb(self):
        self.obj.click_clb()

    @allure.step(title="选择初登日期")
    def test_cdrq(self):
        self.obj.click_cdrq()

    @allure.step(title="屏幕下滑")
    def test_hd(self):
        self.obj.slide(390, 1667, 390, 516, 2000)

    @allure.step(title="填写售价")
    def test_sj(self):
        self.obj.input_sj()

    @allure.step(title="填写车辆备注")
    def test_clbz(self):
        self.obj.input_clbz()
        self.obj.input_cyms()

    @allure.step(title="点击保存按钮")
    def test_sc(self):
        self.obj.click_baoc()

    @allure.step(title="断言保存")
    def test_dybc(self):
        self.obj.get_toastscy("小马达：保存", "小马达：保存成功")

    @allure.step(title="断言上传成功toals")
    def test_dy(self):
        self.obj.get_toastscy("小马达：上传", "小马达：上传车辆成功")

    #驳回
    @allure.step(title="点击驳回")
    def test_click_bohui(self):
        self.obj.click_bohui()
    #待审
    def test_click_diashen(self):
        self.obj.click_daishen()

    @allure.step(title="验证车源上传后待审列表是否存在该车源")
    def test_click(self):
        self.obj.element_vin()

    @allure.step(title="返回上一级")
    def test_fhz(self):
        self.obj.click_fanhui()
        self.obj.click_wode()

    @allure.step(title="屏幕下滑")
    def test_hd(self):
        self.obj.slide(859, 1506, 859, 1164, 1000)

    @allure.step(title="退出")
    def test_tuichudenglu(self):
        self.obj.click_tuichu()