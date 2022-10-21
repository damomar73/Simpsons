FROM python
RUN apt-get update
RUN mkdir /app
RUN mkdir /app/Lisa
RUN mkdir /app/Homer
RUN mkdir /app/General

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app

CMD ["python","main.py"]
