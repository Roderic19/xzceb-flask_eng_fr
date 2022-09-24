import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(englishToFrench("Game"), "Jeu")
        self.assertEqual(englishToFrench("Goodbye"), "Au revoir")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(englishToFrench(""), "")

    def test_french_to_fenglish(self):
        self.assertEqual(frenchToEnglish("Jeu"), "Game")
        self.assertEqual(frenchToEnglish("Au revoir"), "Goodbye")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(frenchToEnglish(""), "")

unittest.main()