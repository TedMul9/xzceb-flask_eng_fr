import unittest
from translator import english_to_french
from translator import french_to_english

class TestEn2Fr(unittest.TestCase):
    def test1(self):
        #self.assertEqual(english_to_french('Null'), '')
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french('0'), '0')
    

class TestFe2En(unittest.TestCase):
    def test1(self):
        #self.assertEqual(frenchToEnglish('null'), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Null'), 'Null')

unittest.main()