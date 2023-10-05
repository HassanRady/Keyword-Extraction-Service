FROM python:3.9-slim

WORKDIR /src

COPY config.py .
COPY logger.py .
COPY keywords_extractor.py .
COPY main.py .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]