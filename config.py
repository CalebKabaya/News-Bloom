import os

class Config:

      # https://newsapi.org/v2/everything?
    NEWS_API_URL='https://newsapi.org/v2/sources?apiKey={}'

    NEWS_API_KEY=os.environ.get('NEWS_API_KEY') 
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    TOPIC_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
