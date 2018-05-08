#!/usr/bin/python3 
# -*-coding:utf-8-*- 
# @Author: 李多
# @Time: 2018年05月08日14时07分 
# 说明: 
# 总结:

from flask.ext.wtf import Form
# 导入自定义表单需要的字段
from wtforms import SubmitField, StringField, PasswordField
# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired, EqualTo


class NameForm(Form):
    us = StringField(label=u'用户：', validators=[DataRequired()])
    ps = PasswordField(label=u'密码', validators=[DataRequired(), EqualTo('ps2', 'err')])
    ps2 = PasswordField(label=u'确认密码', validators=[DataRequired()])
    submit = SubmitField(u'提交')
