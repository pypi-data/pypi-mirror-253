# setup.py

from setuptools import setup

setup(
    include_package_data=True,
    package_data={
        'comment_recommendation_framework': ['docker-compose.*.yml',
                                             'Dockerfile',
                                             "Pipfile",
                                             "Pipfile.lock",
                                             "wait-for-it.sh"
                                             "UI/"]}
)
