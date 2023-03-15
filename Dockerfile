FROM python:3.9.12-slim-bullseye

WORKDIR /app

RUN groupadd -r miner && \
    useradd -r -g miner miner

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./video_content_miner .

EXPOSE 5000

USER miner

CMD [ "python", "-u", "app.py" ]
