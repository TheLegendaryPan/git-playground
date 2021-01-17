FROM python:3.8-slim-buster as builder

ENV POETRY_VERSION=1.0.10

# install poetry
RUN pip install "poetry==$POETRY_VERSION"

# set path of workdir in docker
WORKDIR /app

# copy my current dir to /app on WORKDIR
COPY . /app

# step to show my list of copied files and subdirectories
RUN ls -la ./

# turn off virtual envir creation from poetry as we're in docker
# install poetry dependencies #COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction

# Configure for production - multi build
FROM builder as production
#ENV POETRY_VERSION=1.0.10
#RUN pip install "poetry==$POETRY_VERSION"
#WORKDIR /app
#COPY --from=builder /app/ /app/ 
#RUN poetry config virtualenvs.create false \
#    && poetry install --no-interaction
# set my port on container to 5001
# Removed expose and port bind for 5001 due to port binding issue on Heroku
# EXPOSE 5001
# CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--log-level=debug", "app:create_app()"]
# good cmd 01/17/21
# CMD ["gunicorn", "--log-level=debug", "app:create_app()"]
# Testing below port binding with $PORT added to Heroku config vars
CMD ["gunicorn --log-level=debug --bind 0.0.0.0:$PORT app:create_app()"]

# Configure for development - multi build
FROM builder as development
#ENV POETRY_VERSION=1.0.10
#RUN pip install "poetry==$POETRY_VERSION"
#WORKDIR /app
#COPY --from=builder /app/ /app/ 
#RUN poetry config virtualenvs.create false \
#    && poetry install --no-interaction
EXPOSE 5002
CMD flask run --host=0.0.0.0 --port=5002

# Configure for testing - multi build
FROM builder as test
# Install curl
RUN apt-get update && apt-get install -y \ 
curl
# Install latest Chrome 
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
 apt-get install ./chrome.deb -y && \
 rm ./chrome.deb
EXPOSE 5003
ENTRYPOINT ["poetry", "run", "pytest"]


