
FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip nginx dstat && \
    pip3 install psutil

COPY monitoramento.py /usr/local/bin/monitoramento.py

CMD ["python3", "/usr/local/bin/monitoramento.py"]
