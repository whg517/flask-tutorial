# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: flask-tutorial
@File:  test_tmp
@Date: 2019/8/22 上午10:36
@Description:

"""


def test_tmp(client):
    response = client.get('/tmp')
    assert b'bbb' == response.data
