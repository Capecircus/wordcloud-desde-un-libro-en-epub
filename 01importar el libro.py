import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

book = epub.read_epub('data/moby-dick.epub')
html_content = ''
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        html_content += item.get_content().decode('utf-8')


soup = BeautifulSoup(html_content, 'html.parser')
text = soup.get_text()

from nltk.tokenize import word_tokenize

tokens = word_tokenize(text)
for i in tokens:
    i=i.capitalize()

tokens_clean = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stopwords.words('english')]

# Crear la nube de palabras
wordcloud = WordCloud(width=800, height=800, background_color='white').generate(' '.join(tokens_clean))

# Mostrar la nube de palabras
plt.figure(figsize=(8,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()