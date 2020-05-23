FROM centos:latest


RUN dnf install python36 -y
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow
RUN pip3 install keras
RUN pip3 install pillow 


CMD ["python3","/mlopsj2/mnistmlops.py"]
