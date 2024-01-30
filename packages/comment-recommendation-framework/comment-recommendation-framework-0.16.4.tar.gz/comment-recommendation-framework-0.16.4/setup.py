# setup.py
from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    include_package_data=True,
    name='comment-recommendation-framework',
    version='0.16.4',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={
        'comment_recommendation_framework': ['docker-compose.*.yml',
                                             'Dockerfile',
                                             "Pipfile",
                                             "Pipfile.lock",
                                             "wait-for-it.sh"
                                             "UI/"]}
)
