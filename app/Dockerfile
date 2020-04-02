FROM python:2.7

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]