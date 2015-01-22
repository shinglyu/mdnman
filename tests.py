import unittest
import json

import mdnman


class TestSequenceFunctions(unittest.TestCase):

        def setUp(self):
            with open('testdata.json') as f:
                #print f.readlines()
                self.searchresult = json.loads(f.read())

        def test_search(self):
            query = "for"
            result = mdnman.search(query)
            self.assertTrue(len(result['documents']) > 0)
            self.assertEqual("for", result['documents'][0]['title'])

            query = "for of"
            result = mdnman.search(query)
            self.assertTrue(len(result['documents']) > 0)
            self.assertEqual("for...of", result['documents'][0]['title'])

        def test_get_first_result(self):
            data =self.searchresult
            title, url = mdnman.getFirstResult(data)
            self.assertEqual("for...of", title)
            self.assertEqual("https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of",
                             url)

        def test_get_first_result_not_found(self):
            with open('testdata_notfound.json') as f:
                data = json.loads(f.read())

            title, url = mdnman.getFirstResult(data)
            self.assertEqual("Not Found", title)
            self.assertEqual(None , url)


if __name__ == '__main__':
    unittest.main()
