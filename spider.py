from urllib.parse import urlencode
import download
import requests
import re
import json


# 返回1~7页的连接
def make_url():
    url_list = []
    base_url = 'http://www.deviantart.com/dapi/v1/gallery/23512439?'
    for n in range(1,8):
        data = {
            'iid': '579m684fb66330e9b5404739ffaefa446eb3 - j665oo0w - 1.1',
            'mp': n,
        }
        quries = urlencode(data)
        #print(quries)
        url = base_url + quries
        #print(url)
        url_list.append(url)
    print(url_list)
    return url_list


#
def get_html(url):
    num = url[-1]
    #print('n 等于', n)
    #print(url)
    n = str(24*int(num))          # 注意n的运算，本来n是一个str，运算要先改成int，然后转为str给data使用
    #print(type(n))
    #print(n)
    data = {
        'username': 'wlop',
        'offset': n,
        'limit': '24',
        '_csrf': 'kTM8otrmRSeTXVWE.ougmc9.au7kCV-gYn2a4P5mUHJIWdJLartHdJ0j1YZlAXcGoU4',
        'dapiIid': '579m684fb66330e9b5404739ffaefa446eb3-j665oo0w-1.1'
    }
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '164',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '__qca=P0-869274252-1502351979903; _gat=1; tw=%7B%22gallery%22%3A877%2C%22userprofile-zone-1%22%3A518%7D; _ga=GA1.2.2002268016.1502351977; _gid=GA1.2.806349571.1502351977; userinfo=__bea37f819a3bf5dd91a1%3B%7B%22username%22%3A%22%22%2C%22uniqueid%22%3A%229f4727e23366b4ae5c278b18e7f64c64%22%2C%22vd%22%3A%22BZjBJk%2CBZjBJk%2CA%2CM%2CA%2C%2CB%2CA%2CB%2CBZjBJk%2CBZjBMb%2CE%2CE%2CA%2CBZjBLH%2C13%2CA%2CB%2CA%2C%2CA%2CA%2CB%2CA%2CA%2C%2CA%22%7D',
        'Host': 'www.deviantart.com',
        'Origin': 'http://wlop.deviantart.com',
        'Referer': 'http://wlop.deviantart.com/gallery/?coffset=250',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    #url = 'http://www.deviantart.com/dapi/v1/gallery/23512439?iid=579m684fb66330e9b5404739ffaefa446eb3-j665oo0w-1.1&mp=1'
    resp = requests.post(url, data=data, headers=headers)
    html = resp.text
    #print(resp.text)
    print("This page is ....<<", num, ">>")
    parse_html(html)


def parse_html(html):
    js = json.loads(html)
    jsjs = js['content']['results']
    jsjs = str(jsjs)
    pattern = re.compile('data-super-full-img="(.*?)"')
    full_img = re.findall(pattern, jsjs)
    # print(len(full_img))
    # print(type(full_img))
    #print(full_img)
    download.download_pic(full_img)


def main():
    list = make_url()
    for url in list:
        get_html(url)


if __name__ == '__main__':
    main()