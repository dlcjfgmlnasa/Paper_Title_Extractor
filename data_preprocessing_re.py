# coding: utf-8

"""
<<사용 예시>>

path = './data'                 # (path 지정)
data_name = 'train.dat'         # (전처리할 데이터 파일명 지정)

Pre(path, data_name).process()  # 실행!
"""

import os
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

import re
from tqdm import tqdm
import pickle
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

class Pre:
    def __init__(self, path, data_name):
        self.path = path
        self.data_name = data_name
        self.min_abs_len = 32
        self.max_title_len = 32
        
    def load_data(self): # type(data_name) = 'str'
        with open(os.path.join(self.path, self.data_name), 'r', encoding='utf-8') as f:
            data = f.readlines()
            data = [i.split('\t') for i in data] # 35360개
            return data

    def posTag(self, file):
        for i, f in enumerate(file):
            tag = pos_tag(word_tokenize(f))
            if i:
                abstract = tag
                abstract.append('[SEP]')
            else:
                title = ['[SOS]']
                title.extend(tag)
        return [title, abstract]

    def shaper(self, tagged_list):
        a = '{}'.format(tagged_list)
        a = re.sub("', '", "/",a)
        a = re.sub("\(|\)",'',a)
        a = re.sub("'/',","", a)
        return eval(a)

    def write(self, tagged_list):
        tagged_name = 'tagged_{}.dat'.format(data_name.split('.')[0])
        with open(os.path.join(self.path, tagged_name), 'wb') as f:
            pickle.dump(tagged_list, f)

    def process(self):
        tagged_list = []
        data = self.load_data()
        with tqdm(total = len(data)) as pbar:
            for paper in data:
                tagged = self.posTag(paper)
                title_len = len(tagged[0])
                abstract_len = len(tagged[1])
                if title_len <= self.max_title_len and abstract_len > self.min_abs_len: # 35360 -> 35140
                    tagged_list.append(tagged)
                pbar.update(1)
        print('='*20,'데이터 쓰기 준비','='*20)
        tagged_list = self.shaper(tagged_list)
        print('='*20,'데이터 쓰기 완료','='*20)
        self.write(tagged_list)

