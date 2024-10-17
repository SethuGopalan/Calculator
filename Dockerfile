FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install dash

EXPOSE  8050

CMD ["python", "Calculator.py"]