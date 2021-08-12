class Article:
    '''
    Article class to define article object of the news source
    '''
    def __init__(self,title,description,url,urlToImage,publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Category:
    '''
    Category class to define category object of the articles
    '''
    def __init__(self,title,description,url,urlToImage,publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Source:
    '''
    News source class to define source object of news
    '''
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url

class Headlines:
    '''
    Headline class to define headline object of the articles
    '''
    def __init__(self,title,description,url,urlToImage,publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
