FROM python:alpine3.7
COPY . /flask-apis
WORKDIR /flask-apis
RUN pip install -r requirements.txt
EXPOSE 9090
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]