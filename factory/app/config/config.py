import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))


def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(basedir, db_name)


class BaseConfig:  # 基本配置
    SECRET_KEY = 'THIS IS MAX'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=14)


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mycard_1688@192.168.11.128:3306/app'


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("test.db")


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
