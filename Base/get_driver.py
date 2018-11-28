from appium import webdriver


def get_driver():
    """
    :param pac: 包名
    :param act: 启动名
    :return:
    """
    desired_caps = {}
    # 平台 - 必填
    desired_caps['platformName'] = 'Android'
    # 系统版本 - 非必填，填写就必须正确
    desired_caps['platformVersion'] = '5.1'
    # 获取toast支持
    desired_caps['automationName'] = 'Uiautomator2'
    # 设备名称
    desired_caps['deviceName'] = '596a2802'
    # desired_caps['app'] = 'apk绝对路径'
    # app包名
    desired_caps['appPackage'] = "com.kanche.mars"
    # app启动名
    desired_caps['appActivity'] = "com.kanche.mars.activity.WelcomeActivity"
    # 隐藏键盘
    #desired_caps['unicodeKeyboard'] = True
    #desired_caps['resetKeyboard'] = True
    # 获取启动后需要的权限
    desired_caps['noReset'] = True
    # 设置中文输入
    # desired_caps['autoGrantPermissions'] = True
    # desired_caps["unicodeKeyboard"] = True
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
