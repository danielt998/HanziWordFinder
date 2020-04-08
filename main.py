import re

text = "你好你好我叫马斯"

MAX_WORD_LENGTH = 2
words = {}

print([m.group() for m in re.finditer(r'((\S)\2)+', text)]) #finditer is non overlapping??

#TODO: generalise for longer words
for i in range(len(text)):
    if i+2 > len(text):
        continue
    word = text[i] + text[i+1]
    if word in words.keys():
        words[word] = words[word] + 1
    else:
        words[word] = 1

print(words)