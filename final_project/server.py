import machinetranslation
import json
from machinetranslation import translator
from translator import translator_instance
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('Enter English Text')
    # Write your code here
    english_text = str(textToTranslate)
    translation_response = translator_instance.translate(text = english_text, model_id = "en-fr")
    translation = translation_response.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text
    #return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('Enter Frech Text')
    french_text = str(textToTranslate)

    translation_response = translator_instance.translate(text = french_text, model_id = "fr-en")
    translation = translation_response.get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
   

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

    # Write the code to render template

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
