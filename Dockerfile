FROM python:3.10.13-bookworm

WORKDIR /opt/project

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=.
ENV BACKEND_SETTING_IN_DOCKER=true


# TODO(dmu) HIGH: Use the same pip version as suggested in README.md
RUN set -xe \
&& apt-get update \
&& apt-get install -y --no-install-recommends build-essential \
&& pip install virtualenvwrapper poetry==1.8.3 \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

COPY ["poetry.lock", "pyproject.toml", "./"]
RUN poetry install --no-root

COPY ["README.md", "Makefile", "./"]
COPY app app
COPY local local

# TODO(dmu) LOW: Reconsider having `EXPOSE 8000` since only Django needs, but not Celery or Discord bot
EXPOSE 8000


# Set up the entrypoint
COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]