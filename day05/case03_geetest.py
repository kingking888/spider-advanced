# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

Email = '820685755@qq.com'
Passwd = 'gbt73016.'


class CrackGeetest():
    def __init__(self):
        self.url = "https://auth.geetest.com/login"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = Email
        self.passwd = Passwd

    def get_geetest_button(self):
        # 模拟打开网页
        self.browser.get(self.url)
        # 完善登陆表单
        username = self.browser.find_element_by_xpath(
            '//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[1]/div/input')
        password = self.browser.find_element_by_xpath(
            '//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[1]/div/input')
        username.send_keys(self.email)
        time.sleep(3)
        password.send_keys(self.passwd)
        time.sleep(3)
        # 获取验证按钮
        button = self.browser.find_element_by_xpath('//*[@id="captchaIdLogin"]/div/div[2]/div[1]/div[3]')
        time.sleep(3)
        button.click()


if __name__ == '__main__':
    l = CrackGeetest()
    l.get_geetest_button()
