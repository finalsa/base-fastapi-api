FROM python:3.8

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt


WORKDIR /app
COPY app .
COPY cicd/start.sh .

EXPOSE 80
ENTRYPOINT [ "/app/start.sh" ]