 import os

class Config:

    NEWS_API_BASE_URL ='https://api.thenewsdb.org/3/news/{}?api_key={6513ca4ce81d445086dbe242903fad72}
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
