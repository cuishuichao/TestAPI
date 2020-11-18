# -*- coding: utf-8 -*-
import json

import requests


class BaseRequest:
    def __init__(self, url, data, method):
        self.url = url
        self.data = data
        self.method = method

    def send_post(self):
        response = requests.post(url=self.url, data=self.data)
        res = response.text
        return res

    def send_get(self):
        response = requests.get(url=self.url, data=self.data)
        res = response.text
        return res

    def run_main(self):
        if self.method == 'GET':
            res = self.send_get()
        else:
            res = self.send_post()
        try:
            res = json.loads(res)
        except TypeError:
            print("这个结果是 text")
        return res
