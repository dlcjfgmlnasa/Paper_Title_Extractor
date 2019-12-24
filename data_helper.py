# -*- coding:utf-8 -*-
import os
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', default='arxiv', choices=['arxiv', ], type=str)
    parser.add_argument('--collect', action='store_true')
    return parser.parse_args()


def collect_arxiv_paper_dataset():
    # Arxiv Paper 데이터셋 수집
    import arxiv


if __name__ == '__main__':
    args = get_args()
    if args.collect:
        if args.target == 'arxiv':
            collect_arxiv_paper_dataset()

