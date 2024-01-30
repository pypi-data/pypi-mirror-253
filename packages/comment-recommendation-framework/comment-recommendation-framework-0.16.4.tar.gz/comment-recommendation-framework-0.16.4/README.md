# Comment Recommendation Framework

The Comment Recommendation Framework is a modular approach to support scientists in the development of prototypes for
comment recommendation systems that can be used in real-world scenarios. The advantage of such a system is that it
relieves the scientist from the majority of the technical code and only prototype-specific components have to be developed. In this way, the researchers can invest
more time in the development of recommendation models and less time has to be spent in the development of a prototype 
while at the same time getting prototypes that can be used in real-world settings.

## Setup
Ensure that the following tools are installed:
* Docker
* Docker-Compose
* Pyhon >= 3.10

## Documentation

To build the latest version of the documentation, please run in the docs folder:

```
$ make clean && make html
```

Then you find the latest documentation [here](src/comment_recommendation_framework/RecommendationSystem/docs/_build/html/index.html)

## Environment Variables
The framework need some environment variables to be set for running properly. Please ensure that you have an ```.env```
file with the following variables:
* NEO4J_PASSWORD
* NEO4J_BOLT_URL (Format: `bolt://neo4j:<NEO4J_PASSWORD>@neo4j:7687`)

## Run the Comment Recommendation Framework

### Install the package locally
To install the package locally, you have to build it first. For this, run in the folder with `setup.py`:
```
python3 -m build
```

Please make sure that the build library is installed. Otherwise, you cannot build the package.

This creates a `dist` folder at your current location with two files `Comment-Recommendation-Framework-X.X.X.tar.gz` and
`Comment_Recommendation_Framework-X.X.X-py3-none-any.whl`. The `tar.gz` file is the 
[source distribution](https://packaging.python.org/en/latest/glossary/#term-Source-Distribution-or-sdist) and the `.whl`
is the [built distribution](https://packaging.python.org/en/latest/glossary/#term-Built-Distribution).

We recommend to create a [virtual environment](https://docs.python.org/3/library/venv.html) to isolate your project from
the rest of your system to prevent import and version problems.

Then you run inside your virtual environment: 
```
pip install <path_to_the_whl_file>
```

### Create your project
To create the system template you run the following command in your virtual env after you have installed the package:
```
python3 -m comment_recommendation_framework
```
Then the package asks you different questions to determine which modules you need for your project. You can answer them 
with `y` for yes and `n` for no.

### Run different moduls with docker-compose
We provide you with the following `docker-compose` files to run the different components of the recommendation framework. 

* `docker-compose.scraping.yml`: Runs the news agency scraper to retrieve articles and comments from various news agencies.
* `docker-compose.embed.yml`: Starts the embedding process to compute the embeddings for the comments and articles. Should be run directly after `docker-compose.scraping.yml`.
* `docker-compose.csv.yml`: Imports comments and articles from a csv file into the database.
* `docker-compose.test.yml`: Runs the tests for the system.
* `docker-compose.api.yml`: Runs the comment-recommendation systems.

### User-Interface
If you would like to use the default user interface. You have to install the npm packages and build the chrome extension.
For this you have to run in the `UI` folder:

```bash
$ npm install
```

and afterwards:

```bash
$ npm run build
```

Then you can import the `build` folder in a chromium browser.


## Maintainers:
* Jan Steimann

## Contributors:
* Jan Steimann

## License:
Copyright(c) 2024 - today Jan Steimann

Distributed under the [MIT License](LICENSE)
