FROM python:2.7

CMD pip install websocket_client==0.32

COPY ./wssh.py /usr/bin/wssh
CMD chmod +x /usr/bin/wssh
