#python version 
FROM python:3 
COPY . /app
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD python main.py
