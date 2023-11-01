FROM python:3.8-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]