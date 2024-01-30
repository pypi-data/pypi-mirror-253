from typing import List

from django.http import JsonResponse, HttpRequest
from RecommendationSystem.Model.model import Model

model = Model()


def get_recommendations(request: HttpRequest) -> JsonResponse:
    """
    Receives Http request, extracts user comment and other information and triggers model to get suitable recommendations.
    Sends the recommendations as a JSON response back to user interface.
    :param request: request where the data for the recommendation model are extracted.
    :return: Json Response with comment recommendations.
    """

    # Retrieve here the information needed by the model from the request
    comment_data: dict = {
        "user_comment": request.GET.get("user_comment"),
        "keywords": request.GET.get("keywords")
    }
    # Replace with actual model that inherits form the abstract superclass
    suggestions: List = model.get_recommendations(comment_data)

    return JsonResponse({"suggestions": suggestions})
