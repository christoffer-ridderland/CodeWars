# https://www.codewars.com/kata/523a86aa4230ebb5420001e1
def letterCounter(word):
    letters = {}
    for letter in word:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def anagrams(word, words):
    anag = []
    wordMap = letterCounter(word)
    for w in words:
        if wordMap == letterCounter(w):
            anag.append(w)
    return anag