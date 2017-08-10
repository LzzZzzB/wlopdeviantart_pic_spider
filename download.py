import requests

img = ['http://orig02.deviantart.net/d383/f/2017/057/2/c/15s_by_wlop-db0f6cr.jpg']
#imglist = ['http://orig02.deviantart.net/d383/f/2017/057/2/c/15s_by_wlop-db0f6cr.jpg', 'http://orig13.deviantart.net/ee41/f/2017/052/f/e/13s_by_wlop-dazyhfw.jpg', 'http://orig09.deviantart.net/d037/f/2017/045/1/0/werrr_by_wlop-daz4vvz.jpg', 'http://orig05.deviantart.net/6299/f/2017/029/3/4/9s_by_wlop-dax8mou.jpg', 'http://orig02.deviantart.net/a480/f/2017/018/7/d/8s_by_wlop-davy1hm.jpg', 'http://orig11.deviantart.net/1b02/f/2017/012/f/1/7s_by_wlop-dav41t7.jpg', 'http://orig14.deviantart.net/89e6/f/2017/001/5/a/6s_by_wlop-datwopo.jpg', 'http://orig00.deviantart.net/f00c/f/2016/361/e/f/2b_by_wlop-dat0mzo.jpg', 'http://orig14.deviantart.net/ece6/f/2016/359/7/b/4s_by_wlop-dasswtc.jpg', 'http://orig09.deviantart.net/c142/f/2016/350/f/0/2s_by_wlop-darvb38.jpg', 'http://orig08.deviantart.net/0908/f/2016/350/f/6/3333_by_wlop-dart5kp.jpg', 'http://orig04.deviantart.net/0be8/f/2016/340/4/9/1s_by_wlop-daqtf11.jpg', 'http://img08.deviantart.net/e20b/i/2016/330/a/2/cloud_insect_preview_2_by_wlop-dapqogs.jpg', 'http://img03.deviantart.net/76bb/i/2016/325/e/c/cloud_insect_preview_by_wlop-dap7ls5.jpg', 'http://orig12.deviantart.net/dc7c/f/2016/317/e/4/5ss_by_wlop-daoc8al.jpg', 'http://orig11.deviantart.net/7bac/f/2016/301/d/c/3s_by_wlop-damkn2i.jpg', 'http://orig11.deviantart.net/c4bc/f/2016/293/9/0/1s_by_wlop-dalm20x.jpg', 'http://orig06.deviantart.net/4945/f/2016/288/7/4/28_fff_by_wlop-dal1r07.jpg', 'http://orig06.deviantart.net/8b2f/f/2016/261/9/9/17s_by_wlop-dai177u.jpg', 'http://orig13.deviantart.net/e2d8/f/2016/257/0/b/16s_by_wlop-dahmcgg.jpg', 'http://img13.deviantart.net/6fbf/i/2016/248/e/2/farewell_by_wlop-dagjpdr.jpg', 'http://orig07.deviantart.net/a1f6/f/2016/242/e/3/10s_by_wlop-dafti7h.jpg', 'http://orig07.deviantart.net/124f/f/2016/234/1/1/warrior___world_of_warcraft_by_wlop-daefvr0.jpg', 'http://orig12.deviantart.net/eb42/f/2016/228/4/7/3s_by_wlop-dae4axs.jpg']


def download_pic(imglist):
    for img in imglist:
        name = img[-16:]

        resp = requests.get(img, stream=True)

        #print(type(resp))
        if resp.status_code == 200:
            with open('/Users/zhibinliu/scrapypra/wlop_pic/picc/'+name , 'wb') as f:
                for chunk in resp:
                    f.write(chunk)
                print("download",name, "successed.")


def main():
    download_pic(img)


if __name__ == '__main__':
    main()