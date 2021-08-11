from app.request import article_category, get_articles, get_source
from flask import render_template,request
from . import main
from ..request import get_articles,get_source,article_category
from app import app

#Views
@main.app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to News Api'
    newssource = get_source()
    return render_template('index.html',title = title,newssource= newssource)

@main.app('/article/<id>')
def article(id):
    
    articles = get_articles(id)
    return render_template('article.html',articles =articles,id = id)

@main.app('category<name>')
def category(name):

    category = article_category(name)
    # title = f'name'

    return render_template('category.html',category=category)
