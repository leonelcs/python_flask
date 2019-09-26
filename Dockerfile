FROM python:3.7-slim-stretch
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENV FLASK_APP=/app/main.py
CMD ["flask", "run", "--host", "0.0.0.0"]
