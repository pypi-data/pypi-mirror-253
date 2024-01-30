import unittest
from datetime import datetime

from RecommendationSystem.DB.db_models.article import Article
from RecommendationSystem.DB.db_models.comment import Comment
from RecommendationSystem.Embedder.run_embedder import main


class TestEmbedder(unittest.TestCase):
    def setUp(self) -> None:
        """
        Prepares neo4j db with entries
        :return:
        """
        self.article_1: Article = Article(
            title='Article 1',
            news_agency='Foo Bar News',
            keywords='Keyword1 Keyword2',
            pub_date=datetime(year=2022, month=1,  day=1)
        ).save()

        self.article_2: Article = Article(
            title='Article 2',
            news_agency='Foo Bar News',
            keywords='Keyword3 Keyword4',
            pub_date=datetime(year=2022, month=1,  day=1)
        ).save()

        self.comment_1: Comment = Comment(
            text="I am comment 1",
        ).save()

        self.comment_2: Comment = Comment(
            text="I am comment 2",
        ).save()

        self.comment_3: Comment = Comment(
            text="I am comment 3",
        ).save()

        self.article_1.comment.connect(self.comment_1)
        self.article_1.comment.connect(self.comment_2)
        self.article_2.comment.connect(self.comment_3)

    def tearDown(self) -> None:
        """
        Cleans up database after every test
        :return:
        """
        for article in Article.nodes.all():
            article.comment.disconnect_all()
            article.delete()

        for comment in Comment.nodes.all():
            comment.delete()

    def test_main_should_update_nodes_with_embeddings(self):
        self.assertIsNone(self.article_1.embedding)
        self.assertIsNone(self.article_2.embedding)

        main()

        self.article_1.refresh()
        self.article_2.refresh()

        self.assertIsNotNone(self.article_1.embedding)
        self.assertIsNotNone(self.article_2.embedding)


if __name__ == '__main__':
    unittest.main()
