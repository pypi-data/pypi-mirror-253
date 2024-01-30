import os
import sys
import unittest
from typing import List

ROOT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.path.pardir
))

sys.path.append(ROOT_DIR + "/API")
print(sys.path)

from RecommendationSystem.Model.model import Model

class TestModel(unittest.TestCase):
    def test_get_recommendations_empty_dict_no_recommendations_found(self):
        model: Model = Model()
        recommendations: List = model.get_recommendations({})
        self.assertEqual(len(recommendations), 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
