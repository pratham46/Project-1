from os import path
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS


currdir = path.dirname(__file__)

def get_wiki(query):
	
	title = wikipedia.search(query)[0]

	page = wikipedia.page(title)
	return page.content


def create_wordcloud(text):

	mask = np.array(Image.open(path.join(currdir, "cloud1.png")))
	
	stopwords = set(STOPWORDS)

	wc = WordCloud(background_color="white",
					max_words=200, 
					mask=mask,
	               	stopwords=stopwords)

	wc.generate(text)

	wc.to_file(path.join(currdir, "country.png"))


if __name__ == "__main__":
	
	text = get_wiki("india")
	
	
	create_wordcloud(text)
