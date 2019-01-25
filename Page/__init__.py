#!/usr/bin/env python
# -*- coding=UTF-8 -*-
import sys,os
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
# 门店业务z
Store_business=(By.XPATH,"//android.widget.TextView[@text='门店业务']")
# 待办当月驳回
backlog=(By.XPATH,"//android.widget.TextView[@text='当月驳回']")
# 采集入口2
Collecting_entrance=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_vehicle_collectted' and @text='车源采集']")
# 采集门店入口
mdcj=(By.XPATH,"//android.widget.TextView[@text='门店采集']")
# 采集加好
cjjai=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/menu_item_add' and @content-desc='Add']")
# 门店名称
mdmc=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText1' and @text='请输入与门头照片一致的门头名称']")
# 别名
bm=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText1' and @text='请输入该门店的别名，便于辨认']")
# 门头照照片相机
mtxj=(By.XPATH,"//android.widget.ImageButton[@resource-id='com.kanche.mars:id/button2']")
# 相机快门
xjkm=(By.XPATH,"//android.widget.ImageView[@resource-id='com.oppo.camera:id/shutter_button' and @content-desc='“快门”按钮']")
# 选择照片
gouzp=(By.XPATH,"//android.widget.ImageView[@resource-id='com.oppo.camera:id/btn_done']")
# 定位按钮
xxdz=(By.XPATH,"//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")
# 选择位置
wizhi=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_name']")
# 确定
okwz=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/locate' and @text='确定']")
# 位置补充
wzbc=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText1' and @text='请输入位置补充']")
# 所属市场
sssh=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='请选择']")
# 选择市场
xzsc=(By.XPATH,"//android.widget.TextView[@resource-id='android:id/text1' and @text='北京北辰亚运村汽车交易市场中心']")
# 车位数
cws=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText1' and @text='请输入车位数']")
# 拍摄车位照片快门
cwkm=(By.XPATH,"//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]")
# 选择车位照片
cwzpxz=(By.XPATH,"//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]")
# 姓名
name=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText1' and @text='请输入']")
# 手机
cal=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText1' and @text='请输入']")
# 是否是老板
sflb=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='是/否']")
yes=(By.XPATH,"//android.widget.TextView[@resource-id='android:id/text1' and @text='是']")
# 保存门店信息
baoc=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/save_data' and @text='保存']")
# 页面返回
fanhui=(By.XPATH,"//android.widget.ImageButton[@content-desc='转到上一层级']")
# 我的
my=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_tab' and @text='我的']")
# 退出登录
esc=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_logout' and @text='退出']")
# 登录页面
Add=(By.ID,"android:id/button1")
# 账号
username = (By.ID,"com.kanche.mars:id/et_username")
# 密码框
password=(By.ID,"com.kanche.mars:id/et_password")
# 登录按钮
lohin=(By.ID,"com.kanche.mars:id/bt_login")
# 取消更新
cancel=(By.ID,"android:id/button2")
"""采集"""
# 车源采集入口
cjrk=(By.XPATH,"//android.widget.TextView[@text='车源采集']")
# 页面+号
jia=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/menu_item_add' and @content-desc='Add']")
# 门店搜索框
srmd=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/et_dialog_search_store_content' and @text='门店名称/别名/短编码']")
# 搜索按钮
ss=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_dialog_search' and @text='搜索']")
# 门店点击
xzmd=(By.ID,"com.kanche.mars:id/tv_store_name")
#选择固定门店
xzgdmd=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_store_name' and @text='物质(M057782)']")
# 提示
hint=(By.ID,"android:id/message")
car_image=(By.ID,"com.kanche.mars:id/tv_regester_year_mileage")
# 确认选择门店按钮
okan=(By.XPATH,"//android.widget.Button[@resource-id='android:id/button1' and @text='确定']")
# 采集车源信息页
# 相机
xj=(By.XPATH,"//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageButton[1]")
# 相机确认按钮
# vin码相机快门
vinkm=(By.XPATH,"//android.widget.ImageButton[@resource-id='com.kanche.mars:id/btn_shutter']")
# 不识别vin
fou=(By.XPATH,"//android.widget.Button[@resource-id='android:id/button2' and @text='否']")
# 识别vin
shi=(By.XPATH,"//android.widget.Button[@resource-id='android:id/button2' and @text='是']")
# vin码填写框
vinsr=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText1' and @text='请输入17位VIN码']")
# 车型
cx1=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='VIN码识别自动带入，或手选']")
cx2=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_title' and @text='阿斯顿·马丁']")
cx3=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_title' and @text='DB11']")
cx4=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_title' and @text='2019款 NC500 限量版']")
#cx4=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_title' and @text='2017款 540i 3.0T 手自一体 M运动套装']")
# 表显里数
bxls=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText1' and @text='保留到小数点后两位']")
# 车辆照片
# 封面：左前45度
clzp1=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='封面：左前45度']")
clzp1KM=(By.XPATH,"//android.widget.ImageButton[@resource-id='com.kanche.mars:id/btn_shutter_vehicle']")
# 正前/右前45度均可
clzp2=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='正前/右前45度均可']")
xzxj=(By.XPATH,"//android.widget.ImageView[@resource-id='com.kanche.mars:id/imageView']")
# 右后45度
clzp3=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='右后45度']")
# 正后/左后45度
clzp4=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='正后/左后45度']")
# 左后尾灯
clzp5=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='左后尾灯']")
# 左前大灯
clzp6=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='左前大灯']")
# 前排空间
clzp7=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='前排空间']")
# 后排空间
clzp8=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='后排空间']")
# 中控+方向盘全景
clzp9=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='中控+方向盘全景']")
# 仪表盘
clzp10=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='仪表盘']")
# 中控台
clzp11=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='中控台']")
# 档位+手刹
clzp12=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='档位+手刹']")
# 左前门里板
clzp13=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='左前门里板']")
# 发动机
clzp14=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='发动机']")
# 后备仓
clzp15=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='后备仓']")
# 轮毂
clzp16=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/cover_text' and @text='轮毂']")
# 车源相机页面完成
wanc=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/save_data' and @text='1/1 完成']")

# 车身颜色
cys=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='请选择车身颜色']")
# 内饰颜色
qianse=(By.XPATH,"//android.widget.TextView[@resource-id='android:id/text1' and @text='深色']")
nsys=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='请选择内饰颜色']")
# 红色
hongs=(By.XPATH,"//android.widget.TextView[@resource-id='android:id/text1' and @text='红色	']")
# 车辆性质
clxz=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='请选择车辆性质']")
# 车辆类别
cllb=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='请选择车辆类别']")
# 车辆类别选择七座以下普通车辆
cllbxz=(By.XPATH,"//android.widget.TextView[@resource-id='android:id/text1' and @text='七座（含）以下普通小型汽车']")
# 非营运车辆
fyy=(By.XPATH,"//android.widget.TextView[@resource-id='android:id/text1' and @text='非营运']")
# 初等日期
cdrq=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_right' and @text='请选择初登日期']")
# 确定
okrq=(By.XPATH,"//android.widget.Button[@resource-id='android:id/button1' and @text='确定']")
# 售价
sj=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText1' and @text='保留到小数点后两位']")
# 审核备注
shbz=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText' and @text='300字以内']")
# 车源描述
cyms=(By.XPATH,"//android.widget.EditText[@resource-id='com.kanche.mars:id/editText' and @text='200字以内']")
# 保存
baocun=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/save_data' and @text='保存']")
# 完成
wancheng=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_action_four' and @text='完成']")
# 上传
shang=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_action_three' and @text='上传车辆']")
# 车源表示
cybs=(By.ID,"com.kanche.mars:id/tv_vehicle_source")
# 车源点击
che=(By.ID,"com.kanche.mars:id/iv_vehicle_image")
# 采集车源管理
# 待审按钮
daishen=(By.XPATH,"//android.widget.TextView[@text='待审']")
# vin显示框
vinxianshi=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_vin']")
quxiao=(By.XPATH,"//android.widget.Button[@resource-id='android:id/button2' and @text='取消']")
# 门店title
shop_title=(By.ID,"//android.widget.TextView[@text='选择门店']")
# 添加车源title
add_car=(By.XPATH,"//android.widget.TextView[@text='添加车源']")
Collect_the_next_car=(By.XPATH,"//android.widget.TextView[@resource-id='com.kanche.mars:id/tv_action_one' and @text='采集下一辆']")
# 关闭
close=(By.XPATH,"//android.widget.ImageView[@resource-id='com.kanche.mars:id/tv_dialog_close']")
























