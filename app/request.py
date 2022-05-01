import urllib.request,json
from .models import Source,Article,Headlines,Topics



#to get my api key from config
api_key =None
#to get my news_url from config
news_url=None
#to get my topic_url from config
topic_url=None

#configure
def config_request(app):
    global api_key,news_url,topic_url
    api_key= app.config['NEWS_API_KEY']
    news_url= app.config['NEWS_API_URL']
    topic_url= app.config['TOPIC_API_URL']


def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url= news_url.format(api_key)
    # print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data= url.read()
        get_news_response= json.loads(get_news_data)
        # print(get_news_response)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results
    # print(news_results)


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    
    news_results =[]
    for news_item in news_list:
        id=news_item.get('id')
        name=news_item.get('name')
        description= news_item.get('description')
        url = news_item.get('url')
        if id:
            source_object = Source(id,name,description,url)
            news_results.append(source_object)

        return news_results

def get_headlines():
    get_headlines_url='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_headlines_url)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data =url.read()
        get_headlines_response= json.loads(get_headlines_data)
        # print(get_headlines_response)
        get_headlines_results=None

        if get_headlines_response['articles']:
            get_headlines_list= get_headlines_response['articles']
            get_headlines_results= process_articles_results(get_headlines_list)

    return get_headlines_results
def article_source(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    # print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results

def process_articles_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in news:
        author = article.get('author')
        description = article.get('description')
        time = article.get('publishedAt')
        url = article.get('urlToImage')
        image = article.get('url')
        title = article.get ('title')

        if url:
            article_objects = Article(author,description,time,image,url,title)
            article_source_results.append(article_objects)

    return article_source_results

def get_news_topics(topic_name):
    '''
    function that gets the response to the category json
    '''
    get_topic_url= topic_url.format(topic_name,api_key)
    with urllib.request.urlopen(get_topic_url) as url:
        get_topic_data=url.read()
        get_topic_response=json.loads(get_topic_data)
        # print(get_topic_response)
        get_topic_results=None

        if get_topic_response['articles']:
            get_topic_list= get_topic_response['articles']
            get_topic_results= process_articles_results(get_topic_list)

    return get_topic_results        


    

  