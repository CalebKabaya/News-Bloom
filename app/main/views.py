from flask import render_template,request,url_for
from . import main
from flask import render_template,request,redirect,url_for
from ..request import get_news,article_source,get_headlines, get_news_topics

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

@main.route('/topics/<topic_name>')
def topic(topic_name):
    """
    a func that returns the topics.html
    """

    thetopics=get_news_topics(topic_name)
    title=f'{topic_name}'
    tops=topic_name

    return render_template('topics.html',title=title, thetopics=thetopics,tops=tops)
