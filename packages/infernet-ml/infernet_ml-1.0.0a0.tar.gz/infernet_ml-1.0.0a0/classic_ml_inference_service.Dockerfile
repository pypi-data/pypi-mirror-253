FROM python:3.10-slim as builder

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /app
COPY pyproject.toml .

COPY src src
RUN apt-get update && pip install --upgrade pip && pip install ".[classic_inf]"

COPY classic_ml_inference_service classic_ml_inference_service


ENTRYPOINT ["hypercorn", "classic_ml_inference_service:create_app()"]
CMD ["-b", "0.0.0.0:3000"]
