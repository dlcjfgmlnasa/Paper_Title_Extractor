# -*- coding: utf-8 -*-
"""data_prerpocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G6q-njYpqrI2pT_4Kov7UZkzyDDeMuuQ
"""

import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

with open('drive/My Drive/Paper_Title_Extractor/data/train.dat') as f:
  data = f.readlines()

train = [i.split('\t') for i in data]

def Pos_tag(file):
  tag = [pos_tag(word_tokenize(f)) for f in file]
  tags = []
  for i in tag:
    tags.append([("/".join(j)) for j in i])
  
  tags[0].append('[TITLE]')
  tags[1].append('[SEP]')

  yield tags
  
tagged_list = [Pos_tag(i) for i in paper]

print(next(tagged_list[0]))
