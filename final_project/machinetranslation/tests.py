import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour") # test when Hello is given as input the output is Bonjour.
        self.assertEqual(englishToFrench("Bye"), "Au revoir") # test when Bye is given as input the output is Au revoir.
       
class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") # test when Bonjour is given as input the output is Hello.
        self.assertEqual(frenchToEnglish("Au revoir"), "Bye") # test when Au revoir is given as input the output is Bye.
unittest.main()