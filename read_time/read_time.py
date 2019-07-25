# -*- coding: utf-8 -*-

"""Main module."""
import bs4

from urllib.request import urlopen

from loguru import logger

# Words per minute
WPM = 200
WORD_LENGTH = 5


class ReadTime:
    def __init__(self, url, log_level="INFO"):
        self.url = url
        self.logger = logger
        self.logger.level(log_level.upper())

    def extract_text(self):
        html = urlopen(self.url).read()
        soup = bs4.BeautifulSoup(html, "html.parser")
        texts = soup.findAll(text=True)
        return texts

    @staticmethod
    def is_visible(element):
        if element.parent.name in ["style", "script", "[document]", "head", "title"]:
            return False
        elif isinstance(element, bs4.element.Comment):
            return False
        elif element.string == "\n":
            return False
        return True

    def filter_visible_text(self, page_texts):
        return list(filter(self.is_visible, page_texts))

    @staticmethod
    def count_words_in_text(text_list, word_length):
        total_words = 0
        for current_text in text_list:
            total_words += len(current_text) / word_length
        return total_words

    def estimate_reading_time(self):
        texts = self.extract_text()
        filtered_text = self.filter_visible_text(texts)
        total_words = self.count_words_in_text(filtered_text, WORD_LENGTH)
        guestimate = total_words / WPM
        return f"{guestimate:.2f} Min Read"
