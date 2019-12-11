import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import pandas


with open('songofmyself.txt') as textfile:
    text = textfile.read()

### Simple wordcloud

# wordcloud = WordCloud().generate(text) 

# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()


### color masked wordcloud
mask_color = np.array(Image.open("leafmask.jpg"))
stopwords = set(STOPWORDS)
wc = WordCloud(background_color="white", max_words=200, mask=mask_color,
               stopwords=stopwords, max_font_size=60, random_state=42).generate(text)
image_colors = ImageColorGenerator(mask_color)
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off')
plt.savefig("whitman_leaf.png", bbox_inches=0, format='png')
plt.show()
