class Source:
    '''
    Source class to define source objects
    '''

    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url

class Headlines:
    '''
    Class for headlines categories 
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title  

class Article:
    '''
    Class that instantiates objects of the news article objects of the news sources
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title    

class Topics:
    '''
    Class that instantiates objects of the news topic objects of the news sources
    '''
    def __init__(self,author,description,time,url,image,title):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title                    