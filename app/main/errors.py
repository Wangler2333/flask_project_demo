#!/usr/bin/python3 
# -*-coding:utf-8-*- 
# @Author: 李多
# @Time: 2018年05月08日14时08分 
# 说明: 
# 总结:

from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
