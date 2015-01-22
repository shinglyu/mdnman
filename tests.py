import unittest
import json

import jsman


class TestSequenceFunctions(unittest.TestCase):

        def setUp(self):
            with open('testdata.json') as f:
                #print f.readlines()
                self.searchresult = json.loads(f.read())

        def test_search(self):
            query = "for"
            result = jsman.search(query)
            self.assertTrue(len(result['documents']) > 0)
            self.assertEqual("for", result['documents'][0]['title'])

            query = "for of"
            result = jsman.search(query)
            self.assertTrue(len(result['documents']) > 0)
            self.assertEqual("for...of", result['documents'][0]['title'])

        def test_get_first_result(self):
            data =self.searchresult
            title, url = jsman.getFirstResult(data)
            self.assertEqual("for...of", title)
            self.assertEqual("https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of",
                             url)


if __name__ == '__main__':
    unittest.main()
