FROM python:3.9-slim

WORKDIR /keyword-extraction

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /keyword-extraction

# EXPOSE 9004

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9004"]

