""" English to french and French to english translation module"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
APIKEY= os.environ['apikey']
URL = os.environ['url']
VERSION = '2018-05-01'
AUTHENTICATOR = IAMAuthenticator(APIKEY) 
translator_instance = LanguageTranslatorV3(version = VERSION, authenticator = AUTHENTICATOR)
translator_instance.set_service_url(URL)

def english_to_french(english_text):
    translation_response = translator_instance.translate(text = english_text, model_id = "en-fr")
    translation = translation_response.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translation_response = translator_instance.translate(text = french_text, model_id = "fr-en")
    translation = translation_response.get_result()
    english_text = translation['translations'][0]['translation']
    return english_text