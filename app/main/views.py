from flask import render_template,request,url_for
from . import main
from flask import render_template,request,redirect,url_for
from ..request import get_news

@main.route('/')
def index():
    """
    return the render_template which is index.html
    
    """
    datas= get_news()
    return render_template('index.html',mydata=datas)
