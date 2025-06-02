FROM python:3.10
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
