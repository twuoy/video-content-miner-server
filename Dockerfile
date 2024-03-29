FROM python:3.9.12-slim-bullseye

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./video_content_miner .

EXPOSE 5000

CMD [ "python", "-u", "app.py" ]
