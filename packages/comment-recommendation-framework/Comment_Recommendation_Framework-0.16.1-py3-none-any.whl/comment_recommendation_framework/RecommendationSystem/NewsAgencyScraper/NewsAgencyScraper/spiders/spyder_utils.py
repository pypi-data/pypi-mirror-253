import logging
import os
import sys
import time
from datetime import datetime
from typing import List

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sentence_transformers import SentenceTransformer, util
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

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


def click_button_to_load_all_comments(driver: WebDriver, button_xpath: str) -> None:
    """
    Clicks the load new comments button to dynamically load all comments until all comments are loaded
    :param driver: Webdriver that queries the website
    :param button_xpath: XPath to button that should be clicked
    :return:
    """
    try:
        while driver.find_element(By.XPATH, button_xpath):
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
            driver.find_element(By.XPATH, button_xpath).click()
            time.sleep(os.environ.get("BUTTON_CLICK_SLEEP_TIME", 1))
            logging.info("Loaded more comments")
    except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException):
        logging.info("Cannot find Load more comments button")


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
