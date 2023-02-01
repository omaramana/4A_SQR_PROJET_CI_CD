FROM ubuntu:16.04

RUN apt-get upgrade
RUN apt-get update 
RUN apt-get install python3-pip -y

CMD [ "export", "FLASK_APP=projet.py" ]
CMD [ "flask", "run" ]
