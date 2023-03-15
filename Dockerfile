ARG USER=appuser
ARG POETRY_VERSION=1.4.0

FROM python:3.10-slim
ARG USER
ARG POETRY_VERSION
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1
RUN pip install poetry=="${POETRY_VERSION}"
ENV UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    "${USER}"
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN poetry export -f requirements.txt | pip install -r /dev/stdin
COPY . /app
USER ${USER}:${USER}
ENTRYPOINT ["python3", "main.py"]
