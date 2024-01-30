import logging
import os
import sys
from datetime import datetime
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from sentence_transformers import SentenceTransformer, util
from webdriver_manager.chrome import ChromeDriverManager

from RecommendationSystem.Embedder.embedding_model import EmbeddingModel


def get_selenium_chrome_driver():
    """
    Instantiate Selenium Chrome driver to query dynamically loaded comment sections
    :return:
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    chrome_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
    chrome_logger.setLevel(logging.WARNING)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(5)
    return driver


def parse_pub_date(pub_date: str) -> datetime.date:
    if pub_date is None:
        return datetime.now().date()
    date = pub_date.split("T")[0]
    year = int(date.split("-")[0])
    month = int(date.split("-")[1])
    day = int(date.split("-")[2])
    return datetime(year=year, month=month, day=day).date()

class ScrapeTopicSpecific():
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.topic_specific_keywords = os.environ.get("TOPIC_SPECIFIC_KEYWORDS").split(" ")

    def is_correct_topic(self, article_keywords: List[str]) -> bool:
        """
        Checks if the article is thematically close to a required  topic
        """
        topic_specific_embeddings = self.embedding_model.embed(self.topic_specific_keywords)
        article_keywords_embeddings = self.embedding_model.embed(article_keywords)
        cosine_similarity_scores = util.cos_sim(topic_specific_embeddings, article_keywords_embeddings)
        for scores in cosine_similarity_scores:
            for score in scores:
                if score >= 0.65:
                    return True
        return False
