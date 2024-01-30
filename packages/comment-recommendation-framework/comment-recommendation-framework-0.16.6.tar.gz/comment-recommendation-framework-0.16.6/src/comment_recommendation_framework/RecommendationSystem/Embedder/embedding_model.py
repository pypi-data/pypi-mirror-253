import os

import torch

from RecommendationSystem.Embedder.abstract_embedding_model import AbstractEmbeddingModel


class EmbeddingModel(AbstractEmbeddingModel):

    def embed(self, text: str) -> torch.Tensor:
        """
        Computes the vector representation of the given text
        :param text: Text that should be embedded
        :return: Torch tensor with embedding of the given text
        """
        embedding_vector = torch.Tensor()
        # Implement embedding method here

        return embedding_vector
