FROM python:3.10-slim as builder

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# download rust and checkout ezkl libary
RUN apt update && apt -y install git-all && apt -y install build-essential && apt-get -y install curl && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && git clone https://github.com/zkonduit/ezkl.git && cd ezkl && git checkout v3.7.6
# make sure cargo is on the path
ENV PATH="/root/.cargo/bin:${PATH}"
WORKDIR /app/ezkl
# copy patched files to src
COPY ezkl/* src
# create venv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
# create custom build of ezkl
RUN pip install --upgrade pip && pip install -r requirements.txt && maturin build --release --features python-bindings


FROM python:3.10-slim
WORKDIR /app
# copy custom ezkl build wheel
COPY --from=builder /app/ezkl/target/wheels /wheels
COPY pyproject.toml .
COPY src src
RUN apt-get update && pip install --no-cache-dir ".[proving]" && pip install --upgrade --no-cache-dir pip && pip install --no-cache-dir --no-cache /wheels/*

COPY classic_ml_proof_service classic_ml_proof_service


ENTRYPOINT ["hypercorn", "classic_ml_proof_service:create_app()"]
CMD ["-b", "0.0.0.0:3000"]
