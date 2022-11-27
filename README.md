# MachineLearningLab1<br>Andrey Ryabov

![image](https://user-images.githubusercontent.com/43186510/204151424-e9a5cda5-89b3-4628-8aa0-a4f445ef160c.png)

## Solution

1) Let's create _uninteresting_words_ as array of exclusions.
```
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
"we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers",
"its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am",
"are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did",
"but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both",
"each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", "on", "in"]
```
2) Use any file with text. I'll use _food.txt_. Open this file and read.
```
with open("food.txt", "r", encoding="utf8") as file:
    text = file.read()
```
3) Using regex (_re_) from python lib generate array of words.
```
words = [w.lower() for w in re.findall("\\w+", text)]
```
4) Filter words using `filter()` function with filtering functor.
Functor code:
```
def wordFilterFunctor(item: str):
    try:
        uninteresting_words.index(item)
    except:
        return True
    return False
```
Filtering:
```
filteredWords = list(filter(wordFilterFunctor, words))
```
5) Prepare word dictionary form list of filtered words.
```
wordDictionary = {word: filteredWords.count(word) for word in filteredWords}
```
6) Now just use _wordCloud_ lib in order to generate wordCloud.
```
wordCloud = wordcloud.WordCloud(height=1080, width=1920).generate_from_frequencies(wordDictionary)
```
7) Let's save file _wordCloud_ to file and also show this on screen using _plt_ lib.
```
    # In case if you want to save image as png
    wordCloud.to_file("new.png")

    # In case if you want to show image immidiately
    plt.imshow(wordCloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
```

## Code of solution
main.py
```
import re
from matplotlib import pyplot as plt
import wordcloud


uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
"we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers",
"its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am",
"are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did",
"but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both",
"each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", "on", "in"]

def wordFilterFunctor(item: str):
    try:
        uninteresting_words.index(item)
    except:
        return True
    return False

with open("food.txt", "r", encoding="utf8") as file:
    text = file.read()

    words = [w.lower() for w in re.findall("\\w+", text)]
    filteredWords = list(filter(wordFilterFunctor, words))
    wordDictionary = {word: filteredWords.count(word) for word in filteredWords}
    wordCloud = wordcloud.WordCloud(height=1080, width=1920).generate_from_frequencies(wordDictionary)

    # In case if you want to save image as png
    wordCloud.to_file("new.png")

    # In case if you want to show image immidiately
    plt.imshow(wordCloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
```

Directory should looks like:

![image](https://user-images.githubusercontent.com/43186510/204152031-735618f6-e1c4-4bfc-846c-6944480d3d03.png)
