#!/usr/bin/python3 
# -*-coding:utf-8-*- 
# @Author: 李多
# @Time: 2018年05月08日14时04分 
# 说明: 构建app_create方法，动态加载配置文件
# 总结:

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def app_create(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    # 路由和其他处理程序定义
    # ...
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
