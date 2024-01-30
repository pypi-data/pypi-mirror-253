# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class NewsagencyscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ArticleDataItem(scrapy.Item):
    """
    Scrapy item that defines the field of the data item where we store the article and comment data
    """
    article_title = Field()
    keywords = Field()
    news_agency = Field()
    pub_date = Field()
    url = Field()

    comments = Field()
