import unittest
import getresults

class TestPersistent(unittest.TestCase):

    # This is the inverted index in the crawler for pages simple1.html and simple2.html provided in the test folder

    #def test_inverted_index(self):

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

        #self.assertEqual(self.bot.get_inverted_index()[1],set([2, 1])) # 'simple' is on both pages
        #self.assertEqual(self.bot.get_inverted_index()[2],set([2, 1])) # '2' is on both pages
       # self.assertEqual(self.bot.get_inverted_index()[3],set([2, 1])) # 'chocolate' is on both pages
        #self.assertEqual(self.bot.get_inverted_index()[4],set([2, 1])) # 'cake' is on both pages 
        #self.assertEqual(self.bot.get_inverted_index()[5],set([2])) # '1' is on simple1.html
        #self.assertEqual(self.bot.get_inverted_index()[6],set([2])) # 'icecream' is on simple1.html 
        
   def test_simple(self):

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
        
        db_lookup = getresults.getResults("dbFile.db", "simple")
        self.assertEqual(set(db_lookup), set([u'file:///nfs/ug/homes-3/v/varikoot/Desktop/csc326Project/csc326/simple2.html', u'file:///nfs/ug/homes-3/v/varikoot/Desktop/csc326Project/csc326/simple1.html'])) # 'simple' is on both pages
        

   def test_2(self):

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
        
        db_lookup = getresults.getResults("dbFile.db", "2")
        self.assertEqual(set(db_lookup), set([u'file:///nfs/ug/homes-3/v/varikoot/Desktop/csc326Project/csc326/simple2.html', u'file:///nfs/ug/homes-3/v/varikoot/Desktop/csc326Project/csc326/simple1.html'])) # 'simple' is on both pages

   def test_chocolate(self):

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
        
        db_lookup = getresults.getResults("dbFile.db", "chocolate")
        self.assertEqual(set(db_lookup), set([u'file:///nfs/ug/homes-3/v/varikoot/Desktop/csc326Project/csc326/simple2.html', u'file:///nfs/ug/homes-3/v/varikoot/Desktop/csc326Project/csc326/simple1.html'])) # 'simple' is on both pages

   def test_cake(self):

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
        
        db_lookup = getresults.getResults("dbFile.db", "cake")
        self.assertEqual(set(db_lookup), set([u'file:///nfs/ug/homes-3/v/varikoot/Desktop/csc326Project/csc326/simple2.html', u'file:///nfs/ug/homes-3/v/varikoot/Desktop/csc326Project/csc326/simple1.html'])) # 'simple' is on both pages

   def test_1(self):

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
        
        db_lookup = getresults.getResults("dbFile.db", "1")
        self.assertEqual(set(db_lookup), set([u'file:///nfs/ug/homes-3/v/varikoot/Desktop/csc326Project/csc326/simple1.html'])) # 'simple' is on both pages

   def test_icecream(self):

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
        
        db_lookup = getresults.getResults("dbFile.db", "icecream")
        self.assertEqual(set(db_lookup), set([u'file:///nfs/ug/homes-3/v/varikoot/Desktop/csc326Project/csc326/simple1.html'])) # 'simple' is on both pages

if __name__ == '__main__':
    unittest.main()
    print getresults.getResults("dbFile.db", "simple")
