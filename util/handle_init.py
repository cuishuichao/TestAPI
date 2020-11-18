# -*- coding: utf-8 -*-
import configparser

from util.base_path import get_path


class HandleInit:
    def __init__(self, path):
        self.path = path

    def load_ini(self):
        file_path = get_path(self.path)
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding='utf-8-sig')
        return cf

    def get_value(self, key, node=None):
        if node is None:
            node = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(node, key)
        except:
            data = None
        return data


if __name__ == '__main__':
    hi = HandleInit('/config/server.ini')
    print(hi.get_value('username', 'auth'))
    print(hi.get_value('t-mpadminapi'))
    print(hi.get_value('pre-mpapi'))
    print(hi.get_value('mpadminapi'))
