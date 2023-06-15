import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('hello'),'bonjour')
    
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

if __name__ == '__main__':
    unittest.main()