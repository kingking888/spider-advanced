# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import requests, re

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    'Cookie': 'ssuid=7302831308; TYCID=30e2fc40949911e98c9dc16387d9eeb3; undefined=30e2fc40949911e98c9dc16387d9eeb3; _ga=GA1.2.1083252562.1561172141; aliyungf_tc=AQAAAMxDZjmYSQwAC6Hd3T9SUCJncB+n; csrfToken=XO9TLdVWKKOoKSZCXsnmv0Kf; bannerFlag=undefined; RTYCID=c24d9973eb8944d8bfae77b5bfd2eefd; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1561424433; CT_TYCID=ece5d43726ef472394b8631d9f5898f6; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%25AD%2594%25E8%259E%258D%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4MzMwNjMzNyIsImlhdCI6MTU2MTQyNDQ1NywiZXhwIjoxNTkyOTYwNDU3fQ.UBZ13sf569HBxuRgbjI_G85N2UVb8NsZM3OPP5XAse6IdxNH6J9V02oz2pKjFlZU1kfcX_l12RTR-OdkDgLhpw%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213383306337%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4MzMwNjMzNyIsImlhdCI6MTU2MTQyNDQ1NywiZXhwIjoxNTkyOTYwNDU3fQ.UBZ13sf569HBxuRgbjI_G85N2UVb8NsZM3OPP5XAse6IdxNH6J9V02oz2pKjFlZU1kfcX_l12RTR-OdkDgLhpw; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1561424463; cloud_token=e1418f7399864c0680d7758abeb515c0; cloud_utm=48ec51860136441f847d8973279ec5e1',
}

url = 'https://www.tianyancha.com/company/2347425611'
rr = requests.get(url, headers=headers)
aa = re.sub('\n', '', rr.text)
print(aa)
addr = re.findall('邮箱：</span>(.*?)</span>', aa, re.S)
print(addr)
call = ''
mail = ''
