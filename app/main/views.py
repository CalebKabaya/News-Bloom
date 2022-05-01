from flask import render_template,request,url_for
from . import main
from flask import render_template,request,redirect,url_for
from ..request import get_news,article_source,get_headlines

@main.route('/')
def index():
    """
    return the render_template which is index.html
    
    """
    source= get_news()
    article=get_headlines()
    return render_template('index.html',sources=source, articles=article)

@main.route('/article/<id>') 
def article(id):
    """
    view the article page
    """
    articles=article_source(id)
    return render_template('article.html',articles= articles,id=id )


