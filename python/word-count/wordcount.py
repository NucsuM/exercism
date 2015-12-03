# Hint: I use python 3.4. In the last exercises I used py.test (py2.7). In this
# exercise it is important to use py.test-3.4 to have unicode-support.
# No more hassle with the vulcan salute (spock hand) in the last test :)

import re
from collections import Counter

def word_count(sentence):
    splitted_sentence = re.split('[\W|_]+', sentence.lower())
    splitted_counted_sentence = Counter(splitted_sentence) # count all items
    del splitted_counted_sentence[""] # to remove {'' : 1 ....}

    return splitted_counted_sentence
