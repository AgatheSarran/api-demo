FROM python:3.12-trixie

COPY app /app
COPY src /src
COPY README.md README.md
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


RUN uv sync


CMD ["uv", "run", "uvicorn", "app.simple:app", "--host", "0.0.0.0", "--port", "8080"]
