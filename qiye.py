from hashlib import md5

import requests
from lxml import html
import os

from sqlalchemy import true

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 'AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31'
}
while true:
    url = input('请输入视频网址：')
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, verify=False).text
    selector = html.fromstring(response)
    imgEle = selector.xpath('//div[@class="preview-box video-preview"]/video/source')
    for img in imgEle:
        imgUrl = img.xpath('@src')[0]
        file = input('请输入视频名称：')
        response = requests.get(imgUrl, headers=headers)
        data = response.content
        if data:
            if not os.path.exists(file):
                with open(file + ".mp4", 'wb')as f:
                    f.write(data)
                    f.close()
                    print('视频下载成功:' + file)