import random
import json
import sys
import os
file_path = 'word_map.json'

words = ['aircraft carrier', 'airplane', 'alarm clock', 'ambulance', 'ant', 'anvil', 'apple', 'arm', 'axe',
         'backpack', 'banana', 'bandage', 'barn', 'baseball', 'baseball bat', 'basket', 'basketball', 'bat', 'bathtub',
         'beach']
path = os.path.dirname(os.path.realpath(__file__))

def word_cloud(word):
    with open(path+'/../python/word_map.json', 'r') as f:
        relation_map = json.load(f)
    n = len(words)
    ans = []
    if word in relation_map:
        if len(relation_map[word]) > 5:
            for i in range(5):
                index = random.randrange(0,len(relation_map[word]))
                if relation_map[word][index] not in ans:
                    ans.append(relation_map[word][index])
        else:
            for ele in relation_map[word]:
                ans.append(ele)

    while(len(ans)<5):
        i = random.randrange(n)
        if words[i] not in ans and words[i] != word:
            ans.append(words[i])
    return ans

def combine(sentence):
    with open(path+'/word_map.json', 'r') as f:
        relation_map  = json.load(f)

    a = None
    b = None
    s = sentence.split()
    for ele in s:
        if ele in sentence and a is None:
            a = ele
        if ele in sentence and a is not None:
            b = ele
    if a not in relation_map:
        relation_map[a] = [b]
    else:
        if b not in relation_map[a]:
            relation_map[a].append(b)



    with open(path+'/word_map.json', 'w') as f:
        json.dump(relation_map, f)




