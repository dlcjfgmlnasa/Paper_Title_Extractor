# -*- coding:utf-8 -*-
import os
import random
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', default='arxiv', choices=['arxiv', ], type=str)
    parser.add_argument('--collect', action='store_true')
    return parser.parse_args()


BASE_DIR = './data'


def collect_arxiv_paper_dataset():
    # Arxiv Paper 데이터셋 수집
    import arxiv
    keywords = open(os.path.join(BASE_DIR, 'keyword'), 'r', encoding='utf-8').readlines()

    # Collecting Dataset
    total_content = []
    for keyword in keywords:
        keyword = keyword.strip()
        temp = arxiv.query(query=keyword, max_results=10)
        for t in temp:
            title = ' '.join(t['title'].split())
            summary = ' '.join(t['summary'].split())
            line = title + '\t' + summary
            total_content.append(line)

    # Shuffling
    random.shuffle(total_content)

    # Split Train dataset / Test dataset / Validation dataset
    train_ratio = 0.80
    val_ratio = 0.10

    total_size = len(total_content)
    with open(os.path.join(BASE_DIR, 'train.dat'), 'a', encoding='utf-8') as f:
        point = int(total_size * train_ratio)

        for line in total_content[:point]:
            f.write(line+'\n')

    with open(os.path.join(BASE_DIR, 'val.dat'), 'a', encoding='utf-8') as f:
        start_point = int(total_size * train_ratio)
        end_point = int(total_size * (train_ratio + val_ratio))

        for line in total_content[start_point:end_point]:
            f.write(line + '\n')

    with open(os.path.join(BASE_DIR, 'test.dat'), 'a', encoding='utf-8') as f:
        point = int(total_size * (train_ratio + val_ratio))

        for line in total_content[point:]:
            f.write(line + '\n')


if __name__ == '__main__':
    args = get_args()
    if args.collect:
        if args.target == 'arxiv':
            collect_arxiv_paper_dataset()

