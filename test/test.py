# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import requests

h = {
    'cookie': '__tasessionId=pmbm8wabq1560302798934; csrftoken=4c2695f61f3453b523660ccfafdf8e2d; tt_webid=6701449431269082631; UM_distinctid=16b494b496c32e-0a0fe96d061c63-37c153e-144000-16b494b496d1c3; CNZZDATA1259612802=1653064915-1560297427-%7C1560297427; s_v_web_id=3dbfbfdd5fa25eb1d70ca5fadfab7882'
}
r = requests.get(
    url='https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=cosplay%E5%9B%BE%E9%9B%86&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1560302812164',
    headers=h)
print(r.status_code)
print(r.text)
