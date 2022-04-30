import urllib.request,json
from .models import Source



#to get my api key from config
api_key =None
#to get my news_url from config
news_url=None

#configure
def config_request(app):
    global api_key,news_url
    api_key= app.config['NEWS_API_KEY']
    news_url= app.config['NEWS_API_URL']

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
  