import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('abcnews','ABc-News.','View the latest news and breaking news today for U.S and around the world','https://www.reuters.com/world/europe/may-day-marchers-france-put-pressure-re-elected-macron-2022-05-01/')

    def test_instance(self):
        '''
        Test to check creation of new article Source instance
        '''
        self.assertTrue(isinstance(self.new_source,Source))