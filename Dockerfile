from python:3.8.0-buster

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["pyton", "app.py"]
