FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY application/pyproject.toml /code/
# Initialize python project with Poetry
RUN pip install --upgrade pip && pip install poetry
RUN poetry install

# # Chrome Driverのインストール
# RUN apt-get update && apt-get install -y wget unzip
# RUN wget -qO /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/LATEST_RELEASE/chromedriver_linux64.zip \
#     && unzip /tmp/chromedriver.zip -d /usr/local/bin \
#     && rm /tmp/chromedriver.zip

# # Edge Driverのインストール
# RUN wget -qO /tmp/edgedriver.zip https://msedgedriver.azureedge.net/latest/edgedriver_linux64.zip \
#     && unzip /tmp/edgedriver.zip -d /usr/local/bin \
#     && rm /tmp/edgedriver.zip

# # Firefox Driverのインストール
# RUN apt-get install -y firefox-geckodriver