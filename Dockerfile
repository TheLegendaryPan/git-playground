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
EXPOSE 5001
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--log-level=debug", "app:create_app()"]

# Configure for development - multi build
FROM builder as development
#ENV POETRY_VERSION=1.0.10
#RUN pip install "poetry==$POETRY_VERSION"
#WORKDIR /app
#COPY --from=builder /app/ /app/ 
#RUN poetry config virtualenvs.create false \
#    && poetry install --no-interaction
EXPOSE 5002
CMD flask run --host=0.0.0.0