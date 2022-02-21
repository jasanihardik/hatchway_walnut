FROM python:3.9

#WORKDIR /Test_1/Assesment_1
WORKDIR /Users/jasanihardik/Desktop/DRIVE_E/Udemy-Python/API
#
#RUN yum -y install python3
#RUN yun -y install python3-pip
#RUN pip3 install -r /Test_1/Assesment_1/requirements.txt

CMD [ "python", "-m" , "--host=127.0.0.1/5000"]


#ENTRYPOINT ["/Test_1/Assesment_1/bootstrap_a.sh"]



