#!/usr/bin/env python
# -*- coding=UTF-8 -*-
import sys,os
from time import sleep

sys.path.append(os.getcwd())
import allure
from Page.xmd_car_source import search
from Base.get_driver import get_driver
class Test_1:
    @allure.step(title="获取权限成功")
    def setup_class(self):
        self.obj=search(get_driver())
    @allure.step(title="输入账号密码")
    def test_2(self):
        self.obj.input_login()
    @allure.step(title="点击登录")
    def test_1(self):
         self.obj.click_login()
    def test_12(self):
        self.obj.judge_login()
    @allure.step(title="点击取消更新")
    def test_qx(self):
        self.obj.click_cy_qx()
    # @allure.step(title="车源采集入口")
    # def test_3(self):
    #     self.obj.clcick_rk()
    # @allure.step(title="验证工作台采集入口")
    # def test_verify_inlet(self):
    #     self.obj.verify_inlet()
    # def test_voip(self):
    #     self.obj.click_voip()
    # @allure.step(title="验证门店业务采集入口")
    # def test_verify_voip(self):
    #     self.obj.verify_voip()
    # def test_click_backlog(self):
    #     self.obj.click_backlog()
    # @allure.step(title="验证待办事项采集入口")
    # def test_verify_backlog(self):
    #     self.obj.verify_backlog()
    # @allure.step(title="验证直接点击搜索")
    # def test_4(self):
    #     self.obj.click_ss()
    # def test_return(self):
    #     self.obj.click_gather()
    # @allure.step(title="输入已存在门店名称/别名/短编码验证")
    # def test_name_seek(self):
    #     self.obj.input_seek()
    # @allure.step(title="点击搜索到的门店提示")
    # def test_seek_cj(self):
    #     self.obj.click_seek_cj()
    # @allure.step(title="点击搜索到的门店，点击取消")
    # def test_verify_qx(self):
    #     self.obj.click_cy_qx()
    # @allure.step(title="点击搜索到的门店，点击确定")
    # def test_click_shop_1(self):
    #     self.obj.click_shop_1()
    # @allure.step(title="在添加车源页左上角点击返回")
    # def test_virify_fh(self):
    #     self.obj.virify_fh()
    # @allure.step(title="在添加车源页左上角点击返回,选择是")
    # def test_vitify_Return_to_save(self):
    #     self.obj.vitify_Return_to_save()
    @allure.step(title="进入添加车源页，直接在添加车源页点击右上角“保存”按钮")
    def test_vitify_button(self):
        self.obj.click_cjrk()
        self.obj.vitify_button()
    @allure.step(title="拍摄vim照片")
    def test_xj(self):
        self.obj.click_xj()
        self.obj.click_ok()
    @allure.step(title="选择不识别vin码")
    def test_fou(self):
        self.obj.click_fou()
    # @allure.step(title="验证信息不全点击上传")
    # def test_sava_car(self):
    #     self.obj.click_save_car()
    @allure.step(title="输入表显历程")
    def test_bxl(self):
        self.obj.input_bxl()
    # @allure.step(title="验证信息不全点击上传")
    # def test_sava_bx(self):
    #     self.obj.click_save_car()
    @allure.step(title="选择车型")
    def test_cxm(self):
        self.obj.click_cx()
    # @allure.step(title="验证信息不全点击上传")
    # def test_sava_car_typ(self):
    #     self.obj.click_save_car()
    @allure.step(title="输入vin码")
    def test_input_vin(self):
        self.obj.input_vin()
    # @allure.step(title="验证信息不全点击上传")
    # def test_sava_vin(self):
    #     self.obj.click_save_car()

    @allure.step(title="点击表显相机")
    def test_bxxj(self):
        self.obj.ckick_bxxj()
        self.obj.click_km()
    # @allure.step(title="验证信息不全点击上传")
    # def test_sava_bxxj(self):
    #     self.obj.click_save_car()
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
        sleep(1)
        self.obj.click_fanhu()
    # @allure.step(title="验证信息不全点击上传")
    # def test_sava_car_watch(self):
    #     self.obj.click_save_car()
    @allure.step(title="选择车辆颜色")
    def test_clys(self):
        self.obj.click_cys()
    # @allure.step(title="验证信息不全点击上传")
    # def test_sava_colour(self):
    #     self.obj.click_save_car()
    @allure.step(title="选择车内饰颜色")
    def test_nsys(self):
        self.obj.click_neis()
    # @allure.step(title="验证信息不全点击上传")
    # def test_sava_ns_colour(self):
    #     self.obj.click_save_car()

    @allure.step(title="选择车辆性质")
    def test_clxz(self):
        self.obj.click_cxz()
    # @allure.step(title="验证信息不全点击上传")
    # def test_sava_car_change(self):
    #     self.obj.click_save_car()
    @allure.step(title="选择初登日期")
    def test_cdrq(self):
        self.obj.click_cdrq()
    # @allure.step(title="验证信息不全点击上传")
    # def test_sava_car_change(self):
    #     self.obj.click_save_car()
    @allure.step(title="填写售价")
    def test_sj(self):
        self.obj.input_sj()
    @allure.step(title="屏幕下滑")
    def test_hd(self):
        self.obj.slide(458, 1900, 458, 800, 2000)
    @allure.step(title="填写车辆备注")
    def test_clbz(self):
        self.obj.input_clbz()
        self.obj.input_clms()
    @allure.step(title="点击保存按钮")
    def test_sc(self):
        self.obj.click_baoc()
    # @allure.step(title="断言保存")
    # def test_dybc(self):
    #     self.obj.get_toastscy("小马达：保存","小马达：保存成功")
    # @allure.step(title="点击完成按钮")
    # def test_wancheng(self):
    #     self.obj.click_wanccheng()
    # @allure.step(title="断言新采集车源是否在待上传列表中")
    # def test_dsc(self):
    #     self.obj.element_dsc()
    @allure.step(title="对保存本地的新采集车源进行上传")
    def test_che(self):
        # self.obj.click_chyxx()
        self.obj.click_baoc()
        self.obj.click_sc()
    # def test_click_diashen(self):
    #     self.obj.click_daishen()
    # @allure.step(title="验证车源上传后待审列表是否存在该车源")
    # def test_click(self):
    #     self.obj.element_vin()
    # @allure.step(title="跳转到车辆审核列表对车源进行审核")
    # def test_webshenhe(self):
    #     web_shenhe()
    #
    @allure.step(title="退出登录")
    def test_fhz(self):
        self.obj.click_fanhu()
        self.obj.click_wode()

