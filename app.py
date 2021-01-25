from flask import Flask, jsonify, request, send_file

import re
import regex
import pandas as pd
import numpy as np
import spacy
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from io import BytesIO
import random
import time
import os
import requests
import wikipedia as wk

import config
import en_core_web_sm
nlp = en_core_web_sm.load()

import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')

app = Flask(__name__)

# Tokens
@app.route('/api/v1/tokens/<string:mytext>',methods=['GET'])
def tokens(mytext):
	# Analysis
	docx = nlp(mytext)
	# Tokens
	mytokens = [token.text for token in docx ]
	return jsonify(mytext,len(mytokens))

# Lemma
@app.route('/api/v1/lemma/<string:mytext>',methods=['GET'])
def lemma(mytext):
	# Analysis
	docx = nlp(mytext.strip())
	# Tokens & Lemma
	mylemma = [('Token:{},Lemma:{}'.format(token.text,token.lemma_))for token in docx ]
	return jsonify(mytext,mylemma)

# NER
@app.route('/api/v1/ner/<string:mytext>',methods=['GET'])
def ner(mytext):
	# Analysis
	docx = nlp(mytext)
	# Tokens
	mynamedentities = [(entity.text,entity.label_)for entity in docx.ents]
	return jsonify(mytext,mynamedentities)


# Sentiment analysis
@app.route('/api/v1/sentiment/<string:mytext>',methods=['GET'])
def sentiment(mytext):
	# Analysis
	blob = TextBlob(mytext)
	mysentiment = [ mytext,blob.sentiment ]
	return jsonify(mysentiment)

# Word cloud
@app.route('/api/v1/wordcloud/<string:mytext>', methods=['Get'])
def fig(mytext):
    plt.figure(figsize=(20,10))
    wordcloud = WordCloud(background_color='white', mode = "RGB", width = 2000, height = 1000).generate(mytext)
    plt.imshow(wordcloud)
    plt.axis("off")
    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    return img


# wikipedia summary
@app.route('/api/v1/wiki_summary/<string:mytext>',methods=['GET'])
def wiki_summary(mytext):
	# Analysis
	wiki_info = wk.summary(mytext, sentences = 8)
	return jsonify(wiki_info)

# wikipedia page images
@app.route('/api/v1/wiki_img/<string:mytext>',methods=['GET'])
def wiki_img(mytext):
  wiki_page = wk.page(mytext)
  imgs = wiki_page.images
  return jsonify(imgs)

# wikipedia page content
@app.route('/api/v1/wiki_content/<string:mytext>',methods=['GET'])
def wiki_content(mytext):
  wiki_page = wk.page(mytext)
  content = wiki_page.content
  return jsonify(content)


# wikipedia page ner
@app.route('/api/v1/wiki_ner/<string:mytext>',methods=['GET'])
def wiki_ner(mytext):
  wiki_page = wk.page(mytext)
  content = wiki_page.content
  docx = nlp(content)
  mynamedentities = [(entity.text,entity.label_)for entity in docx.ents]
  return jsonify(mytext,mynamedentities)

# sentiment analysis
@app.route('/api/v1/wiki_sentiment/<string:mytext>',methods=['GET'])
def wiki_sentiment(mytext):
  wiki_page = wk.page(mytext)
  content = wiki_page.content
  blob = TextBlob(content)
  sentiment = [ mytext,blob.sentiment ]
  return jsonify(sentiment)

# Wikipedia Word cloud
@app.route('/api/v1/wiki_wordcloud/<string:mytext>', methods=['Get'])
def wiki_fig(mytext):
    wiki_page = wk.page(mytext)
    content = wiki_page.content
    plt.figure(figsize=(20,10))
    wordcloud = WordCloud(background_color='white', mode = "RGB", width = 2000, height = 1000).generate(content)
    plt.imshow(wordcloud)
    plt.axis("off")
    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    return img

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
