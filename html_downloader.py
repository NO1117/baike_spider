# -*- coding: utf-8 -*-
# Author Mr.Xu
import urllib.request


class HtmlDownloader(object):


    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        # print(response.status)
        if response.status != 200:
            return None
        # print(response.read().decode('utf-8'))
        return  response.read().decode('utf-8')


