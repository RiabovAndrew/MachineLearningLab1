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
    

    
