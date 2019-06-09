# -*- coding: utf-8 -*-
# -*- author: GXR -*-

import requests
from lxml import etree

for page in range(0, 100, 10):
    print(page)
    response = requests.get('https://maoyan.com/board/4?offset=' + str(page))
    html = etree.HTML(response.text)
    title = html.xpath("//div[@class='movie-item-info']/p[@class='name']/a/text()")
    print(title)
