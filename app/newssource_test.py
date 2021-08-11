import unittest
from models import Source

class Source_Test(unittest.TestCase):
    '''
    tEST class to test behaviour of News_source class
    '''
    def setUp(self):
        '''
        setup test to run before every test
        '''
        self.new_newssource = Source("bbc-sport","BBC Sport", "The home of BBC Sport online. Includes live sports coverage, breaking news, results, video, audio and analysis on Football, F1, Cricket, Rugby Union, Rugby League, Golf, Tennis and all the main world sports, plus major events such as the Olympic Games.","http://www.bbc.co.uk/sport")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newssource,Source))

if __name__ == '__main__':
    unittest.main()