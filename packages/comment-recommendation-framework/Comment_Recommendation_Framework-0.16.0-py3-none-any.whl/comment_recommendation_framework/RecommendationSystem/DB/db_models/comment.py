from neomodel import StructuredNode, StringProperty, ArrayProperty, RelationshipTo, UniqueIdProperty


class Comment(StructuredNode):
    """
    Neomodel structured node that defines the properties for the comments that are stored in the Neo4J database
    """
    comment_id = UniqueIdProperty()
    text = StringProperty()
    embedding = ArrayProperty()

    article = RelationshipTo('.article.Article', 'BELONGS_TO')
