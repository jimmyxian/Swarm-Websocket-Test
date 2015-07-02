FROM centos:7

CMD yum install pip

CMD pip install websocket_client==0.32

COPY ./wssh.py /usr/bin/wssh
CMD chmod +x /usr/bin/wssh
