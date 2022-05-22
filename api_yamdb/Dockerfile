#FROM python:3.7-slim
#COPY ./ /app
#RUN pip install -r /app/requirements.txt
#WORKDIR /app/
#CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]

FROM python:3.7-slim

WORKDIR /app

COPY ./ /app

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY api_yamdb/ /app

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]