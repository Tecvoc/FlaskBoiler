import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'abcdefedcba'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/hero'
    # 'sqlite:///' + \
            # os.path.join(basedir, 'airportbot.sqlite')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

