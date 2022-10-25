FROM python
RUN apt-get update
RUN mkdir /Ejercicio2

WORKDIR /Ejercicio2

COPY requirements.txt /Ejercicio2
RUN pip install -r requirements.txt
COPY . /Ejercicio2

CMD ["python","main.py"]