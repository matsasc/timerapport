FROM python:alpine

RUN apk --update add build-base libxml2-dev libxslt-dev

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./app.py"]