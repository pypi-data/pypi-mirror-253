# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
import os

from neomodel import config

from RecommendationSystem.DB.db_models.article import Article
from RecommendationSystem.DB.db_models.comment import Comment
from scrapy import Item

config.DATABASE_URL = os.environ.get("NEO4J_BOLT_URL", 'bolt://neo4j:test@neo4j:7687')


class ScraperPipeline(object):

    def process_item(self, item, spider) -> Item:
        """
        Stores the articles and comments in the database
        This method is called every time an item is processed
        :param item: Article item with information about the article and the comments that are published under the
        article
        :param spider:
        :return: Unmodified item. The data are only extracted and stored in the database.
        """
        logging.info("Process item")

        article: Article = Article.nodes.get_or_none(article_title=item["article_title"][0])

        if article is None:
            article = Article(
                article_title=item["article_title"][0],
                keywords=item["keywords"][0],
                news_agency=item["news_agency"][0],
                pub_date=item["pub_date"][0],
                url=item["url"][0]
            ).save()

        if "comments" not in item.keys():
            return item

        for comment_text in item["comments"]:
            comment: Comment = Comment.nodes.get_or_none(text=comment_text)
            if comment is None:
                comment = Comment(
                    text=comment_text
                ).save()
                article.comment.connect(comment)
        return item
