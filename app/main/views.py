#!/usr/bin/python3 
# -*-coding:utf-8-*- 
# @Author: 李多
# @Time: 2018年05月08日14时08分 
# 说明: 设计此app使用的视图，蓝图为main
# 总结:

from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # ...
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False),
                           current_time=datetime.utcnow())
