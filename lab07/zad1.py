import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Otwórz plik i przeczytaj zawartość
with open('zad1.txt', 'r') as file:
    data = file.read()

# # Dokonaj tokenizacji
# tokens = nltk.word_tokenize(data)
#
# print(tokens)

raw_text = data.lower()
# create mapping of unique chars to integers
tokenized_text = wordpunct_tokenize(raw_text)
tokenized_text_count = len(tokenized_text)
# tokens = sorted(list(dict.fromkeys(tokenized_text)))

print(tokenized_text_count)

stop_words = set(stopwords.words('english'))

filtered_text = [tok for tok in tokenized_text if not tok in stop_words]

print(len(filtered_text))

stop_words.add('no')

filtered_text2 = [tok for tok in tokenized_text if not tok in stop_words]

print(len(filtered_text2))

lemmatizer = WordNetLemmatizer()

lemmatized_text = [lemmatizer.lemmatize(tok) for tok in filtered_text2]

print(lemmatized_text)

# Przetworzony dokument w formie wektora zliczającego słowa
word_counts = Counter(lemmatized_text)

# Wyświetl 10 najczęściej występujących słów
most_common_words = word_counts.most_common(10)

# Przygotuj dane do wykresu
words, counts = zip(*most_common_words)

# Utwórz wykres słupkowy
plt.bar(words, counts)
plt.xlabel('Words')
plt.ylabel('Counts')
plt.title('10 najczęściej występujących słów')
plt.show()

# Stwórz chmurę tagów
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stop_words,
                      min_font_size=10).generate(' '.join(lemmatized_text))

# Wyświetl chmurę tagów
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()