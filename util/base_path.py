# -*- coding: utf-8 -*-
import os


def get_path(file):
    base_path = os.path.abspath(os.path.dirname(os.getcwd()))
    return base_path + file
