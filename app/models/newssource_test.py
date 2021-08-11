import unittest
from models import newssource

NewsSource = newssource.NewsSource

class News_Source_Test(unittest.TestCase):
    '''
    tEST class to test behaviour of News_source class
    '''
    def setUp(self):
        '''
        setup test to run before every test
        '''
        self.new_newssource = NewsSource("techcrunch","TechCrunch")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newssource,NewsSource))

if __name__ == '__main__':
    unittest.main()