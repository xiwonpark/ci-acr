FROM python:3.11-slim

WORKDIR /home/python

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /home/python/app

CMD ["python", "/home/python/app/main.py"]