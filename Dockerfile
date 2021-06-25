FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

ARG APP_USER=appuser

RUN groupadd -r ${APP_USER} -g 1000 && useradd --no-log-init --create-home -u 1000 -r -g ${APP_USER} ${APP_USER}

ARG APP_DIR=/home/${APP_USER}/project/
RUN echo $APP_DIR && mkdir ${APP_DIR} && chown ${APP_USER}:${APP_USER} ${APP_DIR}
COPY ./requirements.txt ${APP_DIR}

RUN set -ex &&\
    pip install --upgrade pip && \
    pip install --no-cache-dir -r ${APP_DIR}requirements.txt

RUN apt-get -q update && \
    apt-get -qy install postgresql-client \
    musl-dev \
    gcc \
    netcat \
    gettext \
    libgettextpo-dev \
    libjpeg-dev \
    xmlsec1 && \
    rm -rf /var/lib/apt/lists/* \
    chromium-chromedriver \
    python-selenium \
    python3-selenium \
    google-chrome-stable

COPY --chown=${APP_USER}:${APP_USER} . ${APP_DIR}
USER ${APP_USER}:${APP_USER}

WORKDIR ${APP_DIR}

CMD ["python", "main.py"]
#
#COPY requirements.txt /code/
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
#
#COPY . /code/

#RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` \
#  && curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip \
#  && unzip /tmp/chromedriver_linux64.zip \
#  && mv chromedriver /usr/local/bin/