from app.newssource_test import NewsSource
from os import getgrouplist
from app import app
import urllib.request,json
from .models import Article,Source


api_key = None

base_url= None

def get_source(category):

    get_source_url = base_url.format(category,api_key)

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
            source_object = NewsSource(id,name,description,url)

            source_results.append(source_object)

        return source_results

    


