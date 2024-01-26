FROM python:3.11-slim as builder

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY pyproject.toml .


COPY src src
RUN pip install -e .
RUN solc-select use 0.8.21 --always-install

ENTRYPOINT ["python", "src/ml/utils/deployer.py"]
CMD []
