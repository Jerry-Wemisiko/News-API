class NewsSource:
    '''
    News source class to define source object of news
    '''
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url

class Article:
    '''
    article class to define article object of the news source
    '''
    def __init__(self,title,description,url,urlToImage,publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
    
 