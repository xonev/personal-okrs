FROM python:3.7.2

ENV FLASK_APP=personal_okrs
ENV FLASK_ENV=development

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "-p", "5000", "-h", "0.0.0.0"]
