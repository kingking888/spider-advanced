from selenium import webdriver
# 等待页面加载
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from PIL import Image, ImageChops
from io import BytesIO
from lxml import etree
import requests
import re
import time

BORDER = 6


class Login():
    def __init__(self):
        self.url = 'https://www.tianyancha.com/login'
        self.brower = webdriver.Chrome()
        self.brower.maximize_window()

    def login(self):
        self.brower.get(self.url)
        time.sleep(3)
        login_paw = self.brower.find_element_by_xpath('//div[text()="密码登录"]')
        login_paw.click()
        time.sleep(3)
        username = self.brower.find_element_by_xpath(
            '//*[@id="web-content"]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/input')
        username.send_keys('18830004824')
        time.sleep(3)
        password = self.brower.find_element_by_xpath(
            '//*[@id="web-content"]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[3]/input')
        password.send_keys('x13473048836')
        time.sleep(3)
        checked = self.brower.find_element_by_xpath(
            '//*[@id="web-content"]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[4]/input')
        checked.click()
        time.sleep(3)
        login_button = self.brower.find_element_by_xpath(
            '//*[@id="web-content"]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[5]')

        i = 0
        while i < 5:
            login_button.click()
            time.sleep(5)
            if self.brower.find_element_by_xpath('//div[@class="gt_popup_wrap"]'):
                break
            else:
                i = i + 1

    # def get_images(self):  # 获取验证码图片
    #     # print(self.brower.page_source)
    #     full_position = []  #
    #     bg_position = []  # 缺口散图坐标
    #     html = etree.HTML(self.brower.page_source)
    #     # 没有缺口
    #     gt_cut_fullbg_slices = html.xpath('//div[@class="gt_cut_fullbg_slice"]/@style')
    #     full_slice_url = re.findall('url\(\"(.*)\"\);', gt_cut_fullbg_slices[0])[0].replace('webp', 'jpg')
    #     # 有缺口
    #     gt_cut_bg_slices = html.xpath('//div[@class="gt_cut_bg_slice"]/@style')
    #     bg_slice_url = re.findall('url\(\"(.*)\"\);', gt_cut_bg_slices[0])[0].replace('webp', 'jpg')
    #     print(gt_cut_fullbg_slices,bg_slice_url)
    #     for i in gt_cut_fullbg_slices:
    #         position = re.findall('background-position: (.*);', i)[0].replace('px', '').split(' ')
    #         position = [int(i) for i in position]
    #         full_position.append(position)
    #     for i in gt_cut_fullbg_slices:
    #         position = re.findall('background-position: (.*);', i)[0].replace('px', '').split(' ')
    #         position = [int(i) for i in position]
    #         bg_position.append(position)
    #     print(full_position,bg_position)
    #
    #
    #     full_pic_data = requests.get(full_slice_url).content
    #     bg_pic_data = requests.get(bg_slice_url).content
    #     with open('image/full_pic.jpg', 'wb') as f:
    #         f.write(full_pic_data)
    #     with open('image/bg_pic.jpg', 'wb') as f:
    #         f.write(bg_pic_data)
    #     full_image = Image.open('image/full_pic.jpg')
    #     bg_image = Image.open('image/bg_pic.jpg')
    #     return full_image, bg_image, full_position, bg_position

    def get_Image(self, strPath='d:\captcha.png'):
        img = self.brower.find_element(By.XPATH, "//div[contains(@class,'gt_cut_bg gt_show')]")
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        screenshot = self.brower.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(strPath)
        return captcha

    def get_slider(self):
        slider = self.brower.find_element(By.XPATH, "//div[contains(@class,'gt_slider_knob gt_show')]")
        slider.click()
        return slider

    def pic_cut(self, file, position):  # 分割图片
        first_line_pic = []
        second_line_pic = []
        # full_image, bg_image, full_position, bg_position=self.get_images()
        for p in position:
            if p[1] == -58:
                first_line_pic.append(file.crop((abs(p[0]), 58, abs(p[0]) + 10, 166)))
            if p[1] == 0:
                second_line_pic.append(file.crop((abs(p[0]), 0, abs(p[0]) + 10, 58)))
        print(first_line_pic)
        print(second_line_pic)
        return first_line_pic, second_line_pic

    def merge_pics_new(self, first_line_pic, second_line_pic, file_name):
        # 新建图片
        image = Image.new('RGB', (260, 116))
        offset = 0  # 设置偏移量
        # 拼接第一行
        for i in first_line_pic:
            image.paste(i, (offset, 0))
            offset += i.size[0]
        offset_x = 0
        # 拼接第二行
        for j in second_line_pic:
            image.paste(j, (offset_x, 58))
            offset_x += j.size[0]
        image.save('image/' + file_name)  # 合成完整图片

    def merge_pics(self):  # 合并图片
        # 先割切乱码图片
        full_image, bg_image, full_position, bg_position = self.get_images()
        first_line_pic, second_line_pic = self.pic_cut(full_image, full_position)
        self.merge_pics_new(first_line_pic, second_line_pic, 'full_new_pic1.jpg')
        first_line_pic, second_line_pic = self.pic_cut(bg_image, bg_position)
        self.merge_pics_new(first_line_pic, second_line_pic, 'bg_new_pic1.jpg')

    def check_pics_is_same(self, full_image, bg_image, x, y):  # 判断图片是否一样
        pixel1 = full_image.load()[x, y]
        pixel2 = bg_image.load()[x, y]
        threshold = 50
        print('bg:{};full:{}'.format(pixel1, pixel2))
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False
        # bg_pixel = bg_image.getpixel((x, y))
        # full_pixel = full_image.getpixel((x, y))
        # print('bg:{};full:{}'.format(bg_pixel,full_pixel))
        # if bg_pixel-full_pixel >0:
        #     return False
        # else:
        #     return True
        # for i in range(0, 3):
        #     if abs(bg_pixel[i] - full_pixel[i]) >= 80:
        #         return False
        #     else:
        #         return True

    def get_gap(self, image1, image2):
        """
        获取照片缺口偏移量
        :param image1: 不带缺口图片
        :param image2: 带缺口图片
        :return:
        """
        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left
        return left

    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]

        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def reckon_distance2(self):  # 计算滑块
        try:

            # full_image = Image.open('image/full_new_pic1.jpg').convert('L')
            # full_image.save('image/full_new_pic1.jpg')
            full_image = Image.open('image/full_new_pic1.jpg')
            # bg_image = Image.open('image/bg_new_pic1.jpg').convert('L')
            # bg_image.save('image/bg_new_pic1.jpg')
            bg_image = Image.open('image/bg_new_pic1.jpg')
            time.sleep(2)

            for i in range(0, full_image.size[0]):
                for j in range(0, full_image.size[1]):
                    # time.sleep(1)
                    if not self.check_pics_is_same(full_image, bg_image, i, j):
                        return i
        except Exception as e:
            print('图片读取失败')

    def reckon_trail(self):  # 计算运动轨迹
        print('计算运动轨迹')
        track = []
        distance = self.reckon_distance2()
        distance = int(distance) - 1  # 矫正值
        # print('缺口坐标', distance)
        # fast_distance = distance * (0.85)
        # start, v0, t = 0.0, 0.0, 0.15
        # while start < distance:
        #     if start < fast_distance:  # 加速状态
        #         a = 1  # 加速
        #     else:
        #         a = -3  # 减速
        #     # 数学公式 s=v0*t+1/2 v*t平方
        #     move = v0 * t + 1 / 2 * a * t * t
        #     # 当前速度
        #     v = v0 + a * t
        #     # 重置粗速度
        #     v0 = v
        #     # 重置起始位置
        #     start += move
        #     track.append(round(move))
        # return track
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def move_block(self):  # 模拟拖动滑块
        print('开始模拟')
        track = self.reckon_trail()
        # 找寻滑块标签
        # slider = EC.presence_of_element_located((By.CLASS_NAME, 'gt_slider_knob gt_show'))
        slider = self.brower.find_element_by_xpath('/html//div[10]/div[2]/div[2]/div[2]/div[2]')

        ActionChains(self.brower).click_and_hold(slider).perform()  # 执行
        for x in track:
            ActionChains(self.brower).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.brower).release().perform()  # 释放滑块
        time.sleep(3)
        self.brower.close()

    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def move_to_gap(self, slider, track, gap):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        """
        ActionChains(self.brower).click_and_hold(slider).perform()
        # for x in track:
        #     ActionChains(self.brower).move_by_offset(xoffset=x, yoffset=0).perform()
        ActionChains(self.brower).move_by_offset(xoffset=gap, yoffset=0).perform()
        time.sleep(0.8)
        ActionChains(self.brower).release().perform()

    def active(self):
        image1 = l.get_Image()
        slider = l.get_slider()
        time.sleep(5)
        image2 = l.get_Image(strPath='captcha1.png')
        gap = l.get_gap(image1, image2)
        gap -= BORDER
        print('缺口位置', gap)
        track = l.get_track(gap)
        print('滑动轨迹', track)
        # 拖动滑块
        l.move_to_gap(slider, track, gap)
        time.sleep(5)
        while self.brower.find_element(By.XPATH, '//span[@class="gt_info_type"]') != None:
            self.brower.find_element(By.XPATH, "//a[contains(@class,'gt_refresh_button')]")
            time.sleep(5)
            image1 = l.get_Image()
            slider = l.get_slider()
            time.sleep(5)
            image2 = l.get_Image(strPath='captcha1.png')
            gap = l.get_gap(image1, image2)
            gap -= BORDER
            print('缺口位置', gap)
            track = l.get_track(gap)
            print('滑动轨迹', track)
            # 拖动滑块
            l.move_to_gap(slider, track, gap)
            time.sleep(10)
        pass


if __name__ == '__main__':
    l = Login()
    l.login()
    l.active()