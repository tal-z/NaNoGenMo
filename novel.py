import re
import random

from nltk import pos_tag
from nltk.corpus import gutenberg, brown
from nltk.tokenize.treebank import TreebankWordDetokenizer
import numpy as np
from SoundsLike.SoundsLike import Search


seed_words = ["story", "poem", "poetry", "book", "sentence", "paragraph", "period", "page", "spine", "print", "bookworm"]

functions = [
    Search.perfectHomophones,
    Search.closeHomophones,
    Search.vowelClassHomophones,
    Search.phoneClassHomophones,
    Search.endRhymes,
]

for i in range(50000):
    seed_word = random.choice(seed_words)
    new_word = random.choice(functions)(seed_word)
    new_word =new_word[random.randint(0, len(new_word)-1)]
    print(new_word)
    seed_words.remove(seed_word)
    seed_words.append(new_word)
 