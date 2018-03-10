# -*- coding:utf-8 -*-
import re
import os
import urllib
import urllib2
import argparse


class Spider(object):
    def __init__(self, url, outdir='.', headers=None):
        self.url = url
        self.headers = headers
        self.outdir = outdir

    def download_img(self):
        try:
            html = urllib2.urlopen(self.url)
            page = html.read().decode('utf8')
            pattern = re.compile('img\/tiff16_e.*tif')
            list = re.findall(pattern, page)
            print 'Ready to save {} images.'.format(len(list))
            for idx, item in enumerate(list):
                self.saveImg(item)
                print 'Save Completion:No.{} image {}.'.format(idx, os.path.basename(item))

        except urllib2.HTTPError, e:
            print 'Error', e.code, ':', e.reason

    def saveImg(self, imageURL, item):
        imageURL = self.url + imageURL
        fileName = os.path.basename(item)
        fileName = self.outdir + '/' + fileName
        urllib.urlretrieve(imageURL, fileName)

        # 使用write写入图片
        # u = urllib2.urlopen(imageURL)
        # data = u.read()
        # f = open(self.outdir + '/' + fileName, 'wb')
        # f.write(data)
        # # time.sleep(7)
        # f.close()

    def run(self):
        self.download_img()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('img_url', default=None)
    parser.add_argument('out_dir', default=None)

    args = parser.parse_args()

    sp = Spider(args.img_url, args.out_dir)
    sp.run()
