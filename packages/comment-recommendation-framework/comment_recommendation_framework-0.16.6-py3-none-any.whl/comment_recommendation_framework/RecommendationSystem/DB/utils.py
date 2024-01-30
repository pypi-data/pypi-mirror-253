import os
from typing import List

import torch
from neomodel import config, db, StructuredNode

from RecommendationSystem.DB.db_models.article import Article
from RecommendationSystem.DB.db_models.comment import Comment

config.DATABASE_URL = os.environ.get("NEO4J_BOLT_URL", 'bolt://neo4j:test@neo4j:7687')


def __extract_results(results: List, node_type: StructuredNode) -> List:
    """
    Extracts the results from the query response
    :param results: Results from cypher query which should be inflated to nodes of type node_type
    :param node_type:
    :return: List with nodes of type node_type
    """
    return [node_type.inflate(row[0]) for row in results]


def get_article_by_title(title: str) -> Article:
    """
    Gets a specific article by the give title
    :param title: Title of the article
    :return: Article node with given title
    """
    results, _ = db.cypher_query(
        f"""
        MATCH (a:Article)
        WHERE a.article_title="{title}" AND a.embedding IS NOT NULL
        RETURN a
        """
    )
    if len(results) != 0:
        return __extract_results(results, Article)[0]
    return None


def get_article_by_id(article_id: int) -> Article:
    """
    Gets a specific article by the given id
    :param article_id: ID of article node
    :return: Article node with given ID
    """
    results, _ = db.cypher_query(
        f"""
        MATCH (a:Article)
        WHERE a.article_id='{article_id}' AND a.embedding IS NOT NULL
        RETURN a
        """
    )
    if len(results) != 0:
        return __extract_results(results, Article)[0]
    return None


def get_all_article() -> List:
    """
    Gets all article from the db which embedding is not null
    :return: All articles from the database whose embedding is not NULL
    """
    results, _ = db.cypher_query(
        """
        MATCH (a:Article)
        WHERE a.embedding IS NOT NULL
        RETURN a
        """
    )
    return __extract_results(results, Article)


def get_comment_by_id(comment_id: int) -> Comment:
    """
    Gets a specific comment by the given id
    :param comment_id: ID of the comment
    :return: Comment node with given ID
    """
    results, _ = db.cypher_query(
        f"""
        MATCH(c:Comment)
        WHERE c.comment_id='{comment_id}' AND c.embedding IS NOT NULL
        RETURN c
        """
    )
    if len(results) != 0:
        return __extract_results(results, Comment)[0]
    return None


def get_all_comments_for_given_article(article: Article) -> List[Comment]:
    """
    Returns all comments connected to the given article
    :param article: Article node
    :return: List of all comment nodes that are connected with the given article node
    """
    results, _ = db.cypher_query(
        f"""
        MATCH (a:Article)<-[:BELONGS_TO]-(c:Comment)
        WHERE a.article_id='{article.article_id}' AND c.embedding IS NOT NULL
        RETURN c
        """
    )
    return __extract_results(results, Comment)


def run_cypher_query(query: str, node_type) -> List:
    """
    Runs a give cypher query to handle special cases
    :param query: Cypher query string to extract specific data from the Neo4J database
    :param node_type: Type of the expected node to be returned
    :return: List of nodes for the given cypher query
    """
    results, _ = db.cypher_query(query)
    return __extract_results(results, node_type)

def get_articles_without_embedding():
    """
    Gets all article without an embedding
    :return:
    """
    results, _ = db.cypher_query(
        """
        MATCH (a:Article)
        WHERE a.embedding IS NULL
        RETURN a
        """
    )

    return __extract_results(results, Article)


def get_comments_without_embedding():
    """
    Gets all comments without an embedding
    :return:
    """
    results, _ = db.cypher_query(
        """
        MATCH (c:Comment)
        WHERE c.embedding IS NULL
        RETURN c
        """
    )
    return __extract_results(results, Comment)


def update_node_with_embedding(node: StructuredNode, embedding: torch.Tensor):
    """
    Updates the given node with the given embedding
    :param node:
    :param embedding:
    :return:
    """
    node.embedding = embedding.tolist()
    node.save()
