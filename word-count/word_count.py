from collections import defaultdict
import re

def word_count(phrase):
    phrase = re.sub('[^a-zA-Z0-9\n\.]', ' ', phrase).rstrip('.')
    words = phrase.lower().split()
    d = {}
    d = defaultdict(lambda: 0, d)
    
    for word in words:
        d[word] += 1
    
    return d



