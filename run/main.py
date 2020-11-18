# -*- coding: utf-8 -*-
from base.base_request import BaseRequest

if __name__ == '__main__':
    data = {"account": "cuishuichao", "password": "123456"}
    url = 'https://jeff.xiucai.com/api/auth/account/login'
    method = 'POST'
    request = BaseRequest(url, data, method)
    res = request.run_main()
    print(res)
