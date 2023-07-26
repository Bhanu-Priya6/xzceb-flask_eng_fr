""" Unit tests """
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """ English to French """
    def test1(self):
        self.assertIsNotNone(english_to_french('Hello'))
    def test2(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test3(self):
        self.assertNotEqual(english_to_french('Hello'),'Hallo')

class TestFrenchToEnglish(unittest.TestCase):
    """ French to English """
    def test1(self):
        self.assertIsNotNone(french_to_english('Bonjour'))
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test3(self):
        self.assertNotEqual(french_to_english('Bonjour'),'Guten Tag')

unittest.main()
