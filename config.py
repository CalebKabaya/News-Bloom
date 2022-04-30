import os


class Config:
    '''
    General configuration parent class
    '''
    # https://newsapi.org/v2/everything?
    NEWS_API_URL='https://newsapi.org/v2/sources?apiKey={}'

    NEWS_API_KEY=os.environ.get('NEWS_API_KEY') 


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
