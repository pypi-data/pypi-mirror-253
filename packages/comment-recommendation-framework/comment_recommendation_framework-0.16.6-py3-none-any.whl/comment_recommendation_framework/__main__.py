# __main__.py
import logging
import os.path
import shutil
import sys
from os import mkdir
from distutils.dir_util import copy_tree
from pathlib import Path

logging.getLogger().setLevel(logging.INFO)

package_dir = sys.modules['comment_recommendation_framework'].__path__[0]


def copy(relative_path: str, folder: str) -> None:
    """
    Copy the give file or directory to Recommendation System in the current working directory
    :param relative_path:
    :param folder
    :return:
    """
    logging.info("Copy " + folder + " to: " + relative_path)
    object_path = os.path.join(package_dir, relative_path)
    try:
        destination = os.path.join(os.getcwd(), "RecommendationSystem/")
        if not Path(destination).exists():
            mkdir(destination)
        if Path(object_path).is_file():
            shutil.copy(object_path, destination)
        elif Path(object_path).is_dir():
            folder_destination = os.path.join(destination, folder)
            if not Path(folder_destination).exists():
                os.makedirs(folder_destination)
            copy_tree(object_path, folder_destination)
    except shutil.SameFileError:
        logging.error("File already exists in destination folder")
    except PermissionError:
        logging.error("Do not have permission to write in the current directory")


# Source: https://stackoverflow.com/questions/33499866/how-can-i-copy-files-from-a-python-package-site-packages-to-a-directory Accessed on 07/07/2022
def main():
    logging.info("Do you want to create the template project? [Y/N]")
    for line in sys.stdin:
        if 'y' == line.rstrip().lower():
            logging.info("Copy files from package")

            logging.info("Copy Pipefile and Pipefile.lock")
            copy("Pipfile", "")
            copy("Pipfile.lock", "")

            logging.info("Copy Docker for API")
            copy("Dockerfile", "")
            copy("docker-compose.api.yml", "")
            copy("wait-for-it.sh", "")

            logging.info("Copy API folder")
            copy("RecommendationSystem/API/", "RecommendationSystem/API")

            logging.info("Copy DB utils")
            copy("RecommendationSystem/DB/", "RecommendationSystem/DB")

            logging.info("Copy Embedder folder")
            copy("RecommendationSystem/Embedder/", "RecommendationSystem/Embedder")
            copy("docker-compose.embed.yml", "")

            logging.info("Copy Model template")
            copy("RecommendationSystem/Model/", "RecommendationSystem/Model")

            logging.info("Copy UI template")
            copy("RecommendationSystem/UI/", "RecommendationSystem/UI")

            logging.info("Copy tests")
            copy("RecommendationSystem/test/", "RecommendationSystem/test")
            copy("docker-compose.test.yml", "")

            break
        elif 'n' == line.rstrip().lower():
            break
    logging.info("Do you want to scrape news agency sites for articles and comments? [Y/N]")
    for line in sys.stdin:
        if 'y' == line.rstrip().lower():
            logging.info("Copy Scraper folder")
            copy("RecommendationSystem/NewsAgencyScraper/", "RecommendationSystem/NewsAgencyScraper")

            logging.info("Copy Docker for scraping and embedding")
            copy("docker-compose.scraping.yml", "")

            break
        elif 'n' == line.rstrip().lower():
            break

    logging.info("Do you want to read your data from CSV files [Y/N]?")
    for line in sys.stdin:
        if 'y' == line.rstrip().lower():
            logging.info("Copy CSV reader")
            copy("RecommendationSystem/Read_CSV/", "RecommendationSystem/Read_CSV")
            copy("docker-compose.csv.yml", "")
            break
        elif 'n' == line.rstrip().lower():
            break
    print("Done")


if __name__ == '__main__':
    main()
