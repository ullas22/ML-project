from alpine:latest

RUN apk add --no-cashe python3-dev\
    && pip3 install --upgrade pip3

   WORKDIR /app
   COPY . /app
   RUN pip3 --no-cashe-dir install -r requirements.txt
   EXPOSE 5000

ENTRYPOINT ["python"]
CMD [app.py]    
