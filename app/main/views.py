from flask import render_template,request,url_for
from . import main
from flask import render_template,request,redirect,url_for
from ..request import get_news,article_source,get_category,get_headlines

@main.route('/')
def index():
    """
    return the render_template which is index.html
    
    """
    source= get_news()
    return render_template('index.html',sources=source)

@main.route('/article/<id>') 
def article(id):
    """
    view the article page
    """
    articles=article_source(id)
    return render_template('article.html',articles= articles,id=id )


