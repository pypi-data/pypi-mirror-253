FROM python:3.10

ENV PYTHONUNBUFFERED=1

ENV PYTHONPATH "${PYTHONPATH}:/code"

WORKDIR /code

COPY Pipfile .
COPY Pipfile.lock .
RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir pipenv
RUN apt-get update && apt-get install -y libgeos-dev
RUN pipenv install --deploy --system

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get install -y libglib2.0 libnss3 libgconf-2-4 libfontconfig1
RUN apt-get update && \
    apt-get install -y google-chrome-stable && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN chmod +x wait-for-it.sh
