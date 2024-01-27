FROM python:3.10-slim as builder

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_NO_CACHE_DIR 1

WORKDIR /app
COPY pyproject.toml .

COPY src src
RUN apt-get update && pip install --upgrade pip && pip install --no-cache-dir ".[llm_inf]"

COPY llm_inference_service llm_inference_service


ENTRYPOINT ["hypercorn", "llm_inference_service:create_app()"]
CMD ["-b", "0.0.0.0:3000"]
