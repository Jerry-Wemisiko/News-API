import unittest
from  app.models import Article

class  ArticleTest(unittest.TestCase):
    
    def setUp(self):
        self,new_article = Article("Are hydrogen fuel cells the future of green transport? Sorta","Around the world, governments are implementing policies ..",
                                    "https://thenextweb.com/news/are-hydrogen-fuel-cells-the-future-of-green-transport-sorta",
                                    "https://img-cdn.tnwcdn.com/image/shift?filter_last=1&fit=1280%2C640&url=https%3A%2F%2Fcdn0.tnwcdn.com%2Fwp-content%2Fblogs.dir%2F1%2Ffiles%2F2021%2F08%2Fr_MIR_MY21_0006_V001.jpeg&signature=ca3714ab69d07634973e1c4505d67cb8",
                                    "2021-08-11T09:46:58Z")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
    