import unittest
from crawler import *
from getresults import *

class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.con = lite.connect("dbFile.db")
        self.bot = crawler(self.con, "urls.txt")
        self.bot.crawl(depth=1)
        self.bot.generate_page_ranks(self.bot._links)
        self.curs = self.con.cursor()
        

    def test_inverted_index(self):

        # Word Id Mapping:
        # 'simple' - 1
        # 'chocolate' - 3
        # '1' - 5
        # 'icecream' - 6
        # '2' - 2
        # 'cake' - 4

        # Doc Id Mapping:
        # 'simple2.html' - 1
        # 'simple1.html' - 2

        self.assertEqual(self.bot.get_inverted_index()[1],set([2, 1])) # 'simple' is on both pages
        self.assertEqual(self.bot.get_inverted_index()[2],set([2, 1])) # '2' is on both pages
        self.assertEqual(self.bot.get_inverted_index()[3],set([2, 1])) # 'chocolate' is on both pages
        self.assertEqual(self.bot.get_inverted_index()[4],set([2, 1])) # 'cake' is on both pages 
        self.assertEqual(self.bot.get_inverted_index()[5],set([2])) # '1' is on simple1.html
        self.assertEqual(self.bot.get_inverted_index()[6],set([2])) # 'icecream' is on simple1.html 


if __name__ == '__main__':
    unittest.main()
    print getresults.getResults("dbFile.db", "simple")
