#! /usr/bin/python3
import nltk
from nltk.corpus import brown
import random

from time import sleep
from os import system

system('clear')

# get corpus
corpus = list(brown.sents())
random.shuffle(corpus)
corpus = corpus[:1000]

# separate words by tag
tags = {}
for sent in corpus:
    tagged = nltk.pos_tag(sent)
    for word, tag in tagged:
        tags.setdefault(tag, [])
        if word not in tags[tag]:
            tags[tag] += [word]

# filter corpus
corpus = [sent for sent in corpus if sent[-1] == '.' and len(sent) > 4]

good_tags = [
    'CC',  # coordinating conjunction
    'IN',  # preposition/subordinating conjunction
    'MD',  # modal (could, will)
    'VBZ'  # verb, 3rd person sing. present
]

# create questions
for i in range(5):
    # choose the sentence
    sent = random.choice(corpus)
    tagged = nltk.pos_tag(sent)

    # choose the missing word
    good_words = [(word, tag) for word, tag in tagged if tag in good_tags]
    if good_words == []:
        continue
    missing_word, missing_tag = random.choice(good_words)
    sent[sent.index(missing_word)] = '....'

    # create the items
    items = [missing_word]
    while len(items) < 5:
        item = random.choice(tags[missing_tag])
        if item not in items:
            items += [item]
            continue

        if len(tags[missing_tag]) < 5:
            tag = random.choice(good_tags)
            item = random.choice(tags[tag])
            if item not in items:
                items += [item]
    random.shuffle(items)

    # print the question
    print('QUESTION', i, end='\n\n')
    print(' '.join(sent), end='\n\n')
    for idx, item in enumerate(items):
        print(' ', idx, ') ', item, sep='')

    answer = int(input('\nAnswer: '))
    if items[answer] == missing_word:
        print('CORRECT!')
    else:
        print('INCORRECT :(')
    print('\n')
    sleep(2)
    system('clear')
