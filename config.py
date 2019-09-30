class Config(object): 
    POSTS_PER_PAGE = 10
 
class ProdConfig(Config): 
    SECRET_KEY = '\x17fT\x0e\x9f\xc3\xff1\x19\xcdT\x8b\xc0\x95\xf8\xf5\x8b\xc9\x8a\xa6N\xa5\x8d\x8e'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
 
class DevConfig(Config): 
    DEBUG = True
    SECRET_KEY = '\x17fT\x0e\x9f\xc3\xff1\x19\xcdT\x8b\xc0\x95\xf8\xf5\x8b\xc9\x8a\xa6N\xa5\x8d\x8e'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'