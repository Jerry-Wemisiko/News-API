import urllib.request,json
from .models import Article,Source,Category,Headlines


# Getting api key
api_key = None

# Getting the news base url
base_url= None

#Category url from source
name_cat_url = None


def configure_request(app):
    global api_key,base_url,name_cat_url
    
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    name_cat_url = app.config['NEWS_CAT_API_URL']

def get_source():

    get_source_url = base_url.format(api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_sources(source_results_list)

    return source_results
def process_sources(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
       source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results =[]
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        
        if id:
            source_object = Source(id,name,description,url)

            source_results.append(source_object)

    return source_results

def  get_articles():
    articles_base_url='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(articles_base_url)

    with urllib.request.urlopen(articles_base_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_results = None

        if articles_response['articles']:
            articles_list = articles_response['articles']
            articles_results = process_article_results(articles_list)

    return articles_results

def process_article_results(articles_list):
    
    articles_source_results = []

    for article_item in articles_list:
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

    if url:
        article_object = Article(title,description,url,urlToImage,publishedAt)
        articles_source_results.append(article_object)

    return articles_source_results

def article_category(name):

    article_category = name_cat_url.format(name,api_key)
    print(article_category)
    with urllib.request.urlopen(article_category) as url:
        article_category_data = url.read()
        article_category_response =json.loads(article_category_data)

        article_category_results = None

        if article_category_response['articles']:
            article_category_list = article_category_response['articles']
            article_category_results = process_article_results(article_category_list)

    return article_category_results

def article_headlines():

    article_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(article_headlines_url)

    with urllib.request.urlopen(article_headlines_url) as url:
        articles_headlines_data = url.read()
        article_headlines_response = json.loads(articles_headlines_data) 

        article_headlines_results = None

        if article_headlines_response['articles']:
            article_headlines_list = article_headlines_response['articles']
            article_headlines_results = process_article_results(article_headlines_list)

    return article_headlines_results      



    


