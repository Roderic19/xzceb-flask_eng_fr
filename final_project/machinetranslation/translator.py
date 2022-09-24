""" Translator """

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishToFrench(english_text):
    """ Translate english text to french text """
    if english_text == "":
        return ""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return translation['translations'][0]['translation']

def frenchToEnglish(french_text):
    """ Translate french text to english text """
    if french_text == "":
        return ""
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return translation['translations'][0]['translation']