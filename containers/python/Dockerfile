FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY application/pyproject.toml /code/
# Initialize python project with Poetry
RUN pip install --upgrade pip && pip install poetry
RUN poetry install

# Chrome Driverのインストール
# https://chromedriver.chromium.org/downloads
RUN apt-get update && apt-get install -y wget unzip
RUN wget -qO /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin \
    && rm /tmp/chromedriver.zip

# Edge Driverのインストール
# https://developer.microsoft.com/ja-jp/microsoft-edge/tools/webdriver/
RUN wget -qO /tmp/edgedriver.zip https://msedgedriver.azureedge.net/114.0.1823.18/edgedriver_linux64.zip \
    && unzip /tmp/edgedriver.zip -d /usr/local/bin \
    && rm /tmp/edgedriver.zip

# Firefox Driverのインストール
# https://github.com/mozilla/geckodriver/releases
# RUN apt-get install -y firefox-geckodriver
RUN wget -qO /tmp/geckodriver.tar https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux32.tar.gz \
    && tar -xvzf /tmp/geckodriver.tar -C /usr/local/bin \
    && rm /tmp/geckodriver.tar
