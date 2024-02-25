# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine

WORKDIR /app

# install the requirements
COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt


EXPOSE 5000/tcp

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]