import sys, os, allure

sys.path.append(os.getcwd())
from time import sleep
from Page.xmd_mdcj import search1
from Base.get_driver import get_driver


class Test_01:
    # 获取权限
    def setup_class(self):
        self.obj = search1(get_driver())

    @allure.step(title="登录操作")
    def test_2(self):
        self.obj.import_login()

    @allure.step(title="点击登录")
    def test_1(self):
        self.obj.click_login()

    def test_09(self):
        self.obj.get_toast("小马达：请输入", "小马达：请输入用户名")

    @allure.step(title="选择不更新")
    def test_3(self):
        self.obj.click_bgx()

    @allure.step(title="点击门店采集入口")
    def test_4(self):
        self.obj.click_mdcj()

    # 门店名称验证
    @allure.step(title="点击保存")
    def test_18_mdmc(self):
        self.obj.click_bc()

    @allure.step(title="验证不填写门店名称是否可以保存")
    def test_md_mc(self):
        self.obj.get_toasts("小马达：门名称", "小马达：门店名称没有填写")

    @allure.step(title="输入门店名字")
    def test_5(self):
        self.obj.input_md_mame()

    # 不拍摄门头照片
    @allure.step(title="点击保存")
    def test_18_mdzp(self):
        self.obj.click_bc()

    @allure.step(title="验证不拍摄门头照片是否可以保存")
    def test_md_mtzp(self):
        self.obj.get_toasts("小马达：请选择门头", "小马达：请选择门头照片")

    @allure.step(title="拍摄门头照片")
    def test_6(self):
        self.obj.click_mdzp()

    @allure.step(title="点击相机快门")
    def test_7(self):
        self.obj.click_xzzp()

    # 位置验证
    @allure.step(title="点击保存")
    def test_18_wz(self):
        self.obj.click_bc()

    @allure.step(title="验证不填写位置信息是否可以保存")
    def test_md_wz(self):
        self.obj.get_toasts("小马达：请选择地", "小马达：请选择地址")

    @allure.step(title="选择位置")
    def test_8(self):
        self.obj.click_gzp()

    @allure.step(title="位置补充")
    def test_9(self):
        self.obj.input_pcwz()

    # 所属市场验证
    @allure.step(title="点击保存")
    def test_18_sssc(self):
        self.obj.click_bc()

    @allure.step(title="验证不填写所在市场是否可以保存")
    def test_md_sssc(self):
        self.obj.get_toasts("小马达：请选择所在市", "小马达：请选择所在市场")

    @allure.step(title="所属市场")
    def test_10(self):
        self.obj.click_szsh()

    # 车位数验证
    @allure.step(title="点击保存")
    def test_18_cws(self):
        self.obj.click_bc()

    @allure.step(title="验证不填写车位数是否可以保存成功")
    def test_md_cws(self):
        self.obj.get_toasts("小马达：车位数", "小马达：车位数没有填写")

    @allure.step(title="填写车位数")
    def test_11(self):
        self.obj.input_cws()

    # 车位照片
    @allure.step(title="点击保存")
    def test_18_cwzp(self):
        self.obj.click_bc()

    @allure.step(title="验证不拍摄车位照片是否可以保存")
    def test_md_cwzp(self):
        self.obj.get_toasts("小马达：请选择车位照", "小马达：请选择车位照片")

    @allure.step(title="拍摄车照片")
    def test_12(self):
        self.obj.click_cwrk()

    # 调用门头元素
    @allure.step(title="点击快门勾选照片")
    def test_13(self):
        self.obj.click_xzzp()

    # 联系人验证
    @allure.step(title="点击保存")
    def test_18_lxr(self):
        self.obj.click_bc()

    @allure.step(title="验证不填写联系人是否可以保存")
    def test_md_lxr(self):
        self.obj.get_toasts("小马达：姓名", "小马达：姓名没有填写")

    @allure.step(title="填写门店联系人")
    def test_14(self):
        self.obj.input_name()

    @allure.step(title="屏幕下滑")
    def test_16(self):
        self.obj.aaa(458, 1300, 458, 850, 1500)

    @allure.step(title="点击保存")
    def test_18_sj(self):
        self.obj.click_bc()

    @allure.step(title="验证不填写手机是否可以保存")
    def test_md_sj(self):
        self.obj.get_toasts("小马达：手机", "小马达：手机没有填写")

    @allure.step(title="输入手机号")
    def test_17(self):
        self.obj.input_cal()

    @allure.step(title="选择是否是老板")
    def test_15(self):
        self.obj.clicj_lb()
        self.obj.click_cwrk()
        self.obj.click_xzzp()

    @allure.step(title="点击保存")
    def test_18(self):
        self.obj.click_bc()

    def test_cjmd(self):
        self.obj.get_toast("小马达：保存", "小马达：保存成功")

    @allure.step(title="点击返回上一级")
    def test_19(self):
        self.obj.click_fh()
        sleep(2)

    @allure.step(title="点击返回")
    def test_22(self):
        self.obj.click_fh()

    @allure.step(title="退出账号")
    def test_21(self):
        self.obj.click_esc()
