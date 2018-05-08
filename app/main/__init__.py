#!/usr/bin/python3 
# -*-coding:utf-8-*- 
# @Author: 李多
# @Time: 2018年05月08日14时07分 
# 说明: 
# 总结:

from flask import Blueprint

main = Blueprint('main', __name__)
from . import views, errors
