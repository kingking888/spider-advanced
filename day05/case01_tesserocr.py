# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import tesserocr
import requests
from lxml import etree
from PIL import Image

zhiwang = requests.get(url='http://my.cnki.net/elibregister/commonRegister.aspx')
html = etree.HTML(zhiwang.text)
yanzhengma = html.xpath("//div[@class='dynamic-pic']/a/img[@id='checkcode']/@src")[0]
img = requests.get(url='http://my.cnki.net/elibregister/' + yanzhengma)
with open('tesserocr.jpg', 'wb+') as f:
    f.write(img.content)
image = Image.open('tesserocr.jpg')
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
# image.show()
result = tesserocr.image_to_text(image)
print(result)
