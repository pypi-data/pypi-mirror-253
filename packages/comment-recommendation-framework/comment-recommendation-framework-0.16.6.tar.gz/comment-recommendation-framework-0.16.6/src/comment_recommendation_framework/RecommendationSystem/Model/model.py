import os
import sys
from typing import List

from RecommendationSystem.API.RESTApi.abstract_model import AbstractModel


class Model(AbstractModel):
    """
    Recommendation model to extract the recommendations from the database.
    """
    def get_recommendations(self, comment_data: dict) -> List[str]:
        """
        Interface method for the REST API view
        :param comment_data: Dict with all information the model needs to extract the recommendations from the database
        :return: List of recommendations
        """
        if len(comment_data.keys()) == 0:
            return []

        # Add model here
