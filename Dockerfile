FROM python:3.9-slim

WORKDIR /src

COPY src/config.py .
COPY src/logger.py .
COPY src/keywords_extractor.py .
COPY main.py .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]