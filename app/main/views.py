from ..request import article_category, article_headlines, get_articles, get_source
from flask import render_template,request,redirect,url_for
from . import main



#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to News Api'
    source = get_source()
    headlines = article_headlines()
    return render_template('index.html',title = title,source= source,headlines = headlines)

@main.route('/article/<id>')
def article(id):
    
    articles = get_articles(id)
    return render_template('article.html',articles =articles,id = id)

@main.route('/category/<name>')
def category(name):

    category = article_category(name)
    # title = f'name'

    return render_template('category.html',category=category,name=name)

