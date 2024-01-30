import csv
import os
import sys
from datetime import datetime
from typing import Dict, Set

from neomodel import config
from tqdm import tqdm



from RecommendationSystem.DB.db_models.article import Article
from RecommendationSystem.DB.db_models.comment import Comment

config.DATABASE_URL = os.environ.get("NEO4J_BOLT_URL", 'bolt://neo4j:test@neo4j:7687')


def __get_article_ids_from_comments(filepath) -> Set:
    """
    Get the  article ids the comments are connected with from the csv file
    :param filepath: File path of the csv file
    :return: Set with all article ids from the comments
    """
    with open(filepath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print("Start reading comments")

        line_counter = 0
        article_ids = []
        for node in csv_reader:
            if line_counter == 0:
                line_counter += 1
                continue
            else:
                article_ids.append(node["<column_name_for_article_id>"])

        return set(article_ids)


def __get_articles_from_db(article_ids) -> Dict:
    """
    The article nodes for the  given ids from the db and store them in a dict
    :param article_ids:
    :return:
    """
    articles = {}

    for id in article_ids:
        articles[id] = Article.nodes.get_or_none(article_id=id)

    return articles


def store_comments_in_db(comment_file_path: str) -> None:
    """
    Reads the given comment file and stores them in the db
    :param comment_file_path:
    :return:
    """
    article_ids = __get_article_ids_from_comments(comment_file_path)
    articles = __get_articles_from_db(article_ids)

    with open(comment_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_counter = 0
        for node in tqdm(csv_reader):
            if line_counter == 0:
                line_counter += 1
                continue
            else:
                if articles[node["<row name for article id>"]] is not None:
                    __store_comment(node, articles)
            line_counter += 1


def __store_comment(node: dict, articles: Dict) -> None:
    """
    Stores the given node in the db
    :param node:
    :return:
    """
    if Comment.nodes.get_or_none(text=node["<column_name>"]) is None:
        comment: Comment = Comment(
           text=node["<column_name>"]
        ).save()
        article = articles[node["<column_name>"]]
        article.comment.connect(comment)


def store_articles_in_db(article_file: str) -> None:
    """
    Reads the give article file and stores them in the db
    :param article_file:
    :return:
    """
    with open(article_file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_counter = 0
        for node in tqdm(csv_reader):
            if line_counter == 0:
                line_counter += 1
            else:
                __store_article(node)


def __store_article(article: Dict) -> None:
    """
    Stores the give node in the db
    :param article: Dict with article information
    :return:
    """
    # Save the node in the db like this
    if Article.nodes.get_or_none(article_id=article["<column_name>"]) is None:
        Article(
            article_id=article["<column_name>"],
            article_title=article["<column_name>"],
            news_agency="<NewsAgencyName>",
            keywords=article["<column_name>"],
            pub_date=datetime.today().date(),
            url=article["<column_name>"]
         ).save()


def main() -> None:
    """
    Store all data from csv in db
    :return: None
    """
    # Make a list of all csv files you would like to store in the db like this
    article_file_paths = ["Read_CSV/data/<filename>"]
    comment_file_paths = ["Read_CSV/data/<filename>"]

    for article_file_path in article_file_paths:
        store_articles_in_db(article_file_path)

    for comment_file_path in comment_file_paths:
        store_comments_in_db(comment_file_path)


if __name__ == '__main__':
    main()
