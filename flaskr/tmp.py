# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: flask-tutorial
@File:  tmp
@Date: 2019/8/22 上午10:35
@Description:

"""
from flask import Blueprint

bp = Blueprint('tmp', __name__)


@bp.route('/tmp')
def tmp():
    return 'bbb'
