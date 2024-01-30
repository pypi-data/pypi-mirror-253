from neomodel import StructuredNode, StringProperty, ArrayProperty, RelationshipFrom, UniqueIdProperty, DateProperty


class Article(StructuredNode):
    """
    Neomodel structured node that defines the properties for the articles that are stored in the Neo4J database
    """
    article_id = UniqueIdProperty()
    article_title = StringProperty()
    news_agency = StringProperty()
    keywords = StringProperty()
    pub_date = DateProperty()
    embedding = ArrayProperty()
    url = StringProperty()

    comment = RelationshipFrom('.comment.Comment', 'BELONGS_TO')
