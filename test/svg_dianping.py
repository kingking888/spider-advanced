# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    'Cookie': 'cy=2; cye=beijing; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=16bd48d0017c8-012bbab936a8e6-37c143e-144000-16bd48d0017c8; _lxsdk=16bd48d0017c8-012bbab936a8e6-37c143e-144000-16bd48d0017c8; _hc.v=e4f4035d-8017-a159-3224-753904080070.1562639139; s_ViewType=10; _lxsdk_s=16bd4c5032d-c6c-254-12f%7C%7C30'
}
response = requests.get(url='http://www.dianping.com/beijing/ch10/g110', headers=headers)
content = response.text
find_css_url = re.search(r'href="([^"]+svgtextcss[^"]+)"', content, re.M)
# print(find_css_url)
if not find_css_url:
    raise Exception("cannot find css_url ,check")
css_url = find_css_url.group(1)
css_url = "https:" + css_url

response_svg = requests.get(url=css_url, headers=headers)
# print(response_svg.text)

scc_list = response_svg.text.split(';}.')
# print(scc_list)
print(len(scc_list))
# print(list(set(scc_list)))
print(len(list(set(scc_list))))
# print(css_url)
# class_tag = re.findall('<svgmtsi class="(.*?)"></svgmtsi>', content, re.S)


# print(class_tag)
#
# def get_tag(_list, offset=1):
#     # 从第一个开始查
#     _new_list = [data for data in _list]
#     if len(set(_new_list)) == 1:
#         # 如果set后只有一个值，说明全部重复，这个时候就把offset加1
#         offset += 1
#         return get_tag(_list, offset)
#     else:
#         # _return_data = [data[0:offset - 1] for data in _list][0]
#         print(len(_new_list))
#         print(_new_list)
#         return list(set(_new_list))
#
#
# _tag = get_tag(class_tag)
# print(len(_tag))
# print(_tag)
