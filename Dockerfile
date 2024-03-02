FROM python:3.9-slim

WORKDIR /src

COPY src/ src/
COPY main.py .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]