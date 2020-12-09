#!/usr/bin/env python3
# count.py
""" This is my solution to count_words Morsel """

from collections import defaultdict
import re


def count_words(str):
    words = re.findall(r"[0-9A-Za-z']+", str)
    words_freq = defaultdict(lambda: 0)
    for word in words:
        words_freq[word.lower()] += 1
    return dict(words_freq)


if __name__ == "__main__":
    print(count_words("This is a lovely day, so lovely day"))

