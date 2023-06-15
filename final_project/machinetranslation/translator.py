"""File responsible for functions translating French to English and vice versa"""
from deep_translator import MyMemoryTranslator

def englishToFrench(english_text):
    """Translates English to French"""
    french_text = MyMemoryTranslator(source='en', target='french').translate(english_text)
    return french_text

def frenchToEnglish(french_text):
    """Translates French to English"""
    english_text = MyMemoryTranslator(source='fr', target='english').translate(french_text)
    return english_text
