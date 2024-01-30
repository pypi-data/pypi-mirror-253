from abc import ABC, abstractmethod
import torch


class AbstractEmbeddingModel(ABC):

    @abstractmethod
    def embed(self, text: str) -> torch.Tensor:
        """
        Computes the embedding for the given text and returns the vector representation
        :param text: Text that should be embedded
        :return: Torch tensor with embedding of the given text
        """
        pass
