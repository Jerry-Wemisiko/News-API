import unittest
from app.models import Source

class SourceTest(unittest.TestCase):

    def setUp(self):

        self.new_source = Source('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com','http://abcnews.go.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
        
if __name__ == '__main__':
    unittest.main()
